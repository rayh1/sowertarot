#!/bin/sh
# Cron entry point (07:00): update the repository, write today's reading in a background Claude session,
# then stop it. Cron's environment is minimal, so set PATH here: claude is in /usr/local/bin, gh in /usr/bin.
export PATH=/usr/local/bin:/opt/venv/bin:/usr/bin:/bin
SCRIPTS=$(dirname "$(readlink -f "$0")")
log() { echo "$(date '+%F %T') $*"; }
# Settings (settings.env, settings.local.env): SOWER_DAILY_DIR for the failure logs, SOWER_CLAUDE_DIR to start in.
if ! settings=$("$SCRIPTS/daily.py" settings 2>&1); then log "FAILED to read the settings: $settings"; exit 1; fi
eval "$settings"
cd "$SOWER_CLAUDE_DIR" || exit 1

# Update first, then run: pull main, then start this script again from its updated copy, so the rest of the
# run uses the updated scripts and deck. TAROT_UPDATED marks the second start, which must not pull again.
if [ -z "$TAROT_UPDATED" ]; then
  if ! out=$("$SCRIPTS/daily.py" pull 2>&1); then log "FAILED to update the repository: $out"; exit 1; fi
  export TAROT_UPDATED=1
  exec "$SCRIPTS/run-daily.sh"
fi

if "$SCRIPTS/daily.py" status >/dev/null; then log "today's reading already exists"; exit 0; fi

out=$(claude --bg "/tarot-daily-reading" --allowedTools=Artifact,Bash,Read,Write < /dev/null 2>&1)
id=$(printf '%s\n' "$out" | sed -n 's/.*backgrounded · \([0-9a-f]*\).*/\1/p')
if [ -z "$id" ]; then log "could not start a session: $out"; exit 1; fi
log "started session $id"

state() {
  claude agents --json 2>/dev/null | /opt/venv/bin/python -c '
import json, sys
print(next((a.get("state", "") for a in json.load(sys.stdin) if a.get("id") == sys.argv[1]), "gone"))' "$1"
}
# Wait up to 30 minutes for the published marker. A session that published a page keeps watching it
# for comments and stays "working", so the marker, not the session state, signals the end.
i=0
while [ $i -lt 180 ]; do
  "$SCRIPTS/daily.py" status --published >/dev/null && break
  s=$(state "$id")
  case $s in working|starting|"") ;; *) break ;; esac
  sleep 10; i=$((i + 1))
done
s=$(state "$id")

if "$SCRIPTS/daily.py" status --published >/dev/null; then
  log "done (session state: $s)"
else
  failed="$SOWER_DAILY_DIR/failed-$(date +%F)-$id.log"
  claude logs "$id" > "$failed" 2>&1
  log "FAILED (session state: $s); session output saved to $failed"
fi
claude stop "$id" >/dev/null 2>&1

# The session's save pushes the reading; push again in case that failed, so the site gets it.
if "$SCRIPTS/daily.py" status >/dev/null; then
  out=$("$SCRIPTS/daily.py" push 2>&1) || log "FAILED to push the reading: $out"
fi

#!/bin/sh
# Cron entry point (07:00): update the repository, write today's reading in a Claude session, then back up
# content/. Cron's environment is minimal, so set PATH here: claude and rclone are in /usr/local/bin, gh in /usr/bin.
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

if "$SCRIPTS/daily.py" status >/dev/null; then
  log "today's reading already exists"
else
  # Print mode waits for the session to finish; stop it after 30 minutes.
  out=$(timeout 1800 claude -p "/tarot-daily-reading" --allowedTools=Bash,Read,Write < /dev/null 2>&1)
  rc=$?
  if "$SCRIPTS/daily.py" status >/dev/null; then
    log "done: $(printf '%s\n' "$out" | tail -1)"
  else
    failed="$SOWER_DAILY_DIR/failed-$(date +%F-%H%M%S).log"
    printf '%s\n' "$out" > "$failed"
    log "FAILED (claude exit $rc); session output saved to $failed"
  fi
fi

# The session's save pushes the reading; push again in case that failed, so the site gets it.
if "$SCRIPTS/daily.py" status >/dev/null; then
  out=$("$SCRIPTS/daily.py" push 2>&1) || log "FAILED to push the reading: $out"
fi
# Trigger draws (The Sower or The Miner as the day's card): a Parked note and an email, once per draw. A failure
# is logged and never fails the reading; an unannounced draw is tried again the next morning.
if out=$("$SCRIPTS/daily.py" notify 2>&1); then
  [ -n "$out" ] && printf '%s\n' "$out" | while IFS= read -r line; do log "$line"; done
else
  log "FAILED to notify: $(printf '%s' "$out" | tr '\n' ' ')"
fi
# Back up content/ (also catches hand edits to card files and media); a failure never fails the reading.
out=$("$SCRIPTS/daily.py" backup 2>&1) || log "FAILED to back up: $out"

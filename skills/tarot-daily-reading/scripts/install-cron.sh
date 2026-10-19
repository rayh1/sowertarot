#!/bin/sh
# Make the crontab's tarot-daily line run run-daily.sh at 07:00, logging to $SOWER_DAILY_DIR/cron.log (from
# the settings). Idempotent; ~/.profile runs it at every container start, because a recreated container starts
# with an empty crontab. The line names run-daily.sh by the path this script was started by, so start it
# through the production clone (or its skill link), never from a test clone.
command -v crontab >/dev/null || exit 0
HERE=$(cd "$(dirname "$0")" && pwd)
settings=$("$HERE/daily.py" settings) || exit 1
eval "$settings"
mkdir -p "$SOWER_DAILY_DIR"
WANT="0 7 * * * $HERE/run-daily.sh >> $SOWER_DAILY_DIR/cron.log 2>&1 # tarot-daily"
[ "$(crontab -l 2>/dev/null | grep tarot-daily)" = "$WANT" ] && exit 0
{ crontab -l 2>/dev/null | grep -v tarot-daily; echo "$WANT"; } | crontab -

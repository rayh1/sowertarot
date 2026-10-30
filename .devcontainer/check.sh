#!/usr/bin/env bash
# The project's checks: install the dependencies, then run the default checks of every language
# whose manifest is at the top of the repository. The "Run Checks" task runs this file in the dev
# container; CI runs it through .devcontainer/ci.sh in a fresh container from the project's image.
# Every check runs even when an earlier one fails; the exit code is 1 when any check failed and 0
# when none did. A failing dependency install stops it at once.
#
# This file is project-owned: `copier update` never overwrites it. Add, change or drop checks here.
set -uo pipefail
cd "$(dirname "$0")/.."

TDP_CI=1 bash .devcontainer/update.sh || exit $?

failed=0
check() {
  echo "==> $*"
  if ! "$@"; then
    echo "==> FAILED: $*"
    failed=1
  fi
}

if [ -f pyproject.toml ]; then
  check uv run ruff check
  echo "==> uv run pytest"
  rc=0
  uv run pytest || rc=$?
  # Exit code 5 means pytest collected no tests: a project without tests passes.
  if [ "$rc" -ne 0 ] && [ "$rc" -ne 5 ]; then
    echo "==> FAILED: uv run pytest"
    failed=1
  fi
fi

if [ -f package.json ]; then
  if jq -e '.scripts | objects | has("check")' package.json > /dev/null 2>&1; then
    check npm run check
  else
    check npm run lint --if-present
    check npm test --if-present
  fi
fi

if [ -f pom.xml ]; then
  check mvn -B verify
fi

if [ -f pubspec.yaml ]; then
  check flutter analyze
  if [ -d test ]; then
    check flutter test
  fi
fi

exit "$failed"

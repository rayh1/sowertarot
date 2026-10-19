#!/usr/bin/env bash
# Synchronise project dependencies for every language in this project. Runs on container create
# (updateContentCommand) and from the "Sync Dependencies" task. Never prompts.
set -euo pipefail
cd "$(dirname "$0")/.."
export CI=1

if [ -f pyproject.toml ]; then
  uv sync
fi
if [ -f package-lock.json ]; then
  npm ci
elif [ -f package.json ]; then
  npm install
fi
if [ -f pom.xml ]; then
  mvn -q -B dependency:go-offline
fi
if [ -f pubspec.yaml ]; then
  flutter pub get
fi

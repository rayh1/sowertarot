# The sowertarot dev container

Ten-Day Project (python, node) rendered from the `tdp-template` copier template. Python
is part of every project; the other languages come from the `languages` answer in
`.copier-answers.yml`.

This file belongs to the template and `copier update` keeps it current. The project's own
documentation belongs in the top-level `README.md`, which the template never overwrites.

## Getting started

1. Open this folder in VS Code and choose **Reopen in Container**. The image builds from
   `.devcontainer/Dockerfile` with the versions pinned in `.devcontainer/.env`. On create,
   `bash .devcontainer/update.sh` syncs the dependencies.
   The first create writes the lockfiles — `uv.lock` and, for a node project, `package-lock.json`
   — into the workspace: commit and push them, so every later create installs the same versions.
2. Git identity and the gh login are copied from the host on every attach.
3. **Sync Dependencies** runs `bash .devcontainer/update.sh` again. Every hook and task runs its
   script through `bash`, so a checkout without the executable bit (Windows cannot store it)
   works too; `.gitattributes` keeps the scripts and the Dockerfile on LF whatever
   `core.autocrlf` says.

## The workspace is a named volume

`/workspace` inside the container is a Docker named volume seeded from the image, not a mount of
this folder. Edits inside the container do not reach the host folder; push your branches to
the remote to get work out. `docker compose down -v` deletes the volume and with it all work that
was not pushed. A plain `docker compose down` (or VS Code's rebuild) keeps it.

Package caches (`uv`, `npm`) and shell history also
live in named volumes and survive rebuilds. Nothing credential-like does: the `gh` login lives in
the container's own filesystem and is gone after a container recreate.

## Tools in the image

`uv` with a pinned CPython, Node, `gh`, Playwright with Chromium (browsers in `/opt/playwright`),
`git`, `jq`, `rg`.
The project's Python environment is `.venv` in the workspace, created by `uv sync` from
`.python-version`.

## Host files used by the container

The home directory is `HOME` on Linux and macOS and `USERPROFILE` on Windows (compose's
`${HOME:-${USERPROFILE}}` fallback in `.devcontainer/compose.yaml`); `~` below means that directory.

- `~/.gitconfig` (read-only): `user.name` and `user.email` are copied in when unset.
- `~/.config/gh` (read-only): the gh login (`hosts.yml`) is copied in when present and the
  container has none.
- Environment: `GH_TOKEN` is passed through when set; `USER_UID`/`USER_GID`
  select the container user's ids (default `1000`). Compose lets shell variables override
  `.devcontainer/.env`, so a `NODE_VERSION` or `PYTHON_VERSION` exported in your shell would
  replace the pin; unset such variables before building.

## Troubleshooting

- The container create fails with `all predefined address pools have been fully subnetted`:
  Docker has run out of subnets for compose networks. Remove networks of projects you no longer
  use (`docker network ls`, then `docker compose down` in that project), or give Docker a larger
  pool in Docker Desktop's engine settings (Settings > Docker Engine, the `default-address-pools`
  key, e.g. `"default-address-pools": [{"base": "10.201.0.0/16", "size": 24}]`) and restart Docker.

## Project-owned extension points

- `README.md` — the project's own README at the top of the repository: written once, a short
  stub to replace with the project's documentation.
- `package.json` — the project's Node manifest at the top of the repository: written once from a
  stub, then the project's own to change or replace (a starter may bring its own). An update that
  drops node from the languages removes it.
- `.devcontainer/extra-packages.txt` — apt packages, one per line, installed at image build.
- `.devcontainer/extra.sh` — runs as root at the end of the image build.
- `.devcontainer/compose.extra.yaml` — extra compose services next to `main` (a PostgreSQL
  database, an object store), with their volumes and ports. `compose.yaml` pulls it in through
  compose's `include`, so a service written there joins the project's network and is reachable
  from `main` by its service name. The rendered file is a commented-out PostgreSQL example.
- `extra_extensions` in `.copier-answers.yml` — extra VS Code extension ids, comma-separated.
- `extra_dockerignore` in `.copier-answers.yml` — extra `.dockerignore` patterns, comma-separated
  (for example `work/, tmp/`): each becomes its own line of `.dockerignore`, after the template's
  own lines, so those paths stay out of the image build.

`copier update` carries template changes into this project and never overwrites the
project-owned files above; it keeps the two answers and renders them again. To change an answer,
pass it to the update, for example `copier update --trust --data extra_dockerignore='work/, tmp/'`.

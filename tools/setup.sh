set -e

if [ ! -d ".venv" ]; then
  uv python pin python3.11.13
  uv venv
  rm .python-version
fi

uv sync

if ! grep -q 'export PYTHONPATH="$(dirname "$VIRTUAL_ENV")"' .venv/bin/activate; then
  echo 'export PYTHONPATH="$(dirname "$VIRTUAL_ENV")"' >> .venv/bin/activate
fi

. .venv/bin/activate

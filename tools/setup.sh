if [ ! -d ".venv" ]; then
  uv venv
fi

uv sync

if ! grep -q 'export PYTHONPATH="$(dirname "$VIRTUAL_ENV")"' .venv/bin/activate; then
  echo 'export PYTHONPATH="$(dirname "$VIRTUAL_ENV")"' >> .venv/bin/activate
fi

. .venv/bin/activate

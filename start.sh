#!/usr/bin/env bash
set -e

# Find and activate virtualenv
for venv_path in /opt/render/project/src/.venv .venv venv; do
  if [ -f "$venv_path/bin/activate" ]; then
    source "$venv_path/bin/activate"
    break
  fi
done

# Run with Gunicorn or Python
if command -v gunicorn >/dev/null 2>&1; then
  exec gunicorn app:app
elif command -v python3 >/dev/null 2>&1; then
  exec python3 -m gunicorn app:app || exec python3 app.py
else
  exec python app.py
fi

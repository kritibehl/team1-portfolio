#!/bin/bash

set -e

PROJECT_DIR="$HOME/team1-portfolio"
VENV_DIR="$PROJECT_DIR/python3-virtualenv"
SESSION_NAME="portfolio"

tmux kill-server 2>/dev/null || true

cd "$PROJECT_DIR"

git fetch
git reset origin/main --hard

if [ ! -d "$VENV_DIR" ]; then
  python -m venv "$VENV_DIR"
fi

source "$VENV_DIR/bin/activate"
pip install -r requirements.txt

tmux new-session -d -s "$SESSION_NAME" "cd '$PROJECT_DIR' && source '$VENV_DIR/bin/activate' && flask run --host=0.0.0.0"

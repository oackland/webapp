#!/bin/bash

VENV_DIR=".venv"
REQUIREMENTS_FILE="requirements.txt"

if [ -d "$VENV_DIR" ]; then
    source "$VENV_DIR/Scripts/activate"
else
    python3 -m venv "$VENV_DIR"
    source "$VENV_DIR/Scripts/activate"
    python3 -m pip install --upgrade pip
fi

pip install -r "$REQUIREMENTS_FILE"
pip freeze > "$REQUIREMENTS_FILE"

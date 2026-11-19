#!/usr/bin/env bash
set -e

# Move to the script's directory
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"
cd "$DIR"

# Ensure dependencies are satisfied
python3 -m pip install -q -r requirements.txt

# Launch pygame simulation
cd pygame_test
python3 pygame_test.py

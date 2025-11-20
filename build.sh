#!/usr/bin/env bash

set -e
set -o pipefail

echo "Starting to build yelp restaurant predictor..."

if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv .venv
fi

source .venv/bin/activate

echo "Installing dependencies..."
pip install --upgrade pip >/dev/null
pip install -r requirements.txt >/dev/null

echo "Successfully installed dependencies, please wait for Flask to provide URL with open port..."
python app.py
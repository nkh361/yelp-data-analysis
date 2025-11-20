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

echo "Launching web app at http://127.0.0.1:5000"
echo "Press Ctrl+C to stop"
cd yelp_flask_app
python app.py
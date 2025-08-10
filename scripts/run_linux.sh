#!/bin/bash

echo "Activating virtual environment..."

# Go one folder up from the script's location
cd "$(dirname "$0")/.."

# Activate the virtual environment
source venv/bin/activate

echo "Running bot..."

# Run the main Python script
python3 main.py

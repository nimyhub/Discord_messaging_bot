#!/bin/bash

echo "Setting up virtual environment..."

# Create virtual environment folder 'venv' if it does not exist
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

# Activate the virtual environment
source venv/bin/activate

# Upgrade pip and install requirements
pip install --upgrade pip
pip install -r requirements.txt

echo "Setup complete."
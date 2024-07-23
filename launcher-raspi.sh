#/bin/bash
git pull
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 src/rover.py

#/bin/bash
git pull
source .venv/bin/activate
sudo pigpiod
export PIGPIO_ADDR=soft
export PIGPIO_PORT=8888
python3 -m pip install -r requirements.txt
python3 src/rover.py

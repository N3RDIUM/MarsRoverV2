#/bin/bash
git pull
source .venv/bin/activate
export PIGPIO_ADDR=soft
export PIGPIO_PORT=8888
sudo killall pigpiod
sudo pigpiod
python3 -m pip install -r requirements.txt
python3 src/rover.py

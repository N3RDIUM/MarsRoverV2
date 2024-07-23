from gpiozero import Servo
from time import sleep

# For the SG90 servo motor, the pulse width is 1ms to 2ms
correction = 0.45
minpulse = (1.0 - correction) / 1000
maxpulse = (2.0 + correction) / 1000
servo = Servo(16, min_pulse_width=minpulse, max_pulse_width=maxpulse)

try:
   while True:
       servo.value = -1
       sleep(1)
       servo.value = 0
       sleep(1)
       servo.value = 1
       sleep(1)
finally:
   servo.value = 0

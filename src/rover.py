from gpiozero import Servo
from time import sleep

correction = 0.45
minpulse = (1.0 - correction) / 1000
maxpulse = (2.0 + correction) / 1000
servo = Servo(16, min_pulse_width=minpulse, max_pulse_width=maxpulse)

servo.mid()
print("servo mid")
sleep(1)

while True:
  servo.min()
  print("servo min")
  sleep(1)

  servo.mid()
  print("servo mid")
  sleep(1)

  servo.max()
  print("servo max")
  sleep(1)

from gpiozero import AngularServo
from time import sleep

# For the SG90 servo motor, the pulse width is 1ms to 2ms
# correction = 0.45
# minpulse = (1.0 - correction) / 1000
# maxpulse = (2.0 + correction) / 1000
# servo = Servo(16, min_pulse_width=minpulse, max_pulse_width=maxpulse, pin_factory=factory)

from gpiozero import AngularServo
servo = AngularServo(18, min_angle=-42, max_angle=44)

while True:
    servo.min()
    sleep(1)
    servo.mid()
    sleep(1)
    servo.max()
    sleep(1)

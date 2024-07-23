print("Hello World from the Mars Rover V2!")
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT)

# Set up the PWM on pin #16 at 50Hz
pwm = GPIO.PWM(16, 50)
pwm.start(0) # Start the servo with 0 duty cycle ( at 0 deg position )
pwm.ChangeDutyCycle(5) # Tells the servo to turn to the left ( -90 deg position )
sleep(0.5) # Tells the servo to Delay for 5sec
pwm.ChangeDutyCycle(7.5) # Tells the servo to turn to the neutral position ( at 0 deg position )
sleep(0.5) # Tells the servo to Delay for 5sec
pwm.ChangeDutyCycle(10) # Tells the servo to turn to the right ( +90 deg position )
sleep(0.5) # Tells the servo to Delay for 5sec
pwm.stop(0) # Stop the servo with 0 duty cycle ( at 0 deg position )
GPIO.cleanup() # Clean up all the ports we've used.

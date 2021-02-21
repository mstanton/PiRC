# Servo Class
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class Servo():
    def __init__(self,servoPin,pwmValue):
        self.servoPin = servoPin
        self.pwmValue = GPIO.PWM(self.servoPin, 50)

        



# from gpiozero import Servo
# from gpiozero.tools import sin_values

# servo = Servo(17)

# def servoTest():
#     print(servo.pulse_width)
#     servo.source = sin_values()
#     servo.source_delay = 0.1
   
    
# Servo Class
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class Servo():
    def __init__(self, servoPin):
        self.servoPin = servoPin
        GPIO.setup(self.servoPin,GPIO.OUT)
        self.pwm = GPIO.PWM(self.servoPin, 50)
        self.pwm.start(0)

    def updatePosition(self,pwmValue):
        self.pwm.ChangeDutyCycle(pwmValue)
        sleep(0.5)

    def reset(self):
        self.pwm.stop()


# from gpiozero import Servo
# from gpiozero.tools import sin_values

# servo = Servo(17)

# def servoTest():
#     print(servo.pulse_width)
#     servo.source = sin_values()
#     servo.source_delay = 0.1
   
    
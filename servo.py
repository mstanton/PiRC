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
        self.pwm.ChangeDutyCycle(0)
        return pwmValue

    def reset(self):
        self.pwm.stop()

# from gpiozero import Servo
# servo = Servo(17)

# class RCServo():
#     def __init__(self, servoPin):

# def servoTest():
#     print(servo.pulse_width)
#     servo.source = sin_values()
#     servo.source_delay = 0.1
   
    
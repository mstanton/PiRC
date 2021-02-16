import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class Motor():
    def __init__(self,Enable,In1,In2):
        self.Enable = Enable
        self.In1 = In1
        self.In2 = In2
        GPIO.setup(self.Enable,GPIO.OUT)
        GPIO.setup(self.In1,GPIO.OUT)
        GPIO.setup(self.In2,GPIO.OUT)
        self.pwm = GPIO.PWM(self.Enable, 100)
        self.pwm.start(0)

    def forward(self,pwmVal=50,t=0):
        GPIO.output(self.In1,GPIO.HIGH)
        GPIO.output(self.In2,GPIO.LOW)
        self.pwm.ChangeDutyCycle(pwmVal)
        sleep(t)
    
    def reverse(self,pwmVal=50,t=0):
        GPIO.output(self.In1, GPIO.LOW)
        GPIO.output(self.In2, GPIO.HIGH)
        self.pwm.ChangeDutyCycle(pwmVal)
        sleep(t)

    def stop(self,t=0):
        self.pwm.ChangeDutyCycle(0)

motor = Motor(17,22,25)

while True:
    motor.forward(50,2)
    motor.stop(2)
    motor.reverse(50,2)
    motor.stop(2)


from gpiozero import Servo
from gpiozero.tools import sin_values

servo = Servo(17)

def servoTest():
    print(servo.pulse_width)
    servo.source = sin_values()
    servo.source_delay = 0.1
   
    
# RPi RC Adventures - Let's GOOOOOOooooo!
# DATE: 2021-02-11
# DESC: Flask app for controlling an RC car.

from flask import Flask, jsonify, render_template, Response, request
from camera import Camera
from motor import Motor
from servo import Servo
import time
import threading
import os
import datetime
import psutil

app = Flask(__name__, static_folder='static')
app.config['DEBUG'] = True

# SET GPIO PINS FOR L298N H-BRIDGE
motor = Motor(17, 22, 25) 

# SET GPIO PINS FOR STEERING SERVO
servo = Servo(18) 

@app.route("/")
def index():
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    templateData = {
        'title' : "RPi Adventure Time with Python &amp; Flask",
        'time' : timeString
    }

    return render_template('index.html', **templateData)

@app.route("/healthcheck", methods=['GET', 'POST'])
def healthcheck():
    #GET method health checker 
    if request.method == 'GET':
        msg = {'msg':'ya got the message!'}
        return jsonify(msg)

    #POST method health check
    if request.method == 'POST':
        print(request.get_json())
        return 'OK', 200

@app.route("/forward", methods=['POST'])
def forward():
    while True:
        motor.forward(50, 5)

@app.route("/brake", methods=['POST'])
def brake():
    while True:
       motor.stop(2)

@app.route("/steering", methods=['POST'])
def update():
    sPosition = request.form["sPosition"]
    servo.updatePosition(float(sPosition))

@app.route("/pistats")
def pistats():
    CPUStats = {'stats': str(psutil.cpu_stats())} 
    return jsonify(CPUStats)

# CAMERA FEED #
def gen(camera):
    # get camera frame
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(Camera()), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True, threaded=True)



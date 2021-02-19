# RPi RC Adventures - Let's GOOOOOOooooo!
# DATE: 2021-02-11
# DESC: Flask app for controlling an RC car.

from flask import Flask, jsonify, render_template, Response, request
from camera import Camera
from motor import Motor
import time
import threading
import os
import datetime

app = Flask(__name__, static_folder='static')

motorPin1 = 17
motorPin2 = 22
motorPin3 = 25

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

@app.route("/motor/forward", methods=['POST'])
def driveForward():
    Motor(motorPin1, motorPin2, motorPin3)
    while True:
        Motor.forward(50, 5)

@app.route("/motor/brake", methods=['POST'])
def brake():
    Motor(motorPin1, motorPin2, motorPin3)
    while True:
        Motor.stop(2)

        # DRIVE DIRECTION 
# @app.route("/<direction>/<action>")
# def action(direction, action):


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



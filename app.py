# RPi RC Adventures - Let's GOOOOOOooooo!
# DATE: 2021-02-11
# DESC: Flask app for controlling an RC car.

from flask import Flask, render_template, Response, request
from camera import Camera
import time
import threading
import os
import datetime

app = Flask(__name__, static_folder='static')

@app.route("/")
def index():
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    templateData = {
        'title' : "RPi Adventure Time with Python &amp; Flask",
        'time' : timeString
    }
    
    return render_template('index.html', **templateData)

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



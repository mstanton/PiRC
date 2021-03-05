# RPi RC Adventures - Let's GOOOOOOooooo!
# DATE: 2021-02-11
# DESC: Flask app for controlling an RC car.

from flask import Flask, jsonify, render_template, Response, request, make_response
from flask_cors import CORS
from camera import Camera
from motor import Motor
from servo import Servo
import datetime
from gpiozero import LED
from signal import pause

# CONFIG
DEBUG = True

app = Flask(__name__, static_folder='static')
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# SET GPIO PINS FOR L298N H-BRIDGE
motor = Motor(17, 22, 25) 

# SET GPIO PINS FOR STEERING SERVO
servo = Servo(19) 

head_lamps = LED(21)

ground_efx = LED(16)

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
    req = request.get_json()
    tPositionFloat = float(req['tPosition'])
    motor.forward(tPositionFloat, 0)
    res = make_response(jsonify(req), 200)
    return res

@app.route("/brake", methods=['POST'])
def brake():
    motor.stop(0)

@app.route("/steering", methods=['POST'])
def sUpdate():
    req = request.get_json()
    sPositionFloat = float(req['sPosition'])
    servo.updatePosition(sPositionFloat)
    res = make_response(jsonify(req), 200)
    return res

@app.route("/hazard_lamps", methods=['POST'])
def hazardLamps():
    req = request.get_json()
    hazardState = req['hazard']
    if(hazardState == 'true'):
        res = make_response(jsonify(head_lamps.is_active), 200)
        head_lamps.blink();
        pause();
        return res
    else:
        head_lamps.toggle()
        res = make_response(jsonify(head_lamps.is_active), 200)
        return res
        
@app.route("/head_lamps", methods=['POST'])
def headLamps():
    head_lamps.toggle()
    pause()
    res = make_response(jsonify(head_lamps.is_active), 200)
    return res

@app.route("/ground_efx", methods=['POST'])
def groundEFX():
    ground_efx.toggle()
    pause()
    res = make_response(jsonify(ground_efx.is_active), 200)
    return res

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
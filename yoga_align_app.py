from flask import Flask, render_template, Response, jsonify, request
from camera import VideoCamera
import sys
import cv2
import os
from sys import platform
from yoga.general_setup import *
from yoga.images import *
from yoga.joints import *
from yoga.instruction import *
import csv
from yoga.yogaAlignAngle import *


app = Flask(__name__)

video_camera = None
global_frame = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/record_status', methods=['POST'])
def record_status():
    global video_camera 
    if video_camera == None:
        video_camera = VideoCamera()

    json = request.get_json()

    status = json['status']

    if status == "true":
        video_camera.start_record()
        return jsonify(result="started")
    else:
        video_camera.stop_record()
        return jsonify(result="stopped")

def video_stream():
    global video_camera 
    global global_frame

   # time.sleep(5)
   # instruction('a', 4, audio=True)
   # instruction('a', 5, audio=True)

    if video_camera == None:
        video_camera = VideoCamera()
        #video_camera.set(5,0.1)   
    frame = video_camera.get_frame()
    yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
    
    while True:
        frame = video_camera.get_frame()
        frame_decoded = cv2.imdecode(np.fromstring(frame,dtype=np.uint8),cv2.IMREAD_COLOR)
        frame = frame_with_angle(frame_decoded)
        ret, frame = cv2.imencode('.png', frame)
        frame = frame.tobytes()

        if frame != None:
            global_frame = frame
            yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        else:
            yield (b'--frame\r\n'
                            b'Content-Type: image/jpeg\r\n\r\n' + global_frame + b'\r\n\r\n')


@app.route('/video_viewer')
def video_viewer():
    return Response(video_stream(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

    
@app.route("/tolerance", methods=["POST"])
def test():
    name_of_slider = request.form["tolerance"]
    return str(10 *int(name_of_slider))


    
    #@app.route('/image_viewer')
#def image_viewer():
#    return frame#Response(video_stream(),
           #         mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True, port='9185')

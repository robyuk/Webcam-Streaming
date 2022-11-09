#! /usr/bin/env /usr/bin/python3
#
# Gets frames from a webcam using cv2 and streams them using flask
#
#  DOES NOT WORK om repl, because the repl does not have access to a camera.  Pull this from git at https://github.com/robyuk/Webcam-Streaming to a device that has python and a webcam.  Index.html template is included in the Git distribution
#
import cv2
from flask import Flask, render_template, Response

video = cv2.VideoCapture(0)  # Access webcam 0 (may be different number on your system)

# Define a generator (not a function because it does not return a value.  Instead, it )
def get_frames():
  while True:
    success, frame = video.read()
    if success:
      success, encoded_image = cv.imencode('.jpg', frame)
      if success:
        frame = encoded_image.tobytes()
        yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + frame +b'\r\n')

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/video_feed_url')
def video_feed():
  return Response(get_frames, mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=5001)
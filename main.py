from flask import Flask, Response, render_template
import threading
import cv2
from deepface import DeepFace

from utile import generate_frames

app = Flask(__name__)

# Load the reference image
reference_img = cv2.imread("test.jpg")  # Replace with your own image path


lock = threading.Lock()  # Lock for thread-safe access to face_match





@app.route('/')
def index():
    # Render the HTML template for the video feed
    return render_template('index.html')


@app.route('/video_feed')
def video_feed():
    # Return the video feed as a streaming response
    return Response(generate_frames(reference_img,lock), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

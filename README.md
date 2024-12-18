# Live-Face-Recognition-with-flask
This project is a Flask-based web application that performs real-time face verification using a webcam. The application uses the DeepFace library for face recognition and OpenCV for video streaming. It compares live video frames with a reference image and displays whether a match is found.

Features
Real-time video streaming through a web interface.
Face verification using DeepFace.
Responsive and dynamic annotations ("MATCH!" or "NO MATCH!") on the video feed.
Thread-safe implementation for smooth performance.
How to Run
Clone the repository.
Install the required dependencies listed in requirements.txt.
Replace test.jpg with your reference image.
Run the Flask app:
bash
Copy code
python app.py
Open your browser and navigate to http://127.0.0.1:5000/.
Technologies Used
Flask: Web application framework.
OpenCV: For video capture and processing.
DeepFace: Face recognition and verification library.
Use Cases
Real-time identity verification.
Access control systems.
Personalized user experiences.

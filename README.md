# Real-Time Face Verification with Flask and DeepFace

This project is a Flask-based web application that performs real-time face verification using a webcam. The application uses the DeepFace library for face recognition and OpenCV for video streaming. It compares live video frames with a reference image and displays whether a match is found.

## Features
- Real-time video streaming through a web interface.
- Face verification using DeepFace.
- Responsive and dynamic annotations ("MATCH!" or "NO MATCH!") on the video feed.
- Thread-safe implementation for smooth performance.

## How to Run
1. Clone the repository.
2. Install the required dependencies listed in `requirements.txt`:
   ```bash
   pip install -r requirements.txt
3. Replace test.jpg with your reference image.
4. . Run the Flask app:
   ```bash
   python app.py
6.  Open your browser and navigate to http://127.0.0.1:5000/.


## Technologies Used
- Flask: Web application framework.
- OpenCV: For video capture and processing.
- DeepFace: Face recognition and verification library.

## Use Cases
- Real-time identity verification.
- Access control systems.
- Personalized user experiences.

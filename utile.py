import threading

import cv2
from deepface import DeepFace

# Initialize face match status
face_match = False
def check_face(frame ,reference_img , lock):
    global face_match
    try:
        result = DeepFace.verify(frame, reference_img.copy())
        with lock:
            face_match = result['verified']
    except Exception as e:
        print(f"Error during face verification: {e}")
        with lock:
            face_match = False


def generate_frames(reference_img,lock):
    cap = cv2.VideoCapture(0)  # Use the default camera
    counter = 0

    if not cap.isOpened():
        raise RuntimeError("Error: Could not open video capture.")

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        if counter % 30 == 0:
            # Run face verification in a separate thread
            threading.Thread(target=check_face, args=(frame.copy(),reference_img,lock)).start()

        counter += 1

        with lock:
            if face_match:
                cv2.putText(frame, "MATCH!", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
            else:
                cv2.putText(frame, "NO MATCH!", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

        # Encode the frame as JPEG
        _, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

    cap.release()
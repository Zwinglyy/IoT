from flask import Flask, render_template, Response, request, jsonify, send_from_directory
import cv2
import face_recognition
import os
from datetime import datetime

app = Flask(__name__)
camera = cv2.VideoCapture(0)

# Variabel global
face_detection_active = False
known_encodings = []
face_log = []
SAVE_DIR = "faces"
os.makedirs(SAVE_DIR, exist_ok=True)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/toggle_detection', methods=['POST'])
def toggle_detection():
    global face_detection_active
    face_detection_active = not face_detection_active
    return {'status': face_detection_active}

@app.route('/history')
def history():
    return jsonify(face_log)

@app.route('/face_image/<filename>')
def face_image(filename):
    return send_from_directory(SAVE_DIR, filename)

def gen_frames():
    global face_detection_active, known_encodings, face_log
    frame_count = 0

    while True:
        success, frame = camera.read()
        if not success:
            break

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_count += 1

        if face_detection_active and frame_count % 10 == 0:
            face_locations = face_recognition.face_locations(rgb_frame)
            face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

            for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
                matches = face_recognition.compare_faces(known_encodings, face_encoding, tolerance=0.5)
                if not any(matches):
                    known_encodings.append(face_encoding)

                    # Simpan gambar wajah
                    face_image = frame[top:bottom, left:right]
                    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                    filename = f"face_{timestamp}.jpg"
                    filepath = os.path.join(SAVE_DIR, filename)
                    cv2.imwrite(filepath, face_image)

                    face_log.append({
                        'time': timestamp,
                        'filename': filename
                    })

                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

        # Encode dan kirim frame
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
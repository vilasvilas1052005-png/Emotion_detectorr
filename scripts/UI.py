from flask import Flask, render_template, Response, jsonify
import cv2
import time
import numpy as np

app = Flask(__name__)
shared_data = None  # global reference to shared_data or detector passed from main


def set_shared_data(data):
    global shared_data
    shared_data = data


def gen_frames():
    blank_frame = np.zeros((480, 640, 3), dtype=np.uint8)  # black image
    last_frame_time = time.time()

    while True:
        frame = None
        # Try to get the latest frame if available
        if shared_data is not None:
            frame = shared_data.get("frame", None)

        if frame is None:
            # If no frame available for more than 1 second, yield a blank frame once
            if time.time() - last_frame_time > 1:
                ret, buffer = cv2.imencode(".jpg", blank_frame)
                if not ret:
                    continue
                frame_bytes = buffer.tobytes()
                yield (
                    b"--frame\r\nContent-Type: image/jpeg\r\n\r\n"
                    + frame_bytes
                    + b"\r\n"
                )
                last_frame_time = time.time()
            else:
                # No delay here, just try again quickly
                time.sleep(0.01)
            continue

        # Frame available, encode immediately without delay
        ret, buffer = cv2.imencode(".jpg", frame)
        if not ret:
            # Encoding failed, try again quickly
            time.sleep(0.01)
            continue

        frame_bytes = buffer.tobytes()
        yield b"--frame\r\nContent-Type: image/jpeg\r\n\r\n" + frame_bytes + b"\r\n"
        last_frame_time = time.time()
        # No explicit sleep here to allow max speed streaming


@app.route("/video_feed")
def video_feed():
    return Response(gen_frames(), mimetype="multipart/x-mixed-replace; boundary=frame")


@app.route("/current_emotion")
def current_emotion():
    try:
        if shared_data is None:
            emotion = "neutral"
        else:
            emotion = shared_data.get("emotion", "neutral")
        return jsonify([emotion]), 200
    except Exception as e:
        return jsonify(["error", str(e)]), 500


@app.route("/")
@app.route("/home", methods=["GET", "POST"])
def emotion_detection():
    current_emotion = (
        shared_data.get("emotion", "neutral") if shared_data else "neutral"
    )
    # Render template without passing song; the JS updates it dynamically
    return render_template("index.html", emotion=current_emotion)

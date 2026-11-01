import cv2
from fer import FER
import time 


def emotion_detection_process(shared_data, logger, camera_index=0, use_mtcnn=False):
    detector = FER(mtcnn=use_mtcnn)
    cap = cv2.VideoCapture(camera_index)
    if not cap.isOpened():
        logger.critical("Error: Cannot open camera.")
        return

    stable_emotion = "Neutral"
    last_update_time = time.time()
    stability_threshold = 1.5  # seconds to wait before updating emotion

    while True:
        ret, frame = cap.read()
        if not ret:
            logger.critical("Failed to grab frame.")
            break

        frame = cv2.flip(frame, 1)
        results = detector.detect_emotions(frame)
        current_time = time.time()

        if results:
            emotions = results[0]["emotions"]
            top_emotion = max(emotions, key=emotions.get).capitalize()
        else:
            top_emotion = "No Face"

        # Update emotion only if stable for threshold duration
        if top_emotion == stable_emotion:
            last_update_time = current_time  # reset timer on stability
        else:
            if (current_time - last_update_time) > stability_threshold:
                stable_emotion = top_emotion
                last_update_time = current_time

        # Update shared emotion after stability check
        shared_data["emotion"] = stable_emotion

        # Optionally draw bounding box and label on the frame
        if results:
            for face in results:
                (x, y, w, h) = face["box"]
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                cv2.putText(
                    frame,
                    top_emotion,
                    (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.9,
                    (0, 255, 0),
                    2,
                    cv2.LINE_AA,
                )

        # Always update the frame in shared data for smooth video feed
        shared_data["frame"] = frame

        time.sleep(0.024)  # keep frame grab roughly 24 fps

    cap.release()

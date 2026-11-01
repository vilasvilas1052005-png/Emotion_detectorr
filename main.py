from scripts.UI import app, set_shared_data
from multiprocessing import Process, Manager, set_start_method
from scripts.log import logger
from scripts.detectionModel import emotion_detection_process


def main():
    manager = Manager()
    shared_data = manager.dict()
    shared_data["frame"] = None
    shared_data["emotion"] = "Neutral"

    emotion_proc = Process(target=emotion_detection_process, args=(shared_data, logger))
    emotion_proc.start()

    # Pass shared_data to Flask app for live emotion reading
    set_shared_data(shared_data)

    try:
        # Disable Flask reloader in multiprocessing
        app.run(debug=False, use_reloader=False)
    finally:
        emotion_proc.terminate()
        emotion_proc.join()


if __name__ == "__main__":
    set_start_method("spawn")
    main()

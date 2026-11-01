# Emotion Detector (MoodVision)

A real-time facial emotion detection web app. It reads your webcam, detects faces, classifies the dominant emotion, and shows the live video feed with the detected emotion in the browser.

## Features

- Real-time emotion detection from webcam video using the **FER** library (pre-trained deep learning model) and **OpenCV**
- Face detection with bounding boxes and emotion labels drawn on the video
- **Stability filter:** the displayed emotion changes only after a new emotion persists for 1.5 seconds, so the label does not flicker
- **Flask** web interface that streams the video and updates the emotion label live
- Detection runs in a separate process (multiprocessing) so the web UI stays responsive
- SQLite helper scripts for an emotion-to-song database (included as utilities)

## Tech Stack

Python 3.12, Flask, OpenCV, FER, TensorFlow, NumPy, SQLite, Tailwind CSS

## Project Structure

```
main.py                      Starts the detector process and the Flask server
scripts/detectionModel.py    Webcam capture and emotion detection loop
scripts/UI.py                Flask routes (video feed, live emotion, home page)
scripts/templates/           HTML page
scripts/static/              Tailwind CSS files
scripts/setup.py             Creates the SQLite database tables
scripts/push-to-db.py        Loads emotion/song data into SQLite
scripts/load_music.py        Reads songs from SQLite
```

## Getting Started

**Prerequisites:** Python 3.12, a working webcam, and [uv](https://docs.astral.sh/uv/) (or pip).

```bash
git clone https://github.com/vilasvilas1052005-png/Emotion_detectorr.git
cd Emotion_detectorr
uv sync
uv run main.py
```

Then open http://127.0.0.1:5000 in your browser and allow camera access.

## How It Works

1. OpenCV captures frames from the webcam.
2. FER detects faces and scores emotions (happy, sad, angry, surprise, fear, disgust, neutral).
3. The highest-scoring emotion is passed through the stability filter.
4. Flask streams the annotated video and serves the current emotion to the page, which refreshes every 300 ms.

## Author

**Vilas N** — Information Science Engineering student, Malnad College of Engineering, Hassan.
GitHub: [vilasvilas1052005-png](https://github.com/vilasvilas1052005-png)

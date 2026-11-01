# sharedEmotionDetector.py
class SharedEmotionDetector:
    def __init__(self, shared_data):
        self.shared_data = shared_data
        self.running = True

    @property
    def frame(self):
        return self.shared_data.get("frame", None)

    @property
    def current_emotion(self):
        return self.shared_data.get("emotion", "Neutral")

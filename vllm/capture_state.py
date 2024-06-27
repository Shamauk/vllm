# vllm/capture_state.py

class CaptureState:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CaptureState, cls).__new__(cls)
            cls._instance.is_capturing = False
        return cls._instance

    def start_capture(self):
        self.is_capturing = True

    def end_capture(self):
        self.is_capturing = False

    def is_capturing(self):
        return self.is_capturing

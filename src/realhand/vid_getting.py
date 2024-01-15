import cv2

class Video():
    capture_id = 0
    width = 900
    height = 600
    cap = None

    def __init__(self, capture_id = 0, width = 900, height = 600):
        self.capture_id = capture_id
        self.width = width
        self.height = height

        self.cap = cv2.VideoCapture(0)

    def get_video_frame(self):
        success, img = self.cap.read()
        if success:
            img = cv2.flip(img, 1)
            return img
        else:
            return None

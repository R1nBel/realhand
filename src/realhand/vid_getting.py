import cv2

class Video():
    """
    ВИДЕО С КАМЕРЫ УСТРОЙСТВА
    """
    capture_id = 0
    """
    ИНДЕКС КАМЕРЫ
    """
    width = 900
    """
    ШИРИНА ВИДЕО
    """
    height = 600
    """
    ВЫСОТА ВИДЕО
    """
    cap = None
    """
    ОБЪЕКТ КАМЕРЫ
    """

    def __init__(self, capture_id = 0, width = 900, height = 600):
        self.capture_id = capture_id
        self.width = width
        self.height = height

        self.cap = cv2.VideoCapture(0)

    def get_video_frame(self):
        """
        ЗАХВАТ ВИДЕО И ВОЗВРАТ КАДРА
        """
        success, img = self.cap.read()
        if success:
            img = cv2.flip(img, 1)
            return img
        else:
            return None

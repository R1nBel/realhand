import cv2

class Video():
    """
    ВИДЕО С КАМЕРЫ УСТРОЙСТВА
    """
    __capture_id = 0
    """
    [int]: ИНДЕКС КАМЕРЫ
    """
    __cap = None
    """
    ОБЪЕКТ КАМЕРЫ
    """

    def __init__(self, capture_id = 0):
        self.__capture_id = capture_id

        self.__cap = cv2.VideoCapture(self.__capture_id)

    def getVideoFrame(self):
        """
        ЗАХВАТ ВИДЕО И ВОЗВРАТ КАДРА
        """
        success, img = self.__cap.read()
        if success:
            img = cv2.flip(img, 1)
            return img
        else:
            return None

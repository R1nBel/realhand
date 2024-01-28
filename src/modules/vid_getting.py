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

    def __init__(self, captureId = 0):
        self.__captureId = captureId

        self.__cap = cv2.VideoCapture(self.__captureId)

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

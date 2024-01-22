import cv2
import time
class DisplayWindow():
    """
    ОТОБРАЖЕНИЕ ВИДЕОПОТОКА
    """
    show_FPS = False
    """
    [bool]: ФЛАГ ОТОБРАЖЕНИЯ FPS
    """

    __pTime = 0
    __cTime = 0

    def __init__(self, show_FPS=False):
        self.show_FPS = show_FPS

    def __detectFps(self):
        """
        ПОДСЧЕТ FPS
        """

        self.__cTime = time.time()
        self.fps = 1. / (self.__cTime - self.__pTime)
        self.__pTime = self.__cTime

    def showWindow(self, img):
        """
        ОТОБРАЖЕНИЕ ОКНА
        """
        if self.show_FPS:
            self.__detectFps()
            cv2.putText(img, str(int(self.fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)

        # cv2.imshow("Image", img)
        cv2.waitKey(1)

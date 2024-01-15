import cv2
import time 
class DisplayWindow():
    show_FPS = False
    pTime = 0
    cTime = 0

    def __init__(self, show_FPS=False):
        self.show_FPS = show_FPS

    def __detect_fps(self):
        self.cTime = time.time()
        self.fps = 1. / (self.cTime - self.pTime)
        self.pTime = self.cTime

    def show_window(self, img):
        if self.show_FPS:
            self.__detect_fps()
            cv2.putText(img, str(int(self.fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)

        cv2.imshow("Image", img)
        cv2.waitKey(1)
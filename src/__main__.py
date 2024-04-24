from modules.vid_getting import Video
from modules.hand_detecting import HandDetector
from modules.gui_interface import Display

def main():
    """
    ТОЧКА ВХОДА
    СБОРКА КАДРОВ В ВИДЕО
    """
    height = 600
    width = 900

    video = Video()
    detector = HandDetector(maxHands=1, detectionCon=0.8)
    modelWindow = Display(width = width, height = height)


    while True:
        img = video.getVideoFrame()
        img = detector.findHands(img)

        points = detector.findPosition(img)
        modelWindow.showVideoFrame(img, True)

        if detector.handExist:
            modelWindow.drowHand(points)
            detector.handExist = False

        if not modelWindow.windowEndStatus():
            exit()

if __name__ == "__main__":
    main()

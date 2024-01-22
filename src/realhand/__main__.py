from vid_getting import Video
from hand_detecting import HandDetector
from display import DisplayWindow
from gui_interface import ModelWindow

def main():
    """
    ТОЧКА ВХОДА
    СБОРКА КАДРОВ В ВИДЕО
    """
    height = 600
    width = 900

    video = Video()
    detector = HandDetector(maxHands=1, detectionCon=0.8)
    cameraWindow = DisplayWindow(show_FPS = True)
    modelWindow = ModelWindow(width = width, height = height)


    while True:
        img = video.getVideoFrame()
        img = detector.findHands(img)

        points = detector.findPosition(img)
        cameraWindow.showWindow(img)
        modelWindow.showVideoFrame(img)

        if detector.handExist:
            modelWindow.drowHand(points)
            detector.handExist = False

        if not modelWindow.windowEndStatus():
            exit()

if __name__ == "__main__":
    main()

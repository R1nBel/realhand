from vid_getting import Video
from hand_detecting import handDetector
from display import DisplayWindow
from model_drawing import ModelWindow

def main():
    """
    ТОЧКА ВХОДА
    СБОРКА КАДРОВ В ВИДЕО
    """
    height = 600
    width = 900

    video = Video()
    detector = handDetector(maxHands=1, detectionCon=0.8)
    cameraWindow = DisplayWindow(show_FPS = True)
    modelWindow = ModelWindow(width = width, height = height)

    while True:
        img = video.get_video_frame()
        img = detector.findHands(img)

        points = detector.findPosition(img)
        cameraWindow.show_window(img)
        modelWindow.display_frame()

        if detector.handExist:
            modelWindow.drow_hand(points=points)
            detector.handExist = False


if __name__ == "__main__":
    main()

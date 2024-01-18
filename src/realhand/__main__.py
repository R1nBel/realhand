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

    video = Video(height = height, width = width)
    detector = handDetector(maxHands=1, detectionCon=0.8)
    camera_window = DisplayWindow(show_FPS = True)
    model_window = ModelWindow(width = width, height = height)


    while True:
        img = video.get_video_frame()
        img = detector.findHands(img)

        points = detector.findPosition(img)

        camera_window.show_window(img)
        model_window.display_frame()
        if points.hand_exist:
            model_window.drow_hand(points=points)


if __name__ == "__main__":
    main()

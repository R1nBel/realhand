import time
from vid_getting import Video
from hand_detecting import handDetector
from display import DisplayWindow

def main():
    height = 600
    width = 900

    video = Video(height = height, width = width)
    detector = handDetector(maxHands=1, detectionCon=0.8)
    window = DisplayWindow(show_FPS = True)

    while True:
        img = video.get_video_frame()
        img = detector.findHands(img)

        lmList = detector.findPosition(img)
        
        data = []
        
        if len(lmList) != 0:
            for l in lmList:
                data.extend([l[0], height - l[1], l[2]])

        window.show_window(img)

if __name__ == "__main__":  
    main()
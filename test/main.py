import cv2
import time
from hand_tracking import handDetector

pTime = 0
cTime = 0
cap = cv2.VideoCapture(0)
w, h = 900, 600
cap.set(3, w)
cap.set(4, h)

detector = handDetector(maxHands=1, detectionCon=0.8)

while True:
	success, img = cap.read()
	img = detector.findHands(img)
	lmList = detector.findPosition(img)

	data = []

	if len(lmList) != 0:
		for l in lmList:
			data.extend([l[0], h - l[1], l[2]])

	cTime = time.time()
	fps = 1. / (cTime - pTime)
	pTime = cTime

	img = cv2.flip(img, 1)

	#cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)

	cv2.imshow("Image", img)
	cv2.waitKey(1)

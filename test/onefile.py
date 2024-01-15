import cv2
import time
import mediapipe as mp
import math

class handDetector():
	def __init__(self, mode=False, maxHands=1, modelComplexity=1, detectionCon=0.5, trackCon=0.5):
		self.mode = mode
		self.maxHands = maxHands
		self.modelComplexity = modelComplexity
		self.detectionCon = detectionCon
		self.trackCon = trackCon

		self.mpHands = mp.solutions.hands
		self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.modelComplexity, self.detectionCon, self.trackCon)
		self.mpDraw = mp.solutions.drawing_utils
		self.tipIds = [4, 8, 12, 16, 20] 

	def findHands(self, img, draw=True):
		imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
		self.results = self.hands.process(imgRGB)

		if self.results.multi_hand_landmarks:
			for handLms in self.results.multi_hand_landmarks:
				if draw:
					self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
		return img

	def findPosition(self, img, handNo=0, draw=True):
		xList = []
		yList = []
		bbox = []
		self.lmList = []
		
		if self.results.multi_hand_landmarks:
			myHand = self.results.multi_hand_landmarks[handNo]
			for id, lm in enumerate(myHand.landmark):
				h, w, c = img.shape
				cx, cy = int(lm.x*w), int(lm.y*h)
				xList.append(cx)
				yList.append(cy)
				self.lmList.append([id, cx, cy])
				if draw:
					cv2.circle(img, (cx, cy), 5, (255,0,255), cv2.FILLED)
			xmin, xmax = min(xList), max(xList)
			ymin, ymax = min(yList), max(yList)
			bbox = xmin, ymin, xmax, ymax

			if draw:
				cv2.rectangle(img, (bbox[0]-20, bbox[1]-20), (bbox[2]+20, bbox[3]+20), (0, 255, 0), 2)
		return self.lmList




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

	# cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)

	cv2.imshow("Image", img)
	cv2.waitKey(1)

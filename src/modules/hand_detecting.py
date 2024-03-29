import cv2
import mediapipe as mp

class HandDetector():
	"""
	РАСПОЗНАВАНИЕ РУКИ НА ИЗОБРАЖЕНИИ
	"""

	handExist = False
	"""
	[bool]: НАЛИЧИЕ РУКИ В КАДРЕ
	"""

	def __init__(self, mode=False, maxHands=1, modelComplexity=1, detectionCon=0.5, trackCon=0.5):
		self.__mode = mode
		self.__maxHands = maxHands
		self.__modelComplexity = modelComplexity
		self.__detectionCon = detectionCon
		self.__trackCon = trackCon

		self.__mpHands = mp.solutions.hands
		self.__hands = self.__mpHands.Hands(self.__mode, self.__maxHands, self.__modelComplexity, self.__detectionCon, self.__trackCon)
		self.__mpDraw = mp.solutions.drawing_utils


	def findHands(self, img, draw=True):
		"""
    	ПОИСК РУК НА ИЗОБРАЖЕНИИ
    	"""

		imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
		self.__results = self.__hands.process(imgRGB)

		if self.__results.multi_hand_landmarks:
			for handLms in self.__results.multi_hand_landmarks:
				if draw:
					self.__mpDraw.draw_landmarks(img, handLms, self.__mpHands.HAND_CONNECTIONS)
		return img

	def findPosition(self, img, handNo=0, draw=True):
		"""
		РАСПОЗНОВАНИЕ РУКИ И ЕЕ СОСТАВЛЯЮЩИХ
		"""

		xList = []
		yList = []
		zList = []
		bbox = []
		self.__lmList = []

		if self.__results.multi_hand_landmarks:
			myHand = self.__results.multi_hand_landmarks[handNo]
			self.handExist = True
			for id, lm in enumerate(myHand.landmark):
				h, w, c = img.shape
				cx, cy, cz = int(lm.x*w), int(lm.y*h), lm.z*c
				xList.append(cx)
				yList.append(cy)
				zList.append(cz)
				self.__lmList.append([cx*0.03, cy*(-0.03), cz])
				if draw:
					cv2.circle(img, (cx, cy), 5, (255,0,255), cv2.FILLED)
			xmin, xmax = min(xList), max(xList)
			ymin, ymax = min(yList), max(yList)
			bbox = xmin, ymin, xmax, ymax

			if draw:
				cv2.rectangle(img, (bbox[0]-20, bbox[1]-20), (bbox[2]+20, bbox[3]+20), (0, 255, 0), 2)
		return self.__lmList

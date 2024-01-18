import cv2
import mediapipe as mp
from mediapipe import solutions
from mediapipe.framework.formats import landmark_pb2

class handDetector():
	"""
	РАСПОЗНАВАНИЕ РУКИ НА ИЗОБРАЖЕНИИ
	"""
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
		"""
    	ПОИСК РУК НА ИЗОБРАЖЕНИИ
    	"""
		imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
		self.results = self.hands.process(imgRGB)

		if self.results.multi_hand_landmarks:
			for handLms in self.results.multi_hand_landmarks:
				if draw:
					self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
		return img

	def findPosition(self, img, handNo=0, draw=True):
		"""
		РАСПОЗНОВАНИЕ РУКИ И ЕЕ СОСТАВЛЯЮЩИХ
		"""
		xList = []
		yList = []
		zList = []
		bbox = []
		self.lmList = []
		self.points = Points()

		if self.results.multi_hand_landmarks:
			myHand = self.results.multi_hand_landmarks[handNo]
			for id, lm in enumerate(myHand.landmark):
				h, w, c = img.shape
				cx, cy, cz = int(lm.x*w), int(lm.y*h), lm.z*c
				xList.append(cx)
				yList.append(cy)
				zList.append(cz)
				self.lmList.append([id, cx, cy, cz])
				if draw:
					cv2.circle(img, (cx, cy), 5, (255,0,255), cv2.FILLED)
			xmin, xmax = min(xList), max(xList)
			ymin, ymax = min(yList), max(yList)
			bbox = xmin, ymin, xmax, ymax

			self.points.attach_points(self.lmList)
			self.points.hand_exist = True

			if draw:
				cv2.rectangle(img, (bbox[0]-20, bbox[1]-20), (bbox[2]+20, bbox[3]+20), (0, 255, 0), 2)
		return self.points

class Points():
	hand_exist = False
	finger_1 = []
	finger_2 = []
	finger_3 = []
	finger_4 = []
	finger_5 =[]
	palm = []

	def __init__(self):
		pass

	def attach_points(self, points):
		self.palm = points[0], points[5], points[9], points[13], points[17]
		self.finger_1 = points[1:5]
		self.finger_2 = points[5:9]
		self.finger_3 = points[9:13]
		self.finger_4 = points[13:17]
		self.finger_5 = points[17:]

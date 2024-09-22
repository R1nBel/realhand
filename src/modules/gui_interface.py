from OpenGL.GL import *
from OpenGL.GLU import *
from PyQt5 import QtWidgets as QtW, QtGui as QtG, QtCore as QtC
import sys
import cv2
import time

class Display():
    """
    ВЫЗОВ ОКНА ОТОБРАЖЕНИЯ МОДЕЛИ
    """

    def __init__(self, width = 900, height = 600):
        self.__width = width
        self.__height = height

        self.__app = QtW.QApplication(sys.argv)
        self.__window = DisplayWindow()
        self.__window.setGeometry(0, 0, int(self.__width), self.__height)
        self.__window.addModelWidget()
        self.__window.addVideoCaptureWidget()

        self.__window.setWindowTitle('REALHAND')
        self.__window.show()

    def drowHand(self, points = None):
        """
        ОБНОВЛЕНИЕ ПОЗИЦИИ РУКИ
        """

        self.__window.gl_widget.updatePos(points)

    def showVideoFrame(self, img, fps):
        """
        ОТОБРАЖЕНИЕ КАДРА ВИДЕОПОТОКА
        """

        self.__window.video_widget.updateFrame(img, fps)

    def windowEndStatus(self):
        """
        ПРОВЕРКА ЗАКРЫТИЯ ОКНА
        """

        return self.__window.status


class Hand():
    """
    ТОЧКИ РУКИ И ИХ СОЕДИНЕНИЯ. ВЫВОД МОДЕЛИ НА ЭКРАН
    """

    __verticies = None
    """
    [arr[arr[int]]]: ТОЧКИ РУКИ
    """

    __edges = [
        [0, 1], [1, 2], [2, 3], # ПЕРВЫЙ ПАЛЕЦ
        [0, 5], [5, 6], [6, 7], [7, 8], # ВТОРОЙ ПАЛЕЦ
        [0, 9], [9, 10], [10, 11], [11, 12], # ТРЕТИЙ ПАЛЕЦ
        [0, 13], [13, 14], [14, 15], [15, 16], # ЧЕТВЕРТЫЙ ПАЛЕЦ
        [0, 17], [17, 18], [18, 19], [19, 20], # ПЯТЫЙ ПАЛЕЦ
        [5, 9], [9, 13], [13, 17] # ЛАДОНЬ

        ]
    """
    [arr[arr[int]]]: СОЕДИНЕНИЯ ТОЧЕК РУКИ
    """

    def __init__(self, points):
        self.__verticies = points

    def draw(self):
        """
        ВЫВОД МОДЕЛИ НА ЭКРАН
        """

        glBegin(GL_LINES)
        for edge in self.__edges:
            for vertex in edge:
                glVertex3fv(self.__verticies[vertex])
        glEnd()


class OpenGLWidget(QtW.QOpenGLWidget):
    """
    ОКНО 3D ГРАФИКИ OPENGL
    """

    __points = [[0, 0, 0] for _ in range(21)]
    """
    [arr[arr[int]]]: КЛЮЧЕВЫЕ ТОЧКИ РУКИ
    """

    def __init__(self, parent=None):
        super(OpenGLWidget, self).__init__(parent)

    def initializeGL(self):
        """
        ИНИЦИАЛИЗАЦИЯ ОКНА
        """

        glClearColor(0.0, 0.0, 0.0, 1.0)

    def resizeGL(self, w, h):
        """
        ФОРМИРОВАНИЕ ОКНА
        """

        glViewport(0, 0, w, h)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(90, w/h, 1, 100)

    def paintGL(self):
        """
        ОТРИСОВКА ОКНА
        """

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glLineWidth(3)
        glTranslatef(-10, 8, -8)

        self.hand = Hand(self.__points)
        self.hand.draw()

    def updatePos(self, points):
        """
        ИЗМЕНЕНИЕ ПОЗИЦИИ МОДЕЛИ
        """

        self.__points = points
        self.update()


class FrameWidget(QtW.QWidget):
    __pTime = 0
    __cTime = 0

    def __init__(self):
        super(FrameWidget, self).__init__()

        self.image_label = QtW.QLabel(self)
        self.image_label.setAlignment(QtC.Qt.AlignCenter)

    def updateFrame(self, frame, showFPS):
        """
        ОБНОВЛЕНИЕ КАДРА ВИДЕОПОТОКА
        """

        if showFPS:
            self.__detectFps()
            cv2.putText(frame, str(int(self.fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)
        h, w, ch = frame.shape
        bytes_per_line = ch * w
        q_image = QtG.QImage(frame.data, w, h, bytes_per_line, QtG.QImage.Format_BGR888)
        pixmap = QtG.QPixmap.fromImage(q_image)
        self.image_label.setPixmap(pixmap)

        cv2.waitKey(1)

    def __detectFps(self):
        """
        ПОДСЧЕТ FPS
        """

        self.__cTime = time.time()
        self.fps = 1. / (self.__cTime - self.__pTime)
        self.__pTime = self.__cTime


class DisplayWindow(QtW.QMainWindow):
    """
    ОСНОВНОЕ ОКНО ИНТЕРФЕЙСА
    """


    status = True
    """
    [bool]: СОСТОЯНИЕ ОКНА\n
    True = ОКНО ЗАПУЩЕНО\n
    False ОКНО ЗАКРЫТО=
    """

    def __init__(self):

        super(DisplayWindow, self).__init__()
        self.__central_widget = QtW.QWidget(self)
        self.setCentralWidget(self.__central_widget)
        self.__layout = QtW.QHBoxLayout(self.__central_widget)

    def addModelWidget(self):
        """
        ДОБАВЛЕНИЕ ВИДЖЕТА ОТРИСОВКИ
        """

        self.gl_widget = OpenGLWidget()
        self.__layout.addWidget(self.gl_widget)
        self.gl_widget.setFixedSize(600, 600)

    def addVideoCaptureWidget(self):
        """
        ДОБАВЛЕНИЕ ВИДЖЕТА ОТОБРАЖЕНИЯ ВИДЕО
        """

        self.video_widget = FrameWidget()
        self.__layout.addWidget(self.video_widget)
        self.__layout.addWidget(self.video_widget.image_label)

    def closeEvent(self, event):
        """
        СОБЫТИЕ ЗАКРЫТИЯ ОКНА
        """

        self.status = False

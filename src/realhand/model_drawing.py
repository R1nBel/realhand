from OpenGL.GL import *
from OpenGL.GLU import *
from PyQt5 import QtWidgets as QtW
import sys

class ModelWindow():
    """
    ВЫЗОВ ОКНА ОТОБРАЖЕНИЯ МОДЕЛИ
    """
    __width = 900
    """
    [int]: ШИРИНА ОКНА
    """
    __height = 600
    """
    [int]: ВЫСОТАА ОКНА
    """

    def __init__(self, width = 900, height = 600):
        self.__width = width
        self.__height = height

        self.__app = QtW.QApplication(sys.argv)
        self.__window = MainWindow()
        self.__window.setGeometry(0, 0, self.__width, self.__height)
        self.__window.gl_widget.setGeometry(0, 0, self.__width, self.__height)
        self.__window.setWindowTitle('OpenGL Animation with PyQt')
        self.__window.show()

    def drowHand(self, points = None):
        """
        ОТРИСОВКА РУКИ
        """
        self.__window.gl_widget.updatePos(points)

    def windowEndStatus(self):
        """
        ПРОВЕРКА ЗАКРЫТИЯ ОКНА
        """
        if not self.__window.status:
            sys.exit(self.__app.exec_())


class Hand():
    """
    ТОЧКИ РУКИ И ИХ СОЕДИНЕНИЯ. ВЫВОД МОДЕЛИ НА ЭКРАН
    """

    verticies = None
    """
    [arr[arr[int]]]: ТОЧКИ РУКИ
    """

    edges = [
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
        self.verticies = points

    def draw(self):
        """
        ВЫВОД МОДЕЛИ НА ЭКРАН
        """
        glBegin(GL_LINES)
        for edge in self.edges:
            for vertex in edge:
                glVertex3fv(self.verticies[vertex])
        glEnd()


class OpenGLWidget(QtW.QOpenGLWidget):
    """
    ОКНО 3D ГРАФИКИ OPENGL
    """
    __points = [[0, 0, 0]]*21
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
        glTranslatef(0.0,0.0, -10)

        self.hand = Hand(self.__points)
        self.hand.draw()

    def updatePos(self, points):
        """
        ИЗМЕНЕНИЕ ПОЗИЦИИ МОДЕЛИ
        """
        self.__points = points
        self.update()


class MainWindow(QtW.QMainWindow):
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
        super(MainWindow, self).__init__()

        self.central_widget = QtW.QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QtW.QVBoxLayout(self.central_widget)

        self.gl_widget = OpenGLWidget()
        self.layout.addWidget(self.gl_widget)

    def closeEvent(self, event):
        """
        СОБЫТИЕ ЗАКРЫТИЯ ОКНА
        """
        self.status = False

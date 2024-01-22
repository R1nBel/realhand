from OpenGL.GL import *
from OpenGL.GLU import *
from PyQt5 import QtWidgets as qWidget
from PyQt5 import QtGui as qGui
from PyQt5 import QtCore as qCore
from PyQt5 import uic
import sys
import os

verticies = [[9.81, -6.72, 1.7044575884028745e-06], [8.549999999999999, -6.8999999999999995, -0.09511209279298782], [7.35, -6.359999999999999, -0.15266158059239388], [6.359999999999999, -5.91, -0.20099752396345139], [5.3999999999999995, -5.819999999999999, -0.25162332504987717], [7.56, -4.2, -0.10762374848127365], [6.779999999999999, -3.06, -0.17613305523991585], [6.27, -2.28, -0.23339322209358215], [5.819999999999999, -1.6199999999999999, -0.2789929434657097], [8.25, -3.81, -0.12039099633693695], [7.739999999999999, -2.37, -0.18177266791462898], [7.35, -1.47, -0.23731794208288193], [7.02, -0.69, -0.27865681797266006], [9.06, -3.75, -0.14368122071027756], [8.67, -2.31, -0.21862062066793442], [8.34, -1.41, -0.27202796190977097], [8.01, -0.6, -0.30906756967306137], [9.9, -3.9899999999999998, -0.17344770580530167], [9.99, -2.88, -0.2517666667699814], [9.959999999999999, -2.13, -0.2881210148334503], [9.9, -1.41, -0.31082410365343094]]

edges = [
        [0, 1], [1, 2], [2, 3], # ПЕРВЫЙ ПАЛЕЦ
        [0, 5], [5, 6], [6, 7], [7, 8], # ВТОРОЙ ПАЛЕЦ
        [0, 9], [9, 10], [10, 11], [11, 12], # ТРЕТИЙ ПАЛЕЦ
        [0, 13], [13, 14], [14, 15], [15, 16], # ЧЕТВЕРТЫЙ ПАЛЕЦ
        [0, 17], [17, 18], [18, 19], [19, 20], # ПЯТЫЙ ПАЛЕЦ
        [5, 9], [9, 13], [13, 17] # ЛАДОНЬ

        ]

def Cube():
    glLineWidth(3)
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()


class mainWindow(qWidget.QMainWindow):
    """Main window class."""

    def __init__(self, *args):
        """Init."""
        super(mainWindow, self).__init__(*args)
        ui = os.path.join('test/test.ui')
        uic.loadUi(ui, self)

    def setupUI(self):
        print("\033[1;101m SETU6P UI \033[0m")
        self.windowsHeight = self.openGLWidget.height()
        self.windowsWidth = self.openGLWidget.width()

        self.openGLWidget.initializeGL()
        self.openGLWidget.resizeGL(self.windowsWidth, self.windowsHeight)
        self.openGLWidget.paintGL = self.paintGL
        self.openGLWidget.initializeGL = self.initializeGL

    def paintGL(self):
        self.loadScene()
        Cube()

    def initializeGL(self):
        print("\033[4;30;102m INITIALIZE GL \033[0m")
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glEnable(GL_DEPTH_TEST)

    def loadScene(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        x, y, width, height = glGetDoublev(GL_VIEWPORT)
        gluPerspective(90, (900/600), 0.1, 50.0)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        gluLookAt(12, 12, 12, 0, 0, 0, 0, 1, 0)


app = qWidget.QApplication(sys.argv)
window = mainWindow()
window.setupUI()
window.show()
sys.exit(app.exec_())

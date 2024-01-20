import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

class ModelWindow():
    """
    ОКНО ОТОБРАЖЕНИЯ МОДЕЛИ
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

        pygame.init()
        display = (self.__width, self.__height)
        pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

        gluPerspective(90, (display[0]/display[1]), 0.1, 50.0)

        glLineWidth(3)
        glTranslatef(0.0,0.0, -10)

    def display_frame(self):
        """
        ОТОБРАЖЕНИЕ КАДРА ОКНА МОДЕЛИ
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    def drow_hand(self, points):
        """
        ОТРИСОВКА РУКИ
        """
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        self.model = Hand(points)
        self.model.draw()
        pygame.display.flip()
        pygame.time.wait(10)


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

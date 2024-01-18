import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

class ModelWindow():
    width = 900
    height = 600

    def __init__(self, width = 900, height = 600):
        self.width = width
        self.height = height

        pygame.init()
        display = (self.width, self.height)
        pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

        gluPerspective(90, (display[0]/display[1]), 0.1, 50.0)

        glTranslatef(0.0,0.0, -5)

    def display_frame(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    def drow_hand(self, points):
        finger_1 = Finger(points)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        finger_1.draw()
        pygame.display.flip()
        pygame.time.wait(10)


class Finger():
    x = 0
    y = 0
    z = 0

    def __init__(self, points):
        self.x = points.finger_1[0][1]
        self.y = points.finger_1[0][2]
        self.z = points.finger_1[0][3]

    def draw(self):
        vertices= (
                (0+0.01*self.x, 0-0.01*self.y, 0+10*self.z),
                (1+0.01*self.x, 0-0.01*self.y, 0+10*self.z),
                (0.5+0.01*self.x, 0.75-0.01*self.y, 0+10*self.z),
                (0.5+0.01*self.x, 0.3-0.01*self.y, 0.9+10*self.z),
        )
        print(vertices)

        edges = (
            (0,1),
            (1, 2),
            (2, 3),
            (3, 0),
            (1, 3),
            (0, 2)
        )

        glBegin(GL_LINES)
        for edge in edges:
            for vertex in edge:
                glVertex3fv(vertices[vertex])
        glEnd()



class Palm():
    pass


# d = ModelWindow()
# d.display_frame()
# while True:

#     for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     pygame.quit()
#                     quit()
#     glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
#     d.drow_hand(None)
#     pygame.display.flip()
#     pygame.time.wait(1)

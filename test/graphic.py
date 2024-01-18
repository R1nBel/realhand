import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
k = 1
verticies = (
    (0+k, 0, 0),
    (1+k, 0, 0),
    (0.5+k, 0.75, 0),
    (0.5+k, 0.3, 0.9),
    )

edges = (
    (0,1),
    (1, 2),
    (2, 3),
    (3, 0),
    (1, 3),
    (0, 2)
    )


def Cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()




def main():
    pygame.init()
    display = (900,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0,0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        pygame.time.wait(10)


main()

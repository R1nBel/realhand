import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

#verticies = [[355, 136, -0.10708111524581909], [358, 110, -0.14757897332310677], [357, 93, -0.16573325917124748], [353, 77, -0.1799609698355198]]

verticies = [[3, 1, -1], [-1, 1, -1], [3, 3, -1], [5, 7, -1]]

edges = (
    (0,1),
    (1, 2),
    (2, 3),
    (3, 0),
    (1, 3),
    (0, 2)
    )


def Cube():
    glLineWidth(10)
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()




def main():
    pygame.init()
    display = (900,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL,)

    gluPerspective(90, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0, 0, -10)

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

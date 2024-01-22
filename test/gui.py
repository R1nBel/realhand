
import pygame
import pygame_gui
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

verticies = [[3, 1, -1], [-1, 1, -1], [3, 3, -1], [5, 7, -1]]

edges = ((0,1),(1, 2),(2, 3),(3, 0),(1, 3),(0, 2))

def Cube():
    glLineWidth(10)
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()


pygame.init()


window_surface = pygame.display.set_mode((900, 600), DOUBLEBUF|OPENGL)
background = pygame.Surface((900, 600))
background.fill(pygame.Color('#AAAAAA'))

manager = pygame_gui.UIManager((900, 600))

# img = pygame.image.load('test/1.jpg')
# img.convert()

# window_surface.blit(img, (0, 0))

# vid1 = pygame_gui.elements.UIImage(relative_rect=pygame.Rect((0, 0), (600, 600)), image_surface=surf)



# gluPerspective(90, (900/600), 0.1, 50.0)
# glTranslatef(0, 0, -10)

# vid2 = pygame_gui.elements.UIImage(relative_rect=pygame.Rect((0, 0), (600, 600)), image_surface=window_surface)

clock = pygame.time.Clock()
is_running = True

while is_running:

    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        manager.process_events(event)

    manager.update(time_delta)

    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    # glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    # Cube()
    pygame.display.flip()

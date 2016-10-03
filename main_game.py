import pygame, sys
from game import *



pygame.init()
screen = pygame.display.set_mode((640, 360),0,32)
clock = pygame.time.Clock()
FPS = 65

bug = Bug(0,100, 50, 50, "robot50.png")

bug = Bug(0,200, 50, 50, "robot50.png")

bug = Bug(0,300, 50, 50, "robot50.png")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    bug.motion()
    screen.fill( (0,0,0))
    BaseClass.allsprites.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)
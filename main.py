import pygame, startScreen
from context import *
from pygame.locals import *

def run():
    pygame.init()
    pygame.display.set_caption('PY껨솟 - 햄버거 만들기')

    resolution = 500, 700
    screen = pygame.display.set_mode(resolution)

    clock = pygame.time.Clock()

    push(startScreen.startScreen(screen))
    while top():
        dt = clock.tick(1000)

        top_context = top()
        if top_context:
            top_context.think(dt)
            
if __name__ == '__main__':    
    run()

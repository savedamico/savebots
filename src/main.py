'''
SAVEBOTS 
v1.0.0

Saverio D'Amico

'''

import pygame
from actions import frame

(width, height) = (600, 400)
DARK_GREY_COLOR = (30,30,30)
CLOCK_TICK = 20
TITLE = "SAVEBOTS"

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption(TITLE)

background_colour = DARK_GREY_COLOR
clock = pygame.time.Clock()

running = True
while running:
    screen.fill(background_colour)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    frame()
    clock.tick(CLOCK_TICK)
    pygame.display.update()
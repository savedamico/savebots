'''
SAVEBOTS 
v1.0.0

Saverio D'Amico

'''

import pygame
import sys
from actions import frame, frame_learn
from utils.parsing import create_bots

(width, height) = (600, 400)
DARK_GREY_COLOR = (30,30,30)
CLOCK_TICK = 300
TITLE = "SAVEBOTS"

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption(TITLE)

background_colour = DARK_GREY_COLOR
clock = pygame.time.Clock()

# Load bots
def init():
    projectiles = []
    bots=[]
    # init bots
    bots = create_bots()
    for bot in bots:
        print(bot.name)
        if bot.name == "RL": 
            bot_RL = bot 
    return bot_RL, bots, projectiles

# Main func.
def main():
    running = True
    bot_RL, bots, projectiles = init()
    while running:
        screen.fill(background_colour)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                running = False
                quit()
        restart = frame_learn(bot_RL, bots, projectiles) 
        if restart: running = False
        clock.tick(CLOCK_TICK)
        pygame.display.update()
    
if __name__ == "__main__":
    while True:
        main()
'''
SAVEBOTS 
v1.0.0

Saverio D'Amico

'''

import pygame
import sys
import seaborn as sns
import numpy as np
import random
import matplotlib.pyplot as plt
from actions import frame, frame_learn
from utils.parsing import create_bots

(width, height) = (600, 400)
DARK_GREY_COLOR = (30,30,30)
CLOCK_TICK = 120
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
    
    return counter_games
    
def plot_seaborn(array_counter, array_score):
    sns.set(color_codes=True)
    ax = sns.regplot(np.array([array_counter])[0], np.array([array_score])[0], color="b", x_jitter=.1, line_kws={'color':'green'})
    ax.set(xlabel='games', ylabel='score')
    plt.show()


if __name__ == "__main__":
    
    score_plot = []
    counter_plot = []
    record = 0
    counter_games = 0
    score=0

    while counter_games < 5:
        main()
        score += random.choice([5,8,7,8,-2,4])
        counter_games += 1
        print('Game', counter_games, '      Score:', score)
        score_plot.append(score)
        counter_plot.append(counter_games)

    plot_seaborn(counter_plot, score_plot)



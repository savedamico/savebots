import pygame

from utils import create_bots
from actions import collide, shooting

(width, height) = (600, 400)


pygame.font.init() 
screen = pygame.display.set_mode((width, height))
myfont = pygame.font.SysFont('Times new roman', 30)



def frame_learn(bot_RL, bots, projectiles):

    # Bots visualization.
    for i, bot in enumerate(bots):
        if len(bots) is 1: # remaing one bot.
            return True
        else:
            if bot.visible is True:
                state = bot_RL.get_state()
                actions = bot_RL.predict_new_actions()
                bot.move()
                for bot2 in bots[i+1:]: # menage collisions between bots.
                    collide(bot, bot2)
                    bot2.move(bot)
                bot.display(screen)
                projectile = bot.weapon() # create projectile if bot shooting
                projectiles.append(bot.projectile)
            if bot.health < 0: # remove death bot from arena.
                #print('KILL ' + bot.name)
                bot.remove()
                bots.remove(bot)
            #print(str(bot.name) + ' ' + str(bot.health))
    
    # Projectile visualization.
    for projectile in projectiles:
        if projectile:
            for bot in bots:
                if projectile.visible is True:
                    projectile.move()
                    shooting(bot,projectile,screen)
                    projectile.draw(screen)

    # state = bot_RL.get_state()
    # bot_RL.predict_new_actions()
    print(state, actions)
    return False



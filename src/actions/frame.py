import pygame

from utils import create_bots
from actions import collide, shooting

(width, height) = (600, 400)

pygame.font.init() 
screen = pygame.display.set_mode((width, height))
myfont = pygame.font.SysFont('Times new roman', 30)

projectiles = []
bots=[]

# init bots
bots = create_bots()

def frame():
    for i, bot in enumerate(bots):
        if len(bots) is 1:
            bot.display(screen)
            bot.move()
            textsurface = myfont.render((bot.name.upper()+" WIN!"), False, (255, 255, 255))
            screen.blit(textsurface, ((width-120)/2, height/2))
        else:
            if bot.visible is True:
                bot.move()
                for bot2 in bots[i+1:]:
                    collide(bot, bot2)
                    bot2.move(bot)
                bot.display(screen)
                projectile = bot.weapon()
                projectiles.append(bot.projectile)
            if bot.health < 0:
                print('KILL ' + bot.name)
                bot.remove()
                bots.remove(bot)
            print(str(bot.name) + ' ' + str(bot.health))
    print()
    for projectile in projectiles:
        for bot in bots:
            if projectile.visible is True:
                projectile.move()
                shooting(bot,projectile,screen)
                projectile.draw(screen)
    return
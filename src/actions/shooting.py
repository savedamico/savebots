import math
import pygame

def shooting(bot, projectile, screen):
    dx = bot.x - projectile.x
    dy = bot.y - projectile.y
    distance = math.hypot(dx, dy)
    if distance < bot.size + projectile.size:
        bot.health -= 0.5
        projectile.remove()
        pygame.draw.circle(screen, (255,255,0), (int(projectile.x),int(projectile.y)), 10)

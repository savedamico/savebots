import pygame
import math
import random

from .lasers import *

(width, height) = (600, 400)
COLOR_RED = (255, 51, 0)
COLOR_BLACK = (0,0,0)
COLOR_GREEN = (0,255,0)
COLOR_WHITE = (255, 255, 255)

elasticity = 1
gravity = [math.pi, 0.002]

pygame.font.init()
myfont = pygame.font.SysFont("Times New Roman",size=25)

# Default type of bot.
class Default():

    def __init__(self, position, size, color, name, speed):
        self.name = name
        self.x = position[0]
        self.y = position[1]
        self.size = size
        self.color = color
        self.thickness = size
        #self.speed = random.choice([speed*0.2,speed*0.8])
        self.speed = speed * 0.8
        self.angle = 1
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 10
        self.visible = True
        self.projectile = None

    # Select weapon.
    def weapon(self):
        self.projectile = Laser(self.x, self.y, size_robot=self.size, color=COLOR_RED, size=2, angle_robot=self.angle)
        return self.projectile

    # Bot apparence.
    def display(self, screen):
        # robot
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size, self.thickness)
        pygame.draw.circle(screen, (50,50,50), (int(self.x + self.size * math.sin(self.angle)), int(self.y - self.size * math.cos(self.angle))), int(self.size*0.3), int(self.size*0.3))
        # health bar
        pygame.draw.rect(screen, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
        pygame.draw.rect(screen, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        # name
        textsurface = myfont.render(self.name, False, COLOR_WHITE)
        screen.blit(textsurface,(self.x + 17, self.y + 2,))

    # Moving engine.
    def move(self, bot=None):
        (self.angle, self.speed) = addVectors((self.angle, self.speed), gravity)
        self.x += math.sin(self.angle) * self.speed
        self.y -= math.cos(self.angle) * self.speed
        self.angle += random.choice([0.2,-0.2])

        if self.x > width - self.size:
            self.x = 2*(width - self.size) - self.x
            self.angle = - self.angle
            self.speed *= elasticity
        elif self.x < self.size:
            self.x = 2*self.size - self.x
            self.angle = - self.angle
            self.speed *= elasticity
        if self.y > height - self.size:
            self.y = 2*(height - self.size) - self.y
            self.angle = math.pi - self.angle
            self.speed *= elasticity
        elif self.y < self.size:
            self.y = 2*self.size - self.y
            self.angle = math.pi - self.angle
            self.speed *= elasticity

    # Remove bot.
    def remove(self):
        self.visible = False


# Second type of bot.
class Bot1():

    def __init__(self, position, size, color, name, speed):
        self.name = name
        self.x = position[0]
        self.y = position[1]
        self.size = size
        self.color = color
        self.thickness = size
        self.speed = random.choice([speed*0.2,speed*0.8])
        self.angle = 1
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 10
        self.visible = True
        self.projectile = None

    def weapon(self):
        self.projectile = Laser2(self.x, self.y, size_robot=self.size, color=COLOR_GREEN, size=2, angle_robot=self.angle)
        return self.projectile

    def display(self, screen):
        # robot
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size, self.thickness)
        pygame.draw.circle(screen, COLOR_BLACK, (int(self.x), int(self.y)), int(self.size), 2)
        pygame.draw.circle(screen, COLOR_BLACK, (int(self.x), int(self.y)), int(self.size*0.6), 1)
        pygame.draw.circle(screen, (50,50,50), (int(self.x + self.size * math.sin(self.angle)), int(self.y - self.size * math.cos(self.angle))), int(self.size*0.3), int(self.size*0.3))
        # health bar
        pygame.draw.rect(screen, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
        pygame.draw.rect(screen, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        # name
        textsurface = myfont.render(self.name, False, COLOR_WHITE)
        screen.blit(textsurface,(self.x + 17, self.y + 2,))

    def move(self,bot=None):
        (self.angle, self.speed) = addVectors((self.angle, self.speed), gravity)
        self.x += math.sin(self.angle) * self.speed
        self.y -= math.cos(self.angle) * self.speed
        self.angle += .1

        if self.x > width - self.size:
            self.x = 2*(width - self.size) - self.x
            self.angle = - self.angle
            self.speed *= elasticity
        elif self.x < self.size:
            self.x = 2*self.size - self.x
            self.angle = - self.angle
            self.speed *= elasticity
        if self.y > height - self.size:
            self.y = 2*(height - self.size) - self.y
            self.angle = math.pi - self.angle
            self.speed *= elasticity
        elif self.y < self.size:
            self.y = 2*self.size - self.y
            self.angle = math.pi - self.angle
            self.speed *= elasticity

    def remove(self):
        self.visible = False

# Third type of bot.
class BotSeek():

    def __init__(self, position, size, color, name, speed):
        self.name = name
        self.x = position[0]
        self.y = position[1]
        self.size = size
        self.color = color
        self.thickness = size
        self.speed = speed * 0.8
        self.angle = 1
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 10
        self.visible = True
        self.projectile = None

    def weapon(self):
        self.projectile = Laser(self.x, self.y, size_robot=self.size, color=COLOR_WHITE, size=2, angle_robot=self.angle)
        return self.projectile

    def display(self, screen):
        # robot
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size, self.thickness)
        pygame.draw.circle(screen, (50,50,50), (int(self.x + self.size * math.sin(self.angle)), int(self.y - self.size * math.cos(self.angle))), int(self.size*0.3), int(self.size*0.3))
        # health bar
        pygame.draw.rect(screen, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
        pygame.draw.rect(screen, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        # name
        textsurface = myfont.render(self.name, False, COLOR_WHITE)
        screen.blit(textsurface,(self.x + 17, self.y + 2,))

    def move(self, bot=None):
        # find other bot
        if bot:
            dx, dy = bot.x - self.x, bot.y - self.y
            dist = math.hypot(dx, dy) + bot.size
            dx, dy = dx / dist, dy / dist
            self.x += dx * self.speed 
            self.y += dy * self.speed 
            self.angle += random.choice([0.1,-0.1])
        # move random
        else: 
            (self.angle, self.speed) = addVectors((self.angle, self.speed), gravity)
            self.x += math.sin(self.angle) * self.speed
            self.y -= math.cos(self.angle) * self.speed
            self.angle += random.choice([0.2,-0.2])

        if self.x > width - self.size:
            self.x = 2*(width - self.size) - self.x
            self.angle = - self.angle
            self.speed *= elasticity
        elif self.x < self.size:
            self.x = 2*self.size - self.x
            self.angle = - self.angle
            self.speed *= elasticity
        if self.y > height - self.size:
            self.y = 2*(height - self.size) - self.y
            self.angle = math.pi - self.angle
            self.speed *= elasticity
        elif self.y < self.size:
            self.y = 2*self.size - self.y
            self.angle = math.pi - self.angle
            self.speed *= elasticity

    def remove(self):
        self.visible = False


def addVectors(xxx_todo_changeme1, xxx_todo_changeme2):
    (angle1, length1) = xxx_todo_changeme1
    (angle2, length2) = xxx_todo_changeme2
    x  = math.sin(angle1) * length1 + math.sin(angle2) * length2
    y  = math.cos(angle1) * length1 + math.cos(angle2) * length2
    angle = 0.5 * math.pi - math.atan2(y, x)
    length  = math.hypot(x, y)
    return (angle, length)
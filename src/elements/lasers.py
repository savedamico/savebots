import pygame
import math

(width, height) = (600, 400)

# First type of laser.
class Laser(object):
    def __init__(self, x, y, color, size, size_robot, angle_robot):
        self.name = 'BASIC LASER'
        self.x = x + (size_robot+2) * math.sin(angle_robot)
        self.y = y - (size_robot+2) * math.cos(angle_robot)
        self.size = size
        self.color = color
        self.size_robot = size_robot
        self.speed = 7
        self.visible = True
        self.angle_robot = angle_robot

    # projectile behavior
    def draw(self,screen):
        pygame.draw.circle(screen, self.color, (int(self.x),int(self.y)), self.size)

    # projectile move
    def move(self):
        self.x += self.speed * math.sin(self.angle_robot)
        self.y -= self.speed * math.cos(self.angle_robot) 

        if self.x > width - self.size:
            self.visible = False
        elif self.x < self.size:
            self.visible = False
        if self.y > height - self.size:
            self.visible = False
        elif self.y < self.size:
            self.visible = False
    
    # remove laser
    def remove(self):
        self.visible = False

# Second type of laser.
class Laser2(object):
    def __init__(self, x, y, color, size, size_robot, angle_robot):
        self.name = 'LASER2'
        self.x = x + (size_robot+2) * math.sin(angle_robot)
        self.y = y - (size_robot+2) * math.cos(angle_robot)
        self.size = size
        self.color = color
        self.size_robot = size_robot
        self.speed = 10
        self.visible = True
        self.angle_robot = angle_robot

    def draw(self,screen):
        pygame.draw.circle(screen, self.color, (int(self.x)+5,int(self.y)+5), self.size)
        pygame.draw.circle(screen, self.color, (int(self.x),int(self.y)), self.size)
        pygame.draw.circle(screen, self.color, (int(self.x)-5,int(self.y)-5), self.size)
        pygame.draw.circle(screen, self.color, (int(self.x + (self.size_robot+2) * math.sin(self.angle_robot)),int(self.y)), self.size)
    
    def move(self):
        self.x += self.speed * math.sin(self.angle_robot)
        self.y -= self.speed * math.cos(self.angle_robot) 
        self.speed +=2
        if self.x > width - self.size:
            self.visible = False
        elif self.x < self.size:
            self.visible = False
        if self.y > height - self.size:
            self.visible = False
        elif self.y < self.size:
            self.visible = False
    
    def remove(self):
        self.visible = False
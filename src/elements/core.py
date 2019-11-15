import pygame
import math
import random
import numpy as np

from .ai import neural_mock
from .ai import neural_net

from .lasers import *

SENSOR_LENGTH = 70


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
        random_shoot = random.choice([True, False])
        if random_shoot:
            self.projectile = Laser(self.x, self.y, size_robot=self.size, color=COLOR_RED, size=2, angle_robot=self.angle)
            return self.projectile
        else:
            return None

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


class ReinforcmentLearning_PLAY():

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

        # sensors
        self.first_x = self.x + (self.size + SENSOR_LENGTH) * math.sin(self.angle)
        self.first_y = self.y - (self.size + SENSOR_LENGTH) * math.cos(self.angle)
        self.second_x = self.x + (self.size + SENSOR_LENGTH) * math.sin(self.angle + 0.5)
        self.second_y = self.y - (self.size + SENSOR_LENGTH) * math.cos(self.angle + 0.5)
        self.third_x = self.x + (self.size + SENSOR_LENGTH) * math.sin(self.angle - 0.5)
        self.third_y = self.y - (self.size + SENSOR_LENGTH) * math.cos(self.angle - 0.5)


        # Model params.

        # Model input
        self.model = self.network()
        self.reward = 0
        self.old_state = None
        self.state = None
        self.old_state = self.state

    # Init Neural Net
    def network(self):
        SAVED_MODEL = None
        model = neural_net(SAVED_MODEL)
        return model
        
    def set_reward(self):
        return


    # Select weapon.
    def weapon(self):
        random_shoot = random.choice([True, False])
        if random_shoot:
            self.projectile = Laser(self.x, self.y, size_robot=self.size, color=COLOR_RED, size=2, angle_robot=self.angle)
            return self.projectile
        else:
            return None

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

        # sensors
        pygame.draw.circle(screen, COLOR_WHITE, (int(self.first_x), int(self.first_y)), int(self.size*0.3), int(self.size*0.3))
        pygame.draw.circle(screen, COLOR_WHITE, (int(self.second_x), int(self.second_y)), int(self.size*0.3), int(self.size*0.3))
        pygame.draw.circle(screen, COLOR_WHITE, (int(self.third_x), int(self.third_y)), int(self.size*0.3), int(self.size*0.3))


    # Moving engine.
    def move(self, bot=None):
        (self.angle, self.speed) = addVectors((self.angle, self.speed), gravity)
        
        move_x = math.sin(self.angle) * self.speed
        move_y = math.cos(self.angle) * self.speed
        move_angle = random.choice([0.2,-0.2])

        self.x += move_x
        self.y -= move_y
        self.angle += move_angle

        print(move_x)
        print(move_y)
        print(move_angle)

        # update sensors positions
        self.first_x = self.x + (self.size + SENSOR_LENGTH) * math.sin(self.angle)
        self.first_y = self.y - (self.size + SENSOR_LENGTH) * math.cos(self.angle)

        self.second_x = self.x + (self.size + SENSOR_LENGTH) * math.sin(self.angle + 0.5)
        self.second_y = self.y - (self.size + SENSOR_LENGTH) * math.cos(self.angle + 0.5)

        self.third_x = self.x + (self.size + SENSOR_LENGTH) * math.sin(self.angle - 0.5)
        self.third_y = self.y - (self.size + SENSOR_LENGTH) * math.cos(self.angle - 0.5)

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

        # if self.first_x > width - self.size:
        #     print('S1 fuori')
        # elif self.first_x < self.size:
        #     print('S1 fuori')
        # if self.first_y > height - self.size:
        #     print('S1 fuori')
        # elif self.first_y < self.size:
        #     print('S1 fuori')

        # if self.second_x > width - self.size:
        #     print('S2 fuori')
        # elif self.second_x < self.size:
        #     print('S2 fuori')
        # if self.second_y > height - self.size:
        #     print('S2 fuori')
        # elif self.second_y < self.size:
        #     print('S2 fuori')

        # if self.third_x > width - self.size:
        #     print('S3 fuori')
        # elif self.third_x < self.size:
        #     print('S3 fuori')
        # if self.third_y > height - self.size:
        #     print('S3 fuori')
        # elif self.third_y < self.size:
        #     print('S3 fuori')


    # Remove bot.
    def remove(self):
        self.visible = False


class ReinforcmentLearning_LEARN():

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
        self.health = 10 #10
        self.visible = True
        self.projectile = None

        # sensors
        self.first_x = self.x + (self.size + SENSOR_LENGTH) * math.sin(self.angle)
        self.first_y = self.y - (self.size + SENSOR_LENGTH) * math.cos(self.angle)
        self.second_x = self.x + (self.size + SENSOR_LENGTH) * math.sin(self.angle + 0.5)
        self.second_y = self.y - (self.size + SENSOR_LENGTH) * math.cos(self.angle + 0.5)
        self.third_x = self.x + (self.size + SENSOR_LENGTH) * math.sin(self.angle - 0.5)
        self.third_y = self.y - (self.size + SENSOR_LENGTH) * math.cos(self.angle - 0.5)
  
        # Parametri di input
        # self.move_x = None
        # self.move_y = None
        # self.move_angle = None
        # self.shoot = None
        # self.health_diff = None 
        # self.health_enemies = None

        # self.old_health = self.health
        # self.old_state = self.state


        self.enemies_x = 0 
        self.enemies_y = 0
        self.enemies_health = 0 

        move_x = math.sin(self.angle) * self.speed
        move_y = math.cos(self.angle) * self.speed
        move_angle = random.choice([0.2,-0.2])
        shoot = random.choice([True, False]) 
        actions = [move_x,move_y,move_angle,shoot]
        self.actions = actions

        # self.actions = init_actions()
        self.state = None

    # Init Neural Net
    # def network(self):
    #     SAVED_MODEL = None
    #     model = neural_net(SAVED_MODEL)
    #     return model
        

    def init_actions(self):   
        move_x = math.sin(self.angle) * self.speed
        move_y = math.cos(self.angle) * self.speed
        move_angle = random.choice([0.2,-0.2])
        shoot = random.choice([True, False]) 
        actions = [move_x,move_y,move_angle,shoot]
        return actions

    def get_state(self):
        # if self.health < self.old_health:
        #     health_diff = self.old_health - self.health
        #     self.old_health = self.health
        self.state = [
                self.x,
                self.y,
                self.angle,
                self.actions[3],
                self.health,
                self.enemies_x,
                self.enemies_y,
                self.enemies_health]

        return np.asarray(self.state)

    def predict_new_actions(self):
        #model = neural_net()
        #res_sate = np.asarray(self.state).reshape((1,8))
        #predicted_actions = model.predict(res_sate)
        #self.actions = predicted_actions[0]
        
        actionseee = neural_mock(self.state, self.angle, self.speed)
        print("*******************")
        #print(res_sate)
        #print(self.actions)
        return np.asarray(actionseee)

    # Set reward.
    def set_reward(self):
        reward = 0

        if shooted:
            reward =- 10
        if won:
            reward =+ 100
        if lose:
            reward =- 100
        if shooting:
            reward =+ 10

        return reward


    # Select weapon.
    def weapon(self):
        # random_shoot = random.choice([True, False])
        if self.actions[3]:
            self.projectile = Laser(self.x, self.y, size_robot=self.size, color=COLOR_RED, size=2, angle_robot=self.angle)
            return self.projectile
        else:
            return None

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

        # sensors
        pygame.draw.circle(screen, COLOR_WHITE, (int(self.first_x), int(self.first_y)), int(self.size*0.3), int(self.size*0.3))
        pygame.draw.circle(screen, COLOR_WHITE, (int(self.second_x), int(self.second_y)), int(self.size*0.3), int(self.size*0.3))
        pygame.draw.circle(screen, COLOR_WHITE, (int(self.third_x), int(self.third_y)), int(self.size*0.3), int(self.size*0.3))

    # Moving engine.
    def move(self, bot=None):
        (self.angle, self.speed) = addVectors((self.angle, self.speed), gravity)
        
        # move_x = math.sin(self.angle) * self.speed
        # move_y = math.cos(self.angle) * self.speed
        # move_angle = random.choice([0.2,-0.2])

        self.x += self.actions[0] # model.predict()
        self.y -= self.actions[1] 
        self.angle += self.actions[2] 

        # update sensors positions
        self.first_x = self.x + (self.size + SENSOR_LENGTH) * math.sin(self.angle)
        self.first_y = self.y - (self.size + SENSOR_LENGTH) * math.cos(self.angle)
        self.second_x = self.x + (self.size + SENSOR_LENGTH) * math.sin(self.angle + 0.5)
        self.second_y = self.y - (self.size + SENSOR_LENGTH) * math.cos(self.angle + 0.5)
        self.third_x = self.x + (self.size + SENSOR_LENGTH) * math.sin(self.angle - 0.5)
        self.third_y = self.y - (self.size + SENSOR_LENGTH) * math.cos(self.angle - 0.5)

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


    






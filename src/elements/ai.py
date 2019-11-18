from keras.optimizers import Adam
from keras.models import Sequential
from keras.layers.core import Dense, Dropout

import math
import random

def neural_net(weights=None):
    model = Sequential()
    model.add(Dense(output_dim=120, activation='relu', input_dim=9))
    model.add(Dropout(0.15))
    model.add(Dense(output_dim=120, activation='relu'))
    model.add(Dropout(0.15))
    model.add(Dense(output_dim=120, activation='relu'))
    model.add(Dropout(0.15))
    model.add(Dense(output_dim=2, activation='softmax'))
    opt = Adam(learning_rate=0.0005)
    model.compile(loss='mse', optimizer=opt)

    if weights:
        model.load_weights(weights)
    return model

def neural_mock(state,angle,speed):

    move_x = math.sin(angle) * speed
    move_y = math.cos(angle) * speed
    move_angle = random.choice([0.2,-0.2])
    shoot = random.choice([True, False])

    return [move_angle, shoot]
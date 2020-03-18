import pygame, sys
from pygame.math import Vector2

class Brick(object):
    def __init__(self, game,x,y):
        self.game = game
        self.pos=Vector2(round(x), round(y))
        self.bool=True





    def draw(self):
        return pygame.image.load("assets/brick.png")



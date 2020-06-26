import pygame
from pygame import math


class Brick(object):

    def __init__(self, game, x, y):
        self.game = game
        self.pos = math.Vector2(round(x), round(y))
        self.bool = True

    def draw(self):
        return pygame.image.load("assets/brick.png")

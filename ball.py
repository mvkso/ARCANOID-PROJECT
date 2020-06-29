import pygame
from pygame import math

import assets


class Ball(object):

    def __init__(self, game, x, y):

        self.game = game
        self.pos = math.Vector2(int(x), int(y))
        self.moveX = -1
        self.moveY = 2

    def tick(self):
        self.pos.x += self.moveX
        self.pos.y += self.moveY
        if self.pos.x > 920 or self.pos.x < 65:
            assets.Assets.bounce.play()
            self.moveX *= -1

        elif self.pos.y < 30:
            assets.Assets.bounce.play()
            self.moveY = 1
        elif self.pos.y > 750:
            self.moveY = 0
            self.moveX = 0

    def draw(self):
        return assets.Assets.ball_image

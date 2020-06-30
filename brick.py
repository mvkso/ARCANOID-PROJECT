from pygame import math

import assets


class Brick:

    def __init__(self, game, x, y):
        self.game = game
        self.pos = math.Vector2(round(x), round(y))
        self.bool = True

    def draw(self):
        return assets.Assets.brick_image

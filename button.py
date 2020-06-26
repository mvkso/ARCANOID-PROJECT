from pygame import math


class Button(object):
    def __init__(self, x, y, width, height, bool):
        self.bool = bool
        self.pos = math.Vector2(x, y)
        self.width = width

        self.height = height

    def draw(self):
        return [int(self.pos.x), int(self.pos.y), int(self.width), int(self.height)]


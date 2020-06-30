from pygame import math

import assets


class Ball:

    def __init__(self, game, x, y):

        self.game = game
        self.pos = math.Vector2(int(x), int(y))
        self.move_x = -1
        self.move_y = 2

    def tick(self):
        self.pos.x += self.move_x
        self.pos.y += self.move_y
        if self.pos.x > 920 or self.pos.x < 65:
            assets.Assets.ball_bounce_sound.play()
            self.move_x *= -1

        elif self.pos.y < 30:
            assets.Assets.ball_bounce_sound.play()
            self.move_y = 1
        elif self.pos.y > 750:
            self.move_y = 0
            self.move_x = 0

    def draw(self):
        return assets.Assets.ball_image

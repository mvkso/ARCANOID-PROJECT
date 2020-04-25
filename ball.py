import pygame
from pygame.math import Vector2

class Ball(object):
    def __init__(self, game, x, y):
        self.bounce=pygame.mixer.Sound("assets/bounce.wav")
        self.game = game
        self.pos = Vector2(int(x),int(y))
        self.moveX=-1
        self.moveY=2
    def tick(self):
        self.pos.x+=self.moveX
        self.pos.y+=self.moveY
        if self.pos.x>920 or self.pos.x<65:
            self.bounce.play()
            self.moveX*=-1

        elif self.pos.y<30:
            self.bounce.play()
            self.moveY=1
        elif self.pos.y>750:
            self.moveY=0
            self.moveX=0





    def draw(self):
        return pygame.image.load("assets/ball.png")



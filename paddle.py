import pygame
from pygame import math



class Paddle(object):

    def __init__(self, game):
        self.game = game
        self.moveX = 3
        self.pos = math.Vector2(460, 650)

    def tick(self):
        # Input
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_a]:
            self.pos.x -= self.moveX
        if pressed[pygame.K_d]:
            self.pos.x += self.moveX
        if self.pos.x > 840:
            self.pos.x = 840
        if self.pos.x < 80:
            self.pos.x = 80
        # fizyka

    def draw(self):

        paddle1 = [self.pos.x, self.pos.y, 100, 15]
        # Draw triangle
        pygame.draw.rect(self.game.screen, (255, 215, 0), pygame.Rect(paddle1))

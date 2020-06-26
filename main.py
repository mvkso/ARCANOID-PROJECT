import sys
import random

import pygame
from pygame import math

from paddle import Paddle
from brick import Brick
from ball import Ball
from button import Button
from colors import Colors


class Game(object):
    tps_max = 15.0
    TEMP_COLOR = Colors.HOVER_COLOR
    TEMP_COLOR2 = Colors.HOVER_COLOR
    level = 1
    score = 0
    i = 0
    temp = 0
    temp2 = 0
    screen = pygame.display.set_mode((1280, 720))
    tps_clock = pygame.time.Clock()
    tps_delta = 0.0

    LEVEL_PARAMS = [(1, 1, 3, -1, 2), (2, 4, 3, -2, 1),
                    (3, 8, 3, -2, 1), (4, 10, 3, -2, 2),
                    (5, 15, 3, -3, 2), (6, 20, 3, -2, 3),
                    (7, 25, 3, -3, 3), (8, 27, 3, -3, 4),
                    (9, 29, 3, -4, 4), (10, 29, 6, -7, 5)]

    def __init__(self):
        pygame.init()
        pygame.mixer.init(44100, -16, 2, 2048)
        try:
            self.failure = pygame.mixer.Sound("assets/lose.wav")
            self.hitSound = pygame.mixer.Sound("assets/hit.wav")
            self.winSound = pygame.mixer.Sound("assets/win.wav")
            # self.menuSong=pygame.mixer.Sound("assets/menu.wav")
            self.bounceSound = pygame.mixer.Sound("assets/bounce.wav")
        except:
            raise Exception("Music initialization went wrong")

        self.font = pygame.font.Font(None, 72)
        self.font2 = pygame.font.Font(None, 72)
        self.font3 = pygame.font.Font(None, 45)
        self.font4 = pygame.font.Font(None, 72)
        self.font5 = pygame.font.Font(None, 72)
        #  hitSound = pygame.mixer.Sound("assets/hit.wav")

        # nazwa gry

        try:
            pygame.display.set_caption("Arcanoid")
            self.icon = pygame.image.load("assets/rocket.png")
            self.interface = pygame.image.load("assets/interface.png")
            self.cosmos = pygame.image.load("assets/cosmos.png")
            pygame.display.set_icon(self.icon)
        except FileNotFoundError:
            raise Exception("File not found")
        self.screen = pygame.display.set_mode((1280, 720))
        self.tps_clock = pygame.time.Clock()
        self.tps_delta = 0.0

        self.player = Paddle(self)
        self.ball = Ball(self, 600, 350)
        self.button = Button(440, 200, 400, 100, False)
        self.button2 = Button(440, 500, 400, 100, False)

        self.list = []

        for i in range(5):
            self.list.append(Brick(self, random.randint(100, 400), random.randint(100, 400)))

    def tick(self):
        # checking Inputs

        self.player.tick()
        self.ball.tick()
        if (self.player.pos.x - 5) < self.ball.pos.x < (self.player.pos.x + 105) and (
                self.ball.pos.y > self.player.pos.y - 20):
            if self.ball.pos.y < self.player.pos.y + 20:
                self.bounceSound.play()
                self.ball.moveY = -1

    def draw(self):
        # drawing
        self.player.draw()
        pygame.image.load("assets/ball.png")

    def collision(self, ball: Ball, brick: Brick):
        try:
            self.screen.blit(brick.draw(), (int(brick.pos.x), int(brick.pos.y)))
            if (brick.pos.x - 5) < ball.pos.x < (brick.pos.x + 69) and (
                    ball.pos.y > brick.pos.y - 10) and ball.pos.y < brick.pos.y + 74:
                self.hitSound.play()
                ball.moveY *= -1
                ball.moveX *= -1
                brick.bool = False
                self.score += 1
        except TypeError:
            raise Exception("Type Error in collision")
        except:
            raise Exception("Collision function error")

    def isOver(self, button: Button, mouse_pos: tuple):
        try:
            if button.pos[0] < mouse_pos[0] < button.pos[0] + button.width:
                if button.pos[1] < mouse_pos[1] < button.pos[1] + button.height:
                    return True
            return False
        except TypeError:
            raise Exception("Type Error - isOver fun")
        except Exception:
            raise Exception("Error - isOver")

    def wait(self, x: int, y: int):
        try:
            if self.i < 100:
                self.ball.moveX = 0
                self.ball.moveY = 0
                self.i += 1
            elif self.i == 100:
                self.ball.moveX = x
                self.ball.moveY = y
                self.i += 1
        except TypeError:
            raise Exception("Type Error")
        except Exception:
            raise Exception("Error - wait")

    def you_lost_statement(self):
        if self.temp == 0:
            self.failure.play()
            self.temp += 1
        pygame.draw.rect(self.screen, self.TEMP_COLOR, pygame.Rect(self.button.draw()))
        text3 = self.font3.render("YOU LOST", 1, (0, 0, 0))
        self.screen.blit(text3, ((int(self.button.pos.x + self.button.width / 2 - text3.get_width() / 2)),
                                 int((self.button.pos.y + self.button.height / 2 - text3.get_height() / 2))))

    def next_level_button(self, level):
        try:
            if self.temp2 == 0:
                self.winSound.play()
                self.temp2 += 1

            self.ball.moveX = 0
            self.ball.moveY = 0
            self.player.moveX = 0
            if level < 10:
                pygame.draw.rect(self.screen, self.TEMP_COLOR, pygame.Rect(self.button.draw()))
                text3 = self.font3.render("DOUBLE CLICK TO LVL " + str(level + 1), 1, (0, 0, 0))
                self.screen.blit(text3, ((int(self.button.pos.x + self.button.width / 2 - text3.get_width() / 2)),
                                         int((self.button.pos.y + self.button.height / 2 - text3.get_height() / 2))))
            elif level == 10:
                pygame.draw.rect(self.screen, self.TEMP_COLOR, pygame.Rect(self.button.draw()))
                text3 = self.font3.render("YOU WON!!!!!!!!!!!!", 1, (0, 0, 0))
                self.screen.blit(text3, ((int(self.button.pos.x + self.button.width / 2 - text3.get_width() / 2)),
                                         int((self.button.pos.y + self.button.height / 2 - text3.get_height() / 2))))
            elif level > 10:
                pygame.draw.rect(self.screen, self.TEMP_COLOR, pygame.Rect(self.button.draw()))
                text3 = self.font3.render("Nie powinno Cie tu byc", 1, (0, 0, 0))
                self.screen.blit(text3, ((int(self.button.pos.x + self.button.width / 2 - text3.get_width() / 2)),
                                         int((self.button.pos.y + self.button.height / 2 - text3.get_height() / 2))))

        except TypeError:
            raise Exception("Type Error")
        except Exception:
            raise Exception("Error - next_level_button")

    ########################MAIN MENU###############
    def main_menu(self):
        # self.menuSong.play(-1)
        self.ball.moveY = 0
        self.ball.moveX = 0
        self.button2.bool = True
        self.button.bool = True
        while True:
            for event in pygame.event.get():
                mpos = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEMOTION:
                    if self.isOver(self.button, mpos):
                        self.TEMP_COLOR = Colors.HOVER_COLOR
                    else:
                        self.TEMP_COLOR = Colors.BUTTON_COLOR
                    if self.isOver(self.button2, mpos):
                        self.TEMP_COLOR2 = Colors.HOVER_COLOR
                    else:
                        self.TEMP_COLOR2 = Colors.BUTTON_COLOR

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button.bool and self.isOver(self.button, mpos):
                        self.button.bool = False
                        # self.menuSong.stop()
                        return 0
                    if self.button2.bool and self.isOver(self.button2, mpos):
                        self.button2.bool = False
                        sys.exit(0)

                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)
            self.screen.fill((130, 130, 130))
            self.screen.blit(self.cosmos, (0, 0))
            if self.button.bool:
                pygame.draw.rect(self.screen, self.TEMP_COLOR, pygame.Rect(self.button.draw()))
                text4 = self.font4.render("LETS PLAY", 1, (0, 0, 0))
                self.screen.blit(text4, ((int(self.button.pos.x + self.button.width / 2 - text4.get_width() / 2)),
                                         int((self.button.pos.y + self.button.height / 2 - text4.get_height() / 2))))
            if self.button2.bool:
                pygame.draw.rect(self.screen, self.TEMP_COLOR2, pygame.Rect(self.button2.draw()))
                text5 = self.font5.render("QUIT", 1, (0, 0, 0))
                self.screen.blit(text5, ((int(self.button2.pos.x + self.button.width / 2 - text5.get_width() / 2)),
                                         int((self.button2.pos.y + self.button.height / 2 - text5.get_height() / 2))))

            pygame.display.flip()

    def generator_poziomow(self, level, a, b, c, d):
        try:
            points = self.score
            list_of_bricks = []
            for i in range(a):
                list_of_bricks.append(Brick(self, random.randint(70, 884), random.randint(70, 500)))
            for brick in list_of_bricks:
                brick.bool = True

            self.TEMP_COLOR
            self.TEMP_COLOR2
            self.i = 0
            self.button = Button(310, 300, 400, 100, False)
            self.button2 = Button(310, 300, 400, 100, False)
            self.ball.pos.x = 500
            self.ball.pos.y = 550
            self.player.moveX = b

            while True:

                # Handle events
                for event in pygame.event.get():
                    mpos = pygame.mouse.get_pos()
                    if event.type == pygame.QUIT:
                        sys.exit(0)
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        sys.exit(0)
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        self.score += 1
                    elif event.type == pygame.MOUSEMOTION:
                        if self.isOver(self.button, mpos):
                            TEMP_COLOR = Colors.HOVER_COLOR
                        elif self.isOver(self.button, mpos):
                            TEMP_COLOR2 = Colors.BUTTON_COLOR
                        else:
                            TEMP_COLOR = Colors.HOVER_COLOR
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if self.button2.bool and self.isOver(self.button2, mpos):
                            self.button2.bool = False
                            return True

                        if self.button.bool and self.isOver(self.button, mpos):
                            for i in list_of_bricks:
                                i.bool = True
                            self.button.bool = False
                            self.ball.moveY = 0
                            self.ball.moveX = 0
                            self.ball.pos.x = 500
                            self.ball.pos.y = 550
                            self.player.pos = math.Vector2(460, 650)
                            self.score = 0
                            self.i = 0
                            self.temp = 0

                # ticking
                self.tps_delta += self.tps_clock.tick() / 120.0
                while self.tps_delta > 1 / self.tps_max:
                    self.tick()
                    self.tps_delta -= 1 / self.tps_max

                # drawing
                self.screen.fill((130, 130, 130))
                self.screen.blit(self.interface, (0, 0))
                for i in list_of_bricks:
                    if i.bool:
                        self.collision(self.ball, i)

                text = self.font.render(str(self.score), 1, (130, 105, 20))
                text2 = self.font2.render(str(level), 1, (130, 105, 20))
                self.screen.blit(text, (1115, 420))
                self.screen.blit(text2, (1115, 260))
                self.screen.blit(pygame.image.load("assets/ball.png"), (int(self.ball.pos.x), int(self.ball.pos.y)))
                old_y = self.ball.pos.y

                self.draw()
                if old_y > 700:
                    self.button.bool = True
                    self.you_lost_statement()

                if self.score == points + a:
                    self.button2.bool = True
                    self.next_level_button(level)

                self.wait(c, d)
                pygame.display.flip()
        except TypeError:
            raise Exception("Type Error")
        except Exception:
            raise Exception("Error - level creator")

    def play(self):
        try:
            i = 0
            level = True
            self.main_menu()
            if self.main_menu() == 0:
                while level:
                    level = self.generator_poziomow(*self.LEVEL_PARAMS[i])
                    i += 1
            print("finish")
            return True
        except TypeError:
            raise Exception("Type Error")
        except ValueError:
            raise Exception("Value Error")
        except Exception:
            raise Exception("Error")


def main():
    game = Game()
    game.play()



if __name__ == "__main__":
    main()

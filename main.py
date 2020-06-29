import sys
import random

import pygame
from pygame import math

import assets
import paddle
import brick
import ball
import button
import colors


class Game(object):
    LEVEL_PARAMS = [(1, 1, 3, -1, 2), (2, 4, 3, -2, 1),
                    (3, 8, 3, -2, 1), (4, 10, 3, -2, 2),
                    (5, 15, 3, -3, 2), (6, 20, 3, -2, 3),
                    (7, 25, 3, -3, 3), (8, 27, 3, -3, 4),
                    (9, 29, 3, -4, 4), (10, 29, 6, -7, 5)]

    def __init__(self):
        self.tps_max = 15.0
        self.TEMP_COLOR = colors.Colors.GREEN
        self.TEMP_COLOR2 = colors.Colors.GREEN
        self.level = 1
        self.score = 0
        self.i = 0
        self.temp = 0
        self.temp2 = 0
        self.screen = pygame.display.set_mode((1280, 720))
        self.tps_clock = pygame.time.Clock()
        self.tps_delta = 0.0
        try:
            assets.Assets.load()
        except:
            raise Exception("Music initialization went wrong")

        #  hitSound = pygame.mixer.Sound("assets/hit.wav")

        try:
            pygame.display.set_caption("Arcanoid")

            pygame.display.set_icon(assets.Assets.icon)
        except FileNotFoundError:
            raise Exception("File not found")
        self.screen = pygame.display.set_mode((1280, 720))
        self.tps_clock = pygame.time.Clock()
        self.tps_delta = 0.0

        self.player = paddle.Paddle(self)
        self.ball = ball.Ball(self, 600, 350)
        self.button = button.Button(440, 200, 400, 100, False)
        self.button2 = button.Button(440, 500, 400, 100, False)

        self.list = []

        for i in range(5):
            self.list.append(brick.Brick(self, random.randint(100, 400), random.randint(100, 400)))

    def tick(self):
        # checking Inputs

        self.player.tick()
        self.ball.tick()
        if (self.player.pos.x - 5) < self.ball.pos.x < (self.player.pos.x + 105) and (
                self.ball.pos.y > self.player.pos.y - 20):
            if self.ball.pos.y < self.player.pos.y + 20:
                assets.Assets.ball_bounce_sound.play()
                self.ball.moveY = -1

    def draw(self):
        # drawing
        self.player.draw()

    def collision(self, ball: ball.Ball, brick: brick.Brick):
        try:
            self.screen.blit(brick.draw(), (int(brick.pos.x), int(brick.pos.y)))
            if (brick.pos.x - 5) < ball.pos.x < (brick.pos.x + 69) and (
                    ball.pos.y > brick.pos.y - 10) and ball.pos.y < brick.pos.y + 74:
                assets.Assets.brick_collision_sound.play()
                ball.moveY *= -1
                ball.moveX *= -1
                brick.bool = False
                self.score += 1
        except TypeError:
            raise Exception("Type Error in collision")
        except:
            raise Exception("Collision function error")

    def isOver(self, button: button.Button, mouse_pos: tuple):
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
            assets.Assets.faulure_sound.play()
            self.temp += 1
        pygame.draw.rect(self.screen, self.TEMP_COLOR, pygame.Rect(self.button.draw()))
        text3 = assets.Assets.font_3.render("YOU LOST", 1, (0, 0, 0))
        self.screen.blit(text3, ((int(self.button.pos.x + self.button.width / 2 - text3.get_width() / 2)),
                                 int((self.button.pos.y + self.button.height / 2 - text3.get_height() / 2))))

    def next_level_button(self, level):
        try:
            if self.temp2 == 0:
                assets.Assets.winning_sound.play()
                self.temp2 += 1

            self.ball.moveX = 0
            self.ball.moveY = 0
            self.player.moveX = 0
            if level < 10:
                pygame.draw.rect(self.screen, self.TEMP_COLOR, pygame.Rect(self.button.draw()))
                text3 = assets.Assets.font_3.render("DOUBLE CLICK TO LVL " + str(level + 1), 1, (0, 0, 0))
                self.screen.blit(text3, ((int(self.button.pos.x + self.button.width / 2 - text3.get_width() / 2)),
                                         int((self.button.pos.y + self.button.height / 2 - text3.get_height() / 2))))
            elif level == 10:
                pygame.draw.rect(self.screen, self.TEMP_COLOR, pygame.Rect(self.button.draw()))
                text3 = assets.Assets.font_3.render("YOU WON!!!!!!!!!!!!", 1, (0, 0, 0))
                self.screen.blit(text3, ((int(self.button.pos.x + self.button.width / 2 - text3.get_width() / 2)),
                                         int((self.button.pos.y + self.button.height / 2 - text3.get_height() / 2))))
            elif level > 10:
                pygame.draw.rect(self.screen, self.TEMP_COLOR, pygame.Rect(self.button.draw()))
                text3 = assets.Assets.font_3.render("Nie powinno Cie tu byc", 1, (0, 0, 0))
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
                mouse_pos = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEMOTION:
                    if self.isOver(self.button, mouse_pos):
                        self.TEMP_COLOR = colors.Colors.GREEN
                    else:
                        self.TEMP_COLOR = colors.Colors.RED
                    if self.isOver(self.button2, mouse_pos):
                        self.TEMP_COLOR2 = colors.Colors.GREEN
                    else:
                        self.TEMP_COLOR2 = colors.Colors.RED

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button.bool and self.isOver(self.button, mouse_pos):
                        self.button.bool = False
                        # self.menuSong.stop()
                        return 0
                    if self.button2.bool and self.isOver(self.button2, mouse_pos):
                        self.button2.bool = False
                        sys.exit(0)

                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)
            self.screen.fill((130, 130, 130))
            self.screen.blit(assets.Assets.cosmos, (0, 0))
            if self.button.bool:
                pygame.draw.rect(self.screen, self.TEMP_COLOR, pygame.Rect(self.button.draw()))
                text4 = assets.Assets.font_4.render("LETS PLAY", 1, (0, 0, 0))
                self.screen.blit(text4, ((int(self.button.pos.x + self.button.width / 2 - text4.get_width() / 2)),
                                         int((self.button.pos.y + self.button.height / 2 - text4.get_height() / 2))))
            if self.button2.bool:
                pygame.draw.rect(self.screen, self.TEMP_COLOR2, pygame.Rect(self.button2.draw()))
                text5 = assets.Assets.font_5.render("QUIT", 1, (0, 0, 0))
                self.screen.blit(text5, ((int(self.button2.pos.x + self.button.width / 2 - text5.get_width() / 2)),
                                         int((self.button2.pos.y + self.button.height / 2 - text5.get_height() / 2))))

            pygame.display.flip()

    def generator_poziomow(self, level, a, b, c, d):
        try:
            points = self.score
            list_of_bricks = []
            for i in range(a):
                list_of_bricks.append(brick.Brick(self, random.randint(70, 884), random.randint(70, 500)))
            for brick_object in list_of_bricks:
                brick_object.bool = True

            self.TEMP_COLOR
            self.TEMP_COLOR2
            self.i = 0
            self.button = button.Button(310, 300, 400, 100, False)
            self.button2 = button.Button(310, 300, 400, 100, False)
            self.ball.pos.x = 500
            self.ball.pos.y = 550
            self.player.moveX = b

            while True:

                # Handle events
                for event in pygame.event.get():
                    mouse_pos = pygame.mouse.get_pos()
                    if event.type == pygame.QUIT:
                        sys.exit(0)
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        sys.exit(0)
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        self.score += 1
                    elif event.type == pygame.MOUSEMOTION:
                        if self.isOver(self.button, mouse_pos):
                            self.TEMP_COLOR = colors.Colors.GREEN
                        elif self.isOver(self.button, mouse_pos):
                            self.TEMP_COLOR2 = colors.Colors.RED
                        else:
                            self.TEMP_COLOR = colors.Colors.GREEN
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if self.button2.bool and self.isOver(self.button2, mouse_pos):
                            self.button2.bool = False
                            return True

                        if self.button.bool and self.isOver(self.button, mouse_pos):
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
                self.screen.blit(assets.Assets.interface, (0, 0))
                for i in list_of_bricks:
                    if i.bool:
                        self.collision(self.ball, i)

                text = assets.Assets.font.render(str(self.score), 1, (130, 105, 20))
                text2 = assets.Assets.font_2.render(str(level), 1, (130, 105, 20))
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
    pygame.init()
    pygame.mixer.init(44100, -16, 2, 2048)
    game = Game()
    game.play()


if __name__ == "__main__":
    main()

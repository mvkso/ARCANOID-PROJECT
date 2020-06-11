import pygame, sys
from paddle import Paddle
from brick import Brick
from ball import Ball
from pygame.math import Vector2
from button import Button
import random



class Game(object):
    tps_max = 15.0
    colorb = (150, 150, 150)
    colorb2 = (150, 150, 150)
    lvl = 1
    score = 0
    i = 0
    temp = 0
    temp2 = 0
    screen = pygame.display.set_mode((1280, 720))
    tps_clock = pygame.time.Clock()
    tps_delta = 0.0


    def __init__(self):
        #config

        #inicjalizacja
        try:
            pygame.init()
            pygame.mixer.init(44100, -16,2,2048)
            self.failure=pygame.mixer.Sound("assets/lose.wav")
            self.hitSound=pygame.mixer.Sound("assets/hit.wav")
            self.winSound=pygame.mixer.Sound("assets/win.wav")
            self.menuSong=pygame.mixer.Sound("assets/menu.wav")
            self.bounceSound=pygame.mixer.Sound("assets/bounce.wav")
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
            self.interface=pygame.image.load("assets/interface.png")
            self.cosmos=pygame.image.load("assets/cosmos.png")
            pygame.display.set_icon(self.icon)
        except FileNotFoundError:
            raise Exception("File not found")
        self.screen= pygame.display.set_mode((1280,720))
        self.tps_clock=pygame.time.Clock()
        self.tps_delta= 0.0

        self.player= Paddle(self)
        self.ball=Ball(self, 600,350)
        self.button=Button(440,200,400,100,False)
        self.button2=Button(440,500,400,100,False)


        self.list=[]

        for i in range(0,5):
            self.list.append(Brick(self,random.randint(100,400),random.randint(100,400)))







        try:
            self.main_menu()
            if self.main_menu()==0:
                lvl1=self.lvl_creator(1,3,3,-1,2)
            if lvl1==0:
                lvl2=self.lvl_creator(2,4,3,-2,1)
            if lvl2==0:
                lvl3=self.lvl_creator(3,8,3,-2,1)
            if lvl3 == 0:
                lvl4 = self.lvl_creator(4, 10, 3, -2, 2)
            if lvl4 == 0:
                lvl5 = self.lvl_creator(5, 15, 3, -3, 2)
            if lvl5 == 0:
                lvl6 = self.lvl_creator(6, 20, 3, -2, 3)
            if lvl6 == 0:
                lvl7 = self.lvl_creator(7, 25, 3, -3, 3)
            if lvl7 == 0:
                lvl8 = self.lvl_creator(8, 27, 3, -3, 4)
            if lvl8 == 0:
                lvl9 = self.lvl_creator(9, 29, 3, -4, 4)
            if lvl9 == 0:
                lvl10= self.lvl_creator(10,30,5,-4,5)
            if lvl10 == 0:
                sys.exit(0)
        except TypeError:
            raise Exception("Type Error")
        except ValueError:
            raise Exception("Value Error")






        #
        # if level9()==0:
        #     self.temp2 = 0
        #     self.score = 0
        #     level10()
        # else:
        #     sys.exit(0)



        ##############WYWOLYWANIE GRY############


    def tick(self):
        # checking Inputs

        self.player.tick()
        self.ball.tick()
        if self.ball.pos.x > (self.player.pos.x-5) and self.ball.pos.x < (self.player.pos.x+105) and (self.ball.pos.y>self.player.pos.y-20):
            if self.ball.pos.y<self.player.pos.y+20:
                self.bounceSound.play()
                self.ball.moveY=-1
        #self.ball.tick()




    def draw(self):
        # drawing
        self.player.draw()
        self.ball.draw()

    def collision(self,ball: Ball, brick: Brick):
        try:
            self.screen.blit(brick.draw(), (int(brick.pos.x), int(brick.pos.y)))
            if ball.pos.x > (brick.pos.x - 5) and ball.pos.x < (brick.pos.x + 69) and (
                    ball.pos.y > brick.pos.y - 10) and ball.pos.y < brick.pos.y + 74:
                self.hitSound.play()
                ball.moveY *= -1
                ball.moveX *= -1
                brick.bool = False
                self.score += 1
        except TypeError:
            raise Exception("Type Error in collision")
        except ValueError:
            raise Exception("Value Error in collision")
        except:
            raise Exception("Collision function error")

    def isOver(self,button: Button, mpos: tuple):
        try:
            if mpos[0] > button.pos.x and mpos[0] < button.pos[0] + button.width:
                if mpos[1] > button.pos[1] and mpos[1] < button.pos[1] + button.height:
                    return True
            return False
        except TypeError:
            raise Exception("Type Error - isOver fun")
        except ValueError:
            raise Exception("Value Error - isOver fun")

    def wait(self,x, y):
        try:
            if self.i < 100:
                self.ball.moveX = 0
                self.ball.moveY = 0
                self.i += 1
            elif self.i == 100:
                self.ball.moveX = x
                self.ball.moveY = y
                self.i += 1
                print(self.ball.pos)
        except TypeError:
            raise Exception("Type Error")
        except ValueError:
            raise Exception("Value Error")

    def youlost(self):
        if self.temp == 0:
            self.failure.play()
            self.temp += 1
        global colorb
        pygame.draw.rect(self.screen, colorb, pygame.Rect(self.button.draw()))
        text3 = self.font3.render("YOU LOST", 1, (0, 0, 0))
        self.screen.blit(text3, ((int(self.button.pos.x + self.button.width / 2 - text3.get_width() / 2)),
                                 int((self.button.pos.y + self.button.height / 2 - text3.get_height() / 2))))

    def nextlevelbutton(self,lvl):
        try:
            if self.temp2 == 0:
                self.winSound.play()
                self.temp2 += 1

            global colorb
            self.ball.moveX = 0
            self.ball.moveY = 0
            self.player.moveX = 0
            if lvl < 10:
                pygame.draw.rect(self.screen, colorb, pygame.Rect(self.button.draw()))
                text3 = self.font3.render("DOUBLE CLICK TO LVL " + str(lvl + 1), 1, (0, 0, 0))
                self.screen.blit(text3, ((int(self.button.pos.x + self.button.width / 2 - text3.get_width() / 2)),
                                         int((self.button.pos.y + self.button.height / 2 - text3.get_height() / 2))))
            elif lvl == 10:
                pygame.draw.rect(self.screen, colorb, pygame.Rect(self.button.draw()))
                text3 = self.font3.render("YOU WON!!!!!!!!!!!!", 1, (0, 0, 0))
                self.screen.blit(text3, ((int(self.button.pos.x + self.button.width / 2 - text3.get_width() / 2)),
                                         int((self.button.pos.y + self.button.height / 2 - text3.get_height() / 2))))
        except TypeError:
            raise Exception("Type Error")
        except ValueError:
            raise Exception("Value Error")

    ########################MAIN MENU###############
    def main_menu(self):
        self.menuSong.play(-1)

        # self.colorb
        # self.colorb2
        self.ball.moveY = 0
        self.ball.moveX = 0
        self.button2.bool = True
        self.button.bool = True
        while True:
            for event in pygame.event.get():
                mpos = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEMOTION:
                    if self.isOver(self.button, mpos):
                        self.colorb = (0, 255, 0)
                    else:
                        self.colorb = (255, 0, 9)
                    if self.isOver(self.button2, mpos):
                        self.colorb2 = (0, 255, 0)
                    else:
                        self.colorb2 = (255, 0, 0)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button.bool == True and self.isOver(self.button, mpos):
                        self.button.bool = False
                        self.menuSong.stop()
                        return 0
                    if self.button2.bool == True and self.isOver(self.button2, mpos):
                        self.button2.bool = False
                        sys.exit(0)

                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)
            self.screen.fill((130, 130, 130))
            self.screen.blit(self.cosmos, (0, 0))
            if self.button.bool == True:
                pygame.draw.rect(self.screen, self.colorb, pygame.Rect(self.button.draw()))
                text4 = self.font4.render("LETS PLAY", 1, (0, 0, 0))
                self.screen.blit(text4, ((int(self.button.pos.x + self.button.width / 2 - text4.get_width() / 2)),
                                         int((self.button.pos.y + self.button.height / 2 - text4.get_height() / 2))))
            if self.button2.bool == True:
                pygame.draw.rect(self.screen, self.colorb2, pygame.Rect(self.button2.draw()))
                text5 = self.font5.render("QUIT", 1, (0, 0, 0))
                self.screen.blit(text5, ((int(self.button2.pos.x + self.button.width / 2 - text5.get_width() / 2)),
                                         int((self.button2.pos.y + self.button.height / 2 - text5.get_height() / 2))))

            pygame.display.flip()

    def lvl_creator(self,lvl, a, b, c, d):
        try:
            points = self.score
            list = []
            for i in range(0, a):
                list.append(Brick(self, random.randint(70, 884), random.randint(70, 500)))
            for i in list:
                i.bool = True

            global colorb
            global colorb2
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
                            colorb = (0, 255, 0)
                        elif self.isOver(self.button, mpos):
                            colorb2 = (0, 255, 0)
                        else:
                            colorb = (255, 0, 0)
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if self.button2.bool == True and self.isOver(self.button2, mpos):
                            self.button2.bool = False
                            return 0

                        if self.button.bool == True and self.isOver(self.button, mpos):
                            for i in list:
                                i.bool = True
                            self.button.bool = False
                            self.ball.moveY = 0
                            self.ball.moveX = 0
                            self.ball.pos.x = 500
                            self.ball.pos.y = 550
                            self.player.pos = Vector2(460, 650)
                            # self.ball.moveX=-1
                            # self.ball.moveY=2
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
                for i in list:
                    if i.bool == True:
                        self.collision(self.ball, i)

                text = self.font.render(str(self.score), 1, (130, 105, 20))
                text2 = self.font2.render(str(lvl), 1, (130, 105, 20))
                self.screen.blit(text, (1115, 420))
                self.screen.blit(text2, (1115, 260))
                self.screen.blit(self.ball.draw(), (int(self.ball.pos.x), int(self.ball.pos.y)))
                temp = self.ball.pos.y

                self.draw()
                if temp > 700:
                    self.button.bool = True
                    self.youlost()

                if self.score == points + a:
                    self.button2.bool = True
                    self.nextlevelbutton(lvl)

                self.wait(c, d)
                pygame.display.flip()
        except TypeError:
            raise Exception("Type Error")
        except ValueError:
            raise Exception("Value Error")










# for font in pygame.font.get_fonts():
#     print(font)
if __name__== "__main__":
    Game()



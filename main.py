import pygame, sys
from paddle import Paddle
from brick import Brick
from ball import Ball
from pygame.math import Vector2
from button import Button
import random


class Game(object):
    def __init__(self):
        #config

        # setup mixer to avoid sound lag
        self.tps_max = 15.0
        colorb=(150,150,150)
        colorb2=(150,150,150)
        self.lvl=1
        self.score = 0
        self.i=0
        self.temp=0
        self.temp2=0




        #inicjalizacja
        pygame.init()
        pygame.mixer.init(44100, -16,2,2048)
        failure=pygame.mixer.Sound("assets/lose.wav")
        hitSound=pygame.mixer.Sound("assets/hit.wav")
        winSound=pygame.mixer.Sound("assets/win.wav")
        menuSong=pygame.mixer.Sound("assets/menu.wav")
        self.bounceSound=pygame.mixer.Sound("assets/bounce.wav")

      #  hitSound = pygame.mixer.Sound("assets/hit.wav")


        font = pygame.font.Font(None, 72)
        font2 = pygame.font.Font(None, 72)
        font3 = pygame.font.Font(None, 45)
        font4 = pygame.font.Font(None, 72)
        font5 = pygame.font.Font(None, 72)

        # nazwa gry
        pygame.display.set_caption("Arcanoid")

        icon = pygame.image.load("assets/rocket.png")
        interface=pygame.image.load("assets/interface.png")
        cosmos=pygame.image.load("assets/cosmos.png")
        pygame.display.set_icon(icon)
        self.screen= pygame.display.set_mode((1280,720))
        self.tps_clock=pygame.time.Clock()
        self.tps_delta= 0.0

        self.player= Paddle(self)
        self.ball=Ball(self, 600,350)
        self.button=Button(440,200,400,100,False)
        self.button2=Button(440,500,400,100,False)

        brick1= Brick(self,404,100)
        brick2= Brick(self,478,100)
        brick3= Brick(self,552,100)
        brick4= Brick(self,441,170)
        brick5 = Brick(self,515,170)
        brick6 = Brick(self, 478, 240)
        brick7 = Brick(self, 480, 25)
        brick8 = Brick(self, 550, 320)
        brick9 = Brick(self, 620, 25)
        brick10 = Brick(self, 690, 320)
        self.list=[]
        for i in range(0,5):
            self.list.append(Brick(self,random.randint(100,400),random.randint(100,400)))






        def collision(ball: Ball, brick: Brick):

            self.screen.blit(brick.draw(), (int(brick.pos.x), int(brick.pos.y)))
            if ball.pos.x > (brick.pos.x-5) and ball.pos.x < (brick.pos.x + 69) and (ball.pos.y > brick.pos.y-10 ) and ball.pos.y< brick.pos.y+74:
                hitSound.play()
                ball.moveY *= -1
                ball.moveX*= -1
                brick.bool = False
                self.score+=1


        def isOver(button: Button, mpos: tuple):
            if mpos[0] > button.pos.x and mpos[0] < button.pos[0] + button.width:
                if mpos[1] > button.pos[1] and mpos[1] < button.pos[1] + button.height:
                    return True
            return False

        def wait(x,y):
            if self.i < 100:
                self.ball.moveX = 0
                self.ball.moveY = 0
                self.i += 1
            elif self.i == 100:
                self.ball.moveX = x
                self.ball.moveY = y
                self.i += 1
                print(self.ball.pos)

        def youlost():
            if self.temp==0:
                failure.play()
                self.temp+=1
            global colorb
            pygame.draw.rect(self.screen, colorb, pygame.Rect(self.button.draw()))
            text3 = font3.render("YOU LOST", 1, (0, 0, 0))
            self.screen.blit(text3, ((int(self.button.pos.x + self.button.width / 2 - text3.get_width() / 2)),
                                     int((self.button.pos.y + self.button.height / 2 - text3.get_height() / 2))))
        def nextlevelbutton(lvl):
            if self.temp2==0:
                winSound.play()
                self.temp2+=1

            global colorb
            self.ball.moveX = 0
            self.ball.moveY = 0
            self.player.moveX = 0
            if lvl <10:
                pygame.draw.rect(self.screen, colorb, pygame.Rect(self.button.draw()))
                text3 = font3.render("DOUBLE CLICK TO LVL "+str(lvl+1), 1, (0, 0, 0))
                self.screen.blit(text3, ((int(self.button.pos.x + self.button.width / 2 - text3.get_width() / 2)),
                                         int((self.button.pos.y + self.button.height / 2 - text3.get_height() / 2))))
            elif lvl == 10:
                pygame.draw.rect(self.screen, colorb, pygame.Rect(self.button.draw()))
                text3 = font3.render("YOU WON!!!!!!!!!!!!", 1, (0, 0, 0))
                self.screen.blit(text3, ((int(self.button.pos.x + self.button.width / 2 - text3.get_width() / 2)),
                                         int((self.button.pos.y + self.button.height / 2 - text3.get_height() / 2))))





        ########################MAIN MENU###############
        def main_menu():
            menuSong.play(-1)

            global colorb
            global colorb2
            self.ball.moveY=0
            self.ball.moveX=0
            self.button2.bool=True
            self.button.bool=True
            while True:
                for event in pygame.event.get():
                    mpos = pygame.mouse.get_pos()
                    if event.type == pygame.MOUSEMOTION:
                        if isOver(self.button, mpos):
                            colorb = (0, 255, 0)
                        else:
                            colorb=(255,0,9)
                        if isOver(self.button2, mpos):
                            colorb2 = (0, 255, 0)
                        else:
                            colorb2 = (255, 0, 0)

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.button.bool == True and isOver(self.button, mpos):
                            self.button.bool=False
                            menuSong.stop()
                            return 0
                        if self.button2.bool == True and isOver(self.button2, mpos):
                            self.button2.bool=False
                            sys.exit(0)

                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        sys.exit(0)
                self.screen.fill((130, 130, 130))
                self.screen.blit(cosmos, (0, 0))
                if self.button.bool==True:
                    pygame.draw.rect(self.screen, colorb, pygame.Rect(self.button.draw()))
                    text4 = font4.render("LETS PLAY", 1, (0, 0, 0))
                    self.screen.blit(text4, ((int(self.button.pos.x + self.button.width / 2 - text4.get_width() / 2)),
                                             int((self.button.pos.y + self.button.height / 2 - text4.get_height() / 2))))
                if self.button2.bool==True:
                    pygame.draw.rect(self.screen, colorb2, pygame.Rect(self.button2.draw()))
                    text5 = font5.render("QUIT", 1, (0, 0, 0))
                    self.screen.blit(text5, ((int(self.button2.pos.x + self.button.width / 2 - text5.get_width() / 2)),
                                             int((self.button2.pos.y + self.button.height / 2 - text5.get_height() / 2))))

                pygame.display.flip()

        def lvl_creator(lvl,a,b,c,d):
            points=self.score
            list=[]
            for i in range(0,a):
                list.append(Brick(self, random.randint(70, 884), random.randint(70, 500)))
            for i in list:
                i.bool=True

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
                        if isOver(self.button, mpos):
                            colorb = (0, 255, 0)
                        elif isOver(self.button, mpos):
                            colorb2 = (0, 255, 0)
                        else:
                            colorb = (255, 0, 0)
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if self.button2.bool == True and isOver(self.button2, mpos):
                            self.button2.bool = False
                            return 0

                        if self.button.bool == True and isOver(self.button, mpos):
                            for i in list:
                                i.bool=True
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
                self.screen.blit(interface, (0, 0))
                for i in list:
                    if i.bool == True:
                        collision(self.ball, i)


                text = font.render(str(self.score), 1, (130, 105, 20))
                text2 = font2.render(str(lvl), 1, (130, 105, 20))
                self.screen.blit(text, (1115, 420))
                self.screen.blit(text2, (1115, 260))
                self.screen.blit(self.ball.draw(), (int(self.ball.pos.x), int(self.ball.pos.y)))
                temp = self.ball.pos.y

                self.draw()
                if temp > 700:
                    self.button.bool = True
                    youlost()

                if self.score == points+a:
                    self.button2.bool = True
                    nextlevelbutton(lvl)

                wait(c,d)
                pygame.display.flip()

        main_menu()
        if main_menu()==0:
            lvl1=lvl_creator(1,1,3,-1,2)
        if lvl1==0:
            lvl2=lvl_creator(2,2,3,-2,1)
        if lvl2==0:
            sys.exit(0)





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











# for font in pygame.font.get_fonts():
#     print(font)
if __name__== "__main__":
    Game()



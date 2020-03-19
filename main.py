import pygame, sys
from paddle import Paddle
from brick import Brick
from ball import Ball
from pygame.math import Vector2
from button import Button
import time

class Game(object):
    def __init__(self):
        #config

        self.tps_max = 15.0
        colorb=(150,150,150)
        colorb2=(150,150,150)
        self.lvl=1
        self.score = 0
        self.i=0





        #inicjalizacja
        pygame.init()
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





        def collision(ball: Ball, brick: Brick):
            self.screen.blit(brick.draw(), (int(brick.pos.x), int(brick.pos.y)))
            if ball.pos.x > (brick.pos.x-5) and ball.pos.x < (brick.pos.x + 69) and (ball.pos.y > brick.pos.y-10 ) and ball.pos.y< brick.pos.y+74:
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
            global colorb
            pygame.draw.rect(self.screen, colorb, pygame.Rect(self.button.draw()))
            text3 = font3.render("YOU LOST", 1, (0, 0, 0))
            self.screen.blit(text3, ((int(self.button.pos.x + self.button.width / 2 - text3.get_width() / 2)),
                                     int((self.button.pos.y + self.button.height / 2 - text3.get_height() / 2))))
        def nextlevelbutton():
            global colorb
            self.ball.moveX = 0
            self.ball.moveY = 0
            self.player.moveX = 0
            pygame.draw.rect(self.screen, colorb, pygame.Rect(self.button.draw()))
            text3 = font3.render("DOUBLE CLICK TO LVL "+str(self.lvl+1), 1, (0, 0, 0))
            self.screen.blit(text3, ((int(self.button.pos.x + self.button.width / 2 - text3.get_width() / 2)),
                                     int((self.button.pos.y + self.button.height / 2 - text3.get_height() / 2))))




        ########################MAIN MENU###############
        def main_menu():
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

        main_menu()
################ LEVEL 1 #########################

        def level1():
            global colorb
            global colorb2
            self.i=0
            self.button = Button(310, 300, 400, 100, False)
            self.button2 = Button(310, 300, 400, 100, False)
            self.ball.pos.x = 500
            self.ball.pos.y = 550
            self.player.moveX=3
            brick7.bool=False
            brick8.bool=False
            brick9.bool=False
            brick10.bool=False

            while True:

                # Handle events
                for event in pygame.event.get():
                    mpos=pygame.mouse.get_pos()
                    if event.type == pygame.QUIT:
                        sys.exit(0)
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        sys.exit(0)
                    elif event.type==pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        self.score+=1
                    elif event.type == pygame.MOUSEMOTION:
                        if isOver(self.button,mpos):
                            colorb=(0,255,0)
                        elif isOver(self.button,mpos):
                            colorb2 = (0, 255, 0)
                        else:
                            colorb=(255,0,0)
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if self.button2.bool == True and isOver(self.button2, mpos):
                            self.button2.bool=False
                            return 0

                        if self.button.bool==True and isOver(self.button, mpos):
                            brick1.bool=True
                            brick2.bool=True
                            brick3.bool=True
                            brick4.bool=True
                            brick5.bool=True
                            brick6.bool=True
                            self.button.bool = False
                            self.ball.moveY = 0
                            self.ball.moveX = 0
                            self.ball.pos.x = 500
                            self.ball.pos.y = 550
                            self.player.pos = Vector2(460, 650)
                            # self.ball.moveX=-1
                            # self.ball.moveY=2
                            self.score=0
                            self.i=0




                 #ticking
                self.tps_delta+=self.tps_clock.tick()/120.0
                while self.tps_delta > 1/ self.tps_max:
                    self.tick()
                    self.tps_delta -= 1/ self.tps_max

                #drawing
                self.screen.fill((130, 130, 130))
                self.screen.blit(interface,(0,0))


                if brick1.bool == True:
                    collision(self.ball, brick1)
                if brick2.bool == True:
                    collision(self.ball, brick2)
                if brick3.bool == True:
                    collision(self.ball, brick3)
                if brick4.bool == True:
                    collision(self.ball, brick4)
                if brick5.bool == True:
                    collision(self.ball, brick5)
                if brick6.bool == True:
                    collision(self.ball, brick6)

                text = font.render(str(self.score), 1, (130, 105, 20))
                text2 = font2.render(str(self.lvl), 1, (130, 105, 20))
                self.screen.blit(text, (1115, 420))
                self.screen.blit(text2, (1115,260))
                self.screen.blit(self.ball.draw(), (int(self.ball.pos.x),int(self.ball.pos.y)))
                temp=self.ball.pos.y


                self.draw()
                if temp>700:
                    self.button.bool = True
                    youlost()

                if self.score==1:
                    self.button2.bool = True
                    nextlevelbutton()


                wait(-1,2)
                pygame.display.flip()

        if main_menu() == 0:
            level1()


##################################LEVEL 2#######################
        def level2():
            global colorb
            self.button = Button(310, 300, 400, 100, False)
            self.button2 = Button(310, 300, 400, 100, False)
            brick1.pos = Vector2(404, 240)
            brick2.pos = Vector2(478, 240)
            brick3.pos = Vector2(552, 240)
            brick6.pos = Vector2(478, 100)
            self.player.pos = Vector2(460, 650)
            brick1.bool = True
            brick2.bool = True
            brick3.bool = True
            brick4.bool = True
            brick5.bool = True
            brick6.bool = True


            self.ball.pos.x = 500
            self.ball.pos.y = 550
            self.button2.bool=False
            self.screen.blit(self.ball.draw(), (int(self.ball.pos.x), int(self.ball.pos.y)))
            self.player.moveX=3
            self.lvl=2
            self.i=0




            while True:
                # Handle events


                for event in pygame.event.get():
                    mpos=pygame.mouse.get_pos()
                    if event.type == pygame.QUIT:
                        sys.exit(0)
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        sys.exit(0)
                    elif event.type==pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        self.score+=1
                    elif event.type == pygame.MOUSEMOTION:
                        if isOver(self.button,mpos):
                            colorb=(0,255,0)
                        else:
                            colorb=(255,0,0)
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if self.button2.bool == True and isOver(self.button2, mpos):
                            return 0
                        if self.button.bool==True and isOver(self.button, mpos):
                            brick1.bool=True
                            brick2.bool=True
                            brick3.bool=True
                            brick4.bool=True
                            brick5.bool=True
                            brick6.bool=True
                            self.button.bool = False
                            self.ball.moveY = 0
                            self.ball.moveX = 0
                            self.ball.pos.x = 500
                            self.ball.pos.y = 550
                            self.player.pos = Vector2(460, 650)
                            # self.ball.moveX=-1
                            # self.ball.moveY=2
                            self.score=0
                            self.i=0

                 #ticking


                self.tps_delta+=self.tps_clock.tick()/120.0
                while self.tps_delta > 1/ self.tps_max:
                    self.tick()
                    self.tps_delta -= 1/ self.tps_max

                #drawing
                self.screen.fill((130, 130, 130))
                self.screen.blit(interface,(0,0))


                if brick1.bool == True:
                    collision(self.ball, brick1)
                if brick2.bool == True:
                    collision(self.ball, brick2)
                if brick3.bool == True:
                    collision(self.ball, brick3)
                if brick4.bool == True:
                    collision(self.ball, brick4)
                if brick5.bool == True:
                    collision(self.ball, brick5)
                if brick6.bool == True:
                    collision(self.ball, brick6)

                text = font.render(str(self.score), 1, (130, 105, 20))
                text2 = font2.render(str(self.lvl), 1, (130, 105, 20))
                self.screen.blit(text, (1115, 420))
                self.screen.blit(text2, (1115,260))
                self.screen.blit(self.ball.draw(), (int(self.ball.pos.x),int(self.ball.pos.y)))

                temp=self.ball.pos.y

                    #self.screen.blit(, (int(self.button.pos.x), int(self.button.pos.y)))
                self.draw()
                if temp>700:
                    self.button.bool=True
                    youlost()
                if self.score==1:
                    self.button2.bool = True
                    nextlevelbutton()

                    #Chwila przerwy przed rozpoczeciem
                wait(-1,2)

                pygame.display.flip()

        if level1() == 0:
            self.score = 0
            level2()

###########LEVEL 3###############
        def level3():
            global colorb
            self.button = Button(310, 300, 400, 100, False)
            self.button2 = Button(310, 300, 400, 100, False)
            self.player.pos = Vector2(460, 650)
            brick7.pos = Vector2(70, 70)
            brick8.pos = Vector2(70, 144)
            brick9.pos = Vector2(890, 70)
            brick10.pos = Vector2(890, 140)
            brick1.bool = True
            brick2.bool = True
            brick3.bool = True
            brick4.bool = True
            brick5.bool = True
            brick6.bool = True
            brick7.bool = True
            brick8.bool = True
            brick9.bool = True
            brick10.bool = True
            self.player.moveX = 3
            self.ball.pos.x = 500
            self.ball.pos.y = 550
            self.button2.bool = False
            self.screen.blit(self.ball.draw(), (int(self.ball.pos.x), int(self.ball.pos.y)))

            self.lvl = 3
            self.i = 0

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
                        else:
                            colorb = (255, 0, 0)
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if self.button2.bool == True and isOver(self.button2, mpos):
                            return 0
                        if self.button.bool == True and isOver(self.button, mpos):
                            brick1.bool = True
                            brick2.bool = True
                            brick3.bool = True
                            brick4.bool = True
                            brick5.bool = True
                            brick6.bool = True
                            brick7.bool = True
                            brick8.bool = True
                            brick9.bool = True
                            brick10.bool = True
                            self.button.bool = False
                            self.ball.moveY = 0
                            self.ball.moveX = 0
                            self.ball.pos.x = 500
                            self.ball.pos.y = 550
                            self.player.pos = Vector2(460, 650)
                            # self.ball.moveX=-1
                            # self.ball.moveY=2

                            self.i = 0

                # ticking

                self.tps_delta += self.tps_clock.tick() / 120.0
                while self.tps_delta > 1 / self.tps_max:
                    self.tick()
                    self.tps_delta -= 1 / self.tps_max

                # drawing
                self.screen.fill((130, 130, 130))
                self.screen.blit(interface, (0, 0))

                if brick1.bool == True:
                    collision(self.ball, brick1)
                if brick2.bool == True:
                    collision(self.ball, brick2)
                if brick3.bool == True:
                    collision(self.ball, brick3)
                if brick4.bool == True:
                    collision(self.ball, brick4)
                if brick5.bool == True:
                    collision(self.ball, brick5)
                if brick6.bool == True:
                    collision(self.ball, brick6)
                if brick7.bool == True:
                    collision(self.ball, brick7)
                if brick8.bool == True:
                    collision(self.ball, brick8)
                if brick9.bool == True:
                    collision(self.ball, brick9)
                if brick10.bool == True:
                    collision(self.ball, brick10)


                text = font.render(str(self.score), 1, (130, 105, 20))
                text2 = font2.render(str(self.lvl), 1, (130, 105, 20))
                self.screen.blit(text, (1115, 420))
                self.screen.blit(text2, (1115, 260))
                self.screen.blit(self.ball.draw(), (int(self.ball.pos.x), int(self.ball.pos.y)))

                temp = self.ball.pos.y

                # self.screen.blit(, (int(self.button.pos.x), int(self.button.pos.y)))
                self.draw()
                if temp > 700:
                    self.button.bool = True
                    youlost()
                if self.score == 1:
                    self.button2.bool = True
                    nextlevelbutton()

                    # Chwila przerwy przed rozpoczeciem
                wait(-2, 1)

                pygame.display.flip()

        if level2() == 0:
            self.score = 0
            level3()
        brick11 = Brick(self, 760, 25)
        brick12 = Brick(self, 830, 320)
        brick13 = Brick(self, 900, 25)
        brick14 = Brick(self, 0, 0)
        brick14.bool = False

####################LEVEL 4 ##########################

        def level4():
            global colorb
            self.button = Button(310, 300, 400, 100, False)
            self.button2 = Button(310, 300, 400, 100, False)
            self.player.pos = Vector2(460, 650)
            brick4.pos=Vector2(330,240)
            brick5.pos=Vector2(626,240)
            brick6.pos=Vector2(478,180)
            brick7.pos = Vector2(330,100 )
            brick8.pos = Vector2(330, 310)
            brick9.pos = Vector2(626, 100)
            brick10.pos = Vector2(626, 310)
            brick11.pos=Vector2(330,170)
            brick12.pos=Vector2(404,170)
            brick13.pos=Vector2(552,170)
            brick14.pos=Vector2(626,170)

            brick1.bool = True
            brick2.bool = True
            brick3.bool = True
            brick4.bool = True
            brick5.bool = True
            brick6.bool = True
            brick7.bool = True
            brick8.bool = True
            brick9.bool = True
            brick10.bool = True
            brick11.bool = True
            brick12.bool = True
            brick13.bool = True
            brick14.bool = True
            self.player.moveX = 3
            self.ball.pos.x = 500
            self.ball.pos.y = 550
            self.button2.bool = False
            self.screen.blit(self.ball.draw(), (int(self.ball.pos.x), int(self.ball.pos.y)))

            self.lvl = 4
            self.i = 0

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
                        else:
                            colorb = (255, 0, 0)
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if self.button2.bool == True and isOver(self.button2, mpos):
                            return 0
                        if self.button.bool == True and isOver(self.button, mpos):
                            brick1.bool = True
                            brick2.bool = True
                            brick3.bool = True
                            brick4.bool = True
                            brick5.bool = True
                            brick6.bool = True
                            brick7.bool = True
                            brick8.bool = True
                            brick9.bool = True
                            brick10.bool = True
                            brick11.bool = True
                            brick12.bool = True
                            brick13.bool = True
                            brick14.bool = True
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

                # ticking

                self.tps_delta += self.tps_clock.tick() / 120.0
                while self.tps_delta > 1 / self.tps_max:
                    self.tick()
                    self.tps_delta -= 1 / self.tps_max

                # drawing
                self.screen.fill((130, 130, 130))
                self.screen.blit(interface, (0, 0))

                if brick1.bool == True:
                    collision(self.ball, brick1)
                if brick2.bool == True:
                    collision(self.ball, brick2)
                if brick3.bool == True:
                    collision(self.ball, brick3)
                if brick4.bool == True:
                    collision(self.ball, brick4)
                if brick5.bool == True:
                    collision(self.ball, brick5)
                if brick6.bool == True:
                    collision(self.ball, brick6)
                if brick7.bool == True:
                    collision(self.ball, brick7)
                if brick8.bool == True:
                    collision(self.ball, brick8)
                if brick9.bool == True:
                    collision(self.ball, brick9)
                if brick10.bool == True:
                    collision(self.ball, brick10)
                if brick11.bool == True:
                    collision(self.ball, brick11)
                if brick12.bool == True:
                    collision(self.ball, brick12)
                if brick13.bool == True:
                    collision(self.ball, brick13)
                if brick14.bool == True:
                    collision(self.ball, brick14)

                text = font.render(str(self.score), 1, (130, 105, 20))
                text2 = font2.render(str(self.lvl), 1, (130, 105, 20))
                self.screen.blit(text, (1115, 420))
                self.screen.blit(text2, (1115, 260))
                self.screen.blit(self.ball.draw(), (int(self.ball.pos.x), int(self.ball.pos.y)))

                temp = self.ball.pos.y

                # self.screen.blit(, (int(self.button.pos.x), int(self.button.pos.y)))
                self.draw()
                if temp > 700:
                    self.button.bool = True
                    youlost()
                if self.score == 1:
                    self.button2.bool = True
                    nextlevelbutton()

                    # Chwila przerwy przed rozpoczeciem
                wait(-2, 1)

                pygame.display.flip()

        if level3()==0:
            self.score = 0
            level4()

        ############ LEVEL 5 ###################

        def level5():
            global colorb
            self.button = Button(310, 300, 400, 100, False)
            self.button2 = Button(310, 300, 400, 100, False)
            self.player.pos = Vector2(460, 650)

            brick1.pos = Vector2(70, 70)
            brick2.pos = Vector2(144, 144)
            brick3.pos = Vector2(218, 218)
            brick4.pos = Vector2(292, 292)
            brick5.pos = Vector2(366, 366)
            brick6.pos = Vector2(480, 200)
            #brick6.pos = Vector2(480, 440)
            brick7.pos = Vector2(594, 366)
            brick8.pos = Vector2(668, 292)
            brick9.pos = Vector2(742, 218)
            brick10.pos = Vector2(816, 144)
            brick11.pos = Vector2(890, 70)
            # brick12.pos = Vector2(480, 366)
            # brick13.pos = Vector2(480, 292)
            # brick14.pos = Vector2(480, 218)

            brick1.bool = True
            brick2.bool = True
            brick3.bool = True
            brick4.bool = True
            brick5.bool = True
            brick6.bool = True
            brick7.bool = True
            brick8.bool = True
            brick9.bool = True
            brick10.bool = True
            brick11.bool = True
            brick12.bool = False
            brick13.bool = False
            brick14.bool = False
            self.player.moveX = 3
            self.ball.pos.x = 500
            self.ball.pos.y = 550
            self.button2.bool = False
            self.screen.blit(self.ball.draw(), (int(self.ball.pos.x), int(self.ball.pos.y)))

            self.lvl = 5
            self.i = 0

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
                        else:
                            colorb = (255, 0, 0)
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if self.button2.bool == True and isOver(self.button2, mpos):
                            return 0
                        if self.button.bool == True and isOver(self.button, mpos):
                            brick1.bool = True
                            brick2.bool = True
                            brick3.bool = True
                            brick4.bool = True
                            brick5.bool = True
                            brick6.bool = True
                            brick7.bool = True
                            brick8.bool = True
                            brick9.bool = True
                            brick10.bool = True
                            brick11.bool = True
                            # brick12.bool = True
                            # brick13.bool = True
                            # brick14.bool = True
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

                # ticking

                self.tps_delta += self.tps_clock.tick() / 120.0
                while self.tps_delta > 1 / self.tps_max:
                    self.tick()
                    self.tps_delta -= 1 / self.tps_max

                # drawing
                self.screen.fill((130, 130, 130))
                self.screen.blit(interface, (0, 0))

                if brick1.bool == True:
                    collision(self.ball, brick1)
                if brick2.bool == True:
                    collision(self.ball, brick2)
                if brick3.bool == True:
                    collision(self.ball, brick3)
                if brick4.bool == True:
                    collision(self.ball, brick4)
                if brick5.bool == True:
                    collision(self.ball, brick5)
                if brick6.bool == True:
                    collision(self.ball, brick6)
                if brick7.bool == True:
                    collision(self.ball, brick7)
                if brick8.bool == True:
                    collision(self.ball, brick8)
                if brick9.bool == True:
                    collision(self.ball, brick9)
                if brick10.bool == True:
                    collision(self.ball, brick10)
                if brick11.bool == True:
                    collision(self.ball, brick11)
                # if brick12.bool == True:
                #     collision(self.ball, brick12)
                # if brick13.bool == True:
                #     collision(self.ball, brick13)
                # if brick14.bool == True:
                #     collision(self.ball, brick14)

                text = font.render(str(self.score), 1, (130, 105, 20))
                text2 = font2.render(str(self.lvl), 1, (130, 105, 20))
                self.screen.blit(text, (1115, 420))
                self.screen.blit(text2, (1115, 260))
                self.screen.blit(self.ball.draw(), (int(self.ball.pos.x), int(self.ball.pos.y)))

                temp = self.ball.pos.y

                # self.screen.blit(, (int(self.button.pos.x), int(self.button.pos.y)))
                self.draw()
                if temp > 700:
                    self.button.bool = True
                    youlost()
                if self.score == 1:
                    self.button2.bool = True
                    nextlevelbutton()

                    # Chwila przerwy przed rozpoczeciem
                wait(-2, 2)

                pygame.display.flip()


        if level4()==0:
            self.score = 0
            level5()

    ##### LEVEL 6 ##############

        def level6():

            global colorb
            self.button = Button(310, 300, 400, 100, False)
            self.button2 = Button(310, 300, 400, 100, False)
            self.player.pos = Vector2(460, 650)

            brick1.pos = Vector2(70, 70)
            brick2.pos = Vector2(144, 144)
            brick3.pos = Vector2(218, 218)
            brick4.pos = Vector2(292, 292)
            brick5.pos = Vector2(366, 366)
            brick6.pos = Vector2(480, 100)
            # brick6.pos = Vector2(420, 440)
            brick7.pos = Vector2(594, 366)
            brick8.pos = Vector2(668, 292)
            brick9.pos = Vector2(742, 218)
            brick10.pos = Vector2(816, 144)
            brick11.pos = Vector2(890, 70)
            brick12.pos = Vector2(480, 366)
            brick13.pos = Vector2(480, 292)
            brick14.pos = Vector2(480, 218)

            brick1.bool = True
            brick2.bool = True
            brick3.bool = True
            brick4.bool = True
            brick5.bool = True
            brick6.bool = True
            brick7.bool = True
            brick8.bool = True
            brick9.bool = True
            brick10.bool = True
            brick11.bool = True
            brick12.bool = True
            brick13.bool = True
            brick14.bool = True
            self.player.moveX = 3
            self.ball.pos.x = 500
            self.ball.pos.y = 550
            self.button2.bool = False
            self.screen.blit(self.ball.draw(), (int(self.ball.pos.x), int(self.ball.pos.y)))

            self.lvl = 6
            self.i = 0


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
                        else:
                            colorb = (255, 0, 0)
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if self.button2.bool == True and isOver(self.button2, mpos):
                            return 0
                        if self.button.bool == True and isOver(self.button, mpos):
                            brick1.bool = True
                            brick2.bool = True
                            brick3.bool = True
                            brick4.bool = True
                            brick5.bool = True
                            brick6.bool = True
                            brick7.bool = True
                            brick8.bool = True
                            brick9.bool = True
                            brick10.bool = True
                            brick11.bool = True
                            brick12.bool = True
                            brick13.bool = True
                            brick14.bool = True
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

                # ticking

                self.tps_delta += self.tps_clock.tick() / 120.0
                while self.tps_delta > 1 / self.tps_max:
                    self.tick()
                    self.tps_delta -= 1 / self.tps_max

                # drawing
                self.screen.fill((130, 130, 130))
                self.screen.blit(interface, (0, 0))

                if brick1.bool == True:
                    collision(self.ball, brick1)
                if brick2.bool == True:
                    collision(self.ball, brick2)
                if brick3.bool == True:
                    collision(self.ball, brick3)
                if brick4.bool == True:
                    collision(self.ball, brick4)
                if brick5.bool == True:
                    collision(self.ball, brick5)
                if brick6.bool == True:
                    collision(self.ball, brick6)
                if brick7.bool == True:
                    collision(self.ball, brick7)
                if brick8.bool == True:
                    collision(self.ball, brick8)
                if brick9.bool == True:
                    collision(self.ball, brick9)
                if brick10.bool == True:
                    collision(self.ball, brick10)
                if brick11.bool == True:
                    collision(self.ball, brick11)
                if brick12.bool == True:
                    collision(self.ball, brick12)
                if brick13.bool == True:
                    collision(self.ball, brick13)
                if brick14.bool == True:
                    collision(self.ball, brick14)

                text = font.render(str(self.score), 1, (130, 105, 20))
                text2 = font2.render(str(self.lvl), 1, (130, 105, 20))
                self.screen.blit(text, (1115, 420))
                self.screen.blit(text2, (1115, 260))
                self.screen.blit(self.ball.draw(), (int(self.ball.pos.x), int(self.ball.pos.y)))

                temp = self.ball.pos.y

                # self.screen.blit(, (int(self.button.pos.x), int(self.button.pos.y)))
                self.draw()
                if temp > 700:
                    self.button.bool = True
                    youlost()
                if self.score == 1:
                    self.button2.bool = True
                    nextlevelbutton()

                    # Chwila przerwy przed rozpoczeciem
                wait(-2, 3)

                pygame.display.flip()

        if level5()==0:
            self.score = 0
            level6()

        ##################LEVEL 7 #################
        brick15 = Brick(self, 0, 0)
        brick16 = Brick(self, 0, 0)
        brick17 = Brick(self, 0, 0)
        brick18 = Brick(self, 0, 0)
        brick19 = Brick(self, 0, 0)
        brick20 = Brick(self, 0, 0)

        def level7():

            global colorb
            self.button = Button(310, 300, 400, 100, False)
            self.button2 = Button(310, 300, 400, 100, False)
            self.player.pos = Vector2(460, 650)

            brick1.pos = Vector2(70, 70)
            brick2.pos = Vector2(144, 70)
            brick3.pos = Vector2(218, 70)
            brick4.pos = Vector2(292, 70)
            brick5.pos = Vector2(366, 70)
            brick6.pos = Vector2(440, 70)
            brick7.pos = Vector2(514, 70)
            brick8.pos = Vector2(588, 70)
            brick9.pos = Vector2(662, 70)
            brick10.pos = Vector2(736, 70)
            brick11.pos = Vector2(810, 70)
            brick12.pos = Vector2(884, 70)
            brick13.pos = Vector2(218, 200)
            brick14.pos = Vector2(292, 200)
            brick15.pos = Vector2(366, 200)
            brick16.pos = Vector2(440, 200)
            brick17.pos = Vector2(514, 200)
            brick18.pos = Vector2(588, 200)
            brick19.pos = Vector2(662, 200)
            brick20.pos = Vector2(736, 200)

            brick1.bool = True
            brick2.bool = True
            brick3.bool = True
            brick4.bool = True
            brick5.bool = True
            brick6.bool = True
            brick7.bool = True
            brick8.bool = True
            brick9.bool = True
            brick10.bool = True
            brick11.bool = True
            brick12.bool = True
            brick13.bool = True
            brick14.bool = True
            brick15.bool = True
            brick16.bool = True
            brick17.bool = True
            brick18.bool = True
            brick19.bool = True
            brick20.bool = True
            self.player.moveX = 4
            self.ball.pos.x = 500
            self.ball.pos.y = 500
            self.button2.bool = False
            self.screen.blit(self.ball.draw(), (int(self.ball.pos.x), int(self.ball.pos.y)))

            self.lvl = 7

            self.i = 0

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
                        else:
                            colorb = (255, 0, 0)
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if self.button2.bool == True and isOver(self.button2, mpos):
                            return 0
                        if self.button.bool == True and isOver(self.button, mpos):
                            brick1.bool = True
                            brick2.bool = True
                            brick3.bool = True
                            brick4.bool = True
                            brick5.bool = True
                            brick6.bool = True
                            brick7.bool = True
                            brick8.bool = True
                            brick9.bool = True
                            brick10.bool = True
                            brick11.bool = True
                            brick12.bool = True
                            brick13.bool = True
                            brick14.bool = True
                            brick15.bool = True
                            brick16.bool = True
                            brick17.bool = True
                            brick18.bool = True
                            brick19.bool = True
                            brick20.bool = True
                            self.button.bool = False
                            self.ball.moveY=0
                            self.ball.moveX=0
                            self.ball.pos.x = 500
                            self.ball.pos.y = 550
                            self.player.pos = Vector2(460, 650)
                            # self.ball.moveX=-1
                            # self.ball.moveY=2
                            self.score = 0
                            self.i = 0

                # ticking

                self.tps_delta += self.tps_clock.tick() / 120.0
                while self.tps_delta > 1 / self.tps_max:
                    self.tick()
                    self.tps_delta -= 1 / self.tps_max

                # drawing
                self.screen.fill((130, 130, 130))
                self.screen.blit(interface, (0, 0))

                if brick1.bool == True:
                    collision(self.ball, brick1)
                if brick2.bool == True:
                    collision(self.ball, brick2)
                if brick3.bool == True:
                    collision(self.ball, brick3)
                if brick4.bool == True:
                    collision(self.ball, brick4)
                if brick5.bool == True:
                    collision(self.ball, brick5)
                if brick6.bool == True:
                    collision(self.ball, brick6)
                if brick7.bool == True:
                    collision(self.ball, brick7)
                if brick8.bool == True:
                    collision(self.ball, brick8)
                if brick9.bool == True:
                    collision(self.ball, brick9)
                if brick10.bool == True:
                    collision(self.ball, brick10)
                if brick11.bool == True:
                    collision(self.ball, brick11)
                if brick12.bool == True:
                    collision(self.ball, brick12)
                if brick13.bool == True:
                    collision(self.ball, brick13)
                if brick14.bool == True:
                    collision(self.ball, brick14)
                if brick15.bool == True:
                    collision(self.ball, brick15)
                if brick16.bool == True:
                    collision(self.ball, brick16)
                if brick17.bool == True:
                    collision(self.ball, brick17)
                if brick18.bool == True:
                    collision(self.ball, brick18)
                if brick19.bool == True:
                    collision(self.ball, brick19)
                if brick20.bool == True:
                    collision(self.ball, brick20)

                text = font.render(str(self.score), 1, (130, 105, 20))
                text2 = font2.render(str(self.lvl), 1, (130, 105, 20))
                self.screen.blit(text, (1115, 420))
                self.screen.blit(text2, (1115, 260))
                self.screen.blit(self.ball.draw(), (int(self.ball.pos.x), int(self.ball.pos.y)))

                temp = self.ball.pos.y

                # self.screen.blit(, (int(self.button.pos.x), int(self.button.pos.y)))
                self.draw()
                if temp > 700:
                    self.button.bool = True
                    youlost()
                if self.score == 1:
                    self.button2.bool = True
                    nextlevelbutton()

                    # Chwila przerwy przed rozpoczeciem
                wait(-2, 3)

                pygame.display.flip()




        if level6()==0:
            self.score = 0
            level7()

        ####LEVEL 8 ####
        brick21 = Brick(self, 0, 0)
        brick22 = Brick(self, 0, 0)
        brick23 = Brick(self, 0, 0)
        brick24 = Brick(self, 0, 0)
        brick25 = Brick(self, 0, 0)
        brick26 = Brick(self, 0, 0)
        brick27 = Brick(self, 0, 0)
        brick28 = Brick(self, 0, 0)
        brick29 = Brick(self, 0, 0)
        brick30 = Brick(self, 0, 0)
        brick31 = Brick(self, 0, 0)
        brick32 = Brick(self, 0, 0)

        def level8():
            global colorb
            self.button = Button(310, 300, 400, 100, False)
            self.button2 = Button(310, 300, 400, 100, False)
            self.player.pos = Vector2(460, 650)

            brick1.pos = Vector2(70, 70)
            brick2.pos = Vector2(144, 70)
            brick3.pos = Vector2(218, 70)
            brick4.pos = Vector2(292, 70)
            brick5.pos = Vector2(366, 70)
            brick6.pos = Vector2(440, 70)
            brick7.pos = Vector2(514, 70)
            brick8.pos = Vector2(588, 70)
            brick9.pos = Vector2(662, 70)
            brick10.pos = Vector2(736, 70)
            brick11.pos = Vector2(810, 70)
            brick12.pos = Vector2(884, 70)
            brick13.pos = Vector2(218, 170)
            brick14.pos = Vector2(292, 170)
            brick15.pos = Vector2(366, 170)
            brick16.pos = Vector2(440, 170)
            brick17.pos = Vector2(514, 170)
            brick18.pos = Vector2(588, 170)
            brick19.pos = Vector2(662, 170)
            brick20.pos = Vector2(736, 170)
            brick21.pos = Vector2(70, 250)
            brick22.pos = Vector2(144, 250)
            brick23.pos = Vector2(218, 250)
            brick24.pos = Vector2(292, 250)
            brick25.pos = Vector2(366, 250)
            brick26.pos = Vector2(440, 250)
            brick27.pos = Vector2(514, 250)
            brick28.pos = Vector2(588, 250)
            brick29.pos = Vector2(662, 250)
            brick30.pos = Vector2(736, 250)
            brick31.pos = Vector2(810, 250)
            brick32.pos = Vector2(884, 250)

            brick1.bool = True
            brick2.bool = True
            brick3.bool = True
            brick4.bool = True
            brick5.bool = True
            brick6.bool = True
            brick7.bool = True
            brick8.bool = True
            brick9.bool = True
            brick10.bool = True
            brick11.bool = True
            brick12.bool = True
            brick13.bool = True
            brick14.bool = True
            brick15.bool = True
            brick16.bool = True
            brick17.bool = True
            brick18.bool = True
            brick19.bool = True
            brick20.bool = True
            brick21.bool = True
            brick22.bool = True
            brick23.bool = True
            brick24.bool = True
            brick25.bool = True
            brick26.bool = True
            brick27.bool = True
            brick28.bool = True
            brick29.bool = True
            brick30.bool = True
            brick31.bool = True
            brick32.bool = True
            self.player.moveX = 4
            self.ball.pos.x = 500
            self.ball.pos.y = 500
            self.button2.bool = False
            self.screen.blit(self.ball.draw(), (int(self.ball.pos.x), int(self.ball.pos.y)))

            self.lvl = 8

            self.i = 0

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
                        else:
                            colorb = (255, 0, 0)
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if self.button2.bool == True and isOver(self.button2, mpos):
                            return 0
                        if self.button.bool == True and isOver(self.button, mpos):
                            brick1.bool = True
                            brick2.bool = True
                            brick3.bool = True
                            brick4.bool = True
                            brick5.bool = True
                            brick6.bool = True
                            brick7.bool = True
                            brick8.bool = True
                            brick9.bool = True
                            brick10.bool = True
                            brick11.bool = True
                            brick12.bool = True
                            brick13.bool = True
                            brick14.bool = True
                            brick15.bool = True
                            brick16.bool = True
                            brick17.bool = True
                            brick18.bool = True
                            brick19.bool = True
                            brick20.bool = True
                            brick21.bool = True
                            brick22.bool = True
                            brick23.bool = True
                            brick24.bool = True
                            brick25.bool = True
                            brick26.bool = True
                            brick27.bool = True
                            brick28.bool = True
                            brick29.bool = True
                            brick30.bool = True
                            brick31.bool = True
                            brick32.bool = True
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

                # ticking

                self.tps_delta += self.tps_clock.tick() / 120.0
                while self.tps_delta > 1 / self.tps_max:
                    self.tick()
                    self.tps_delta -= 1 / self.tps_max

                # drawing
                self.screen.fill((130, 130, 130))
                self.screen.blit(interface, (0, 0))

                if brick1.bool == True:
                    collision(self.ball, brick1)
                if brick2.bool == True:
                    collision(self.ball, brick2)
                if brick3.bool == True:
                    collision(self.ball, brick3)
                if brick4.bool == True:
                    collision(self.ball, brick4)
                if brick5.bool == True:
                    collision(self.ball, brick5)
                if brick6.bool == True:
                    collision(self.ball, brick6)
                if brick7.bool == True:
                    collision(self.ball, brick7)
                if brick8.bool == True:
                    collision(self.ball, brick8)
                if brick9.bool == True:
                    collision(self.ball, brick9)
                if brick10.bool == True:
                    collision(self.ball, brick10)
                if brick11.bool == True:
                    collision(self.ball, brick11)
                if brick12.bool == True:
                    collision(self.ball, brick12)
                if brick13.bool == True:
                    collision(self.ball, brick13)
                if brick14.bool == True:
                    collision(self.ball, brick14)
                if brick15.bool == True:
                    collision(self.ball, brick15)
                if brick16.bool == True:
                    collision(self.ball, brick16)
                if brick17.bool == True:
                    collision(self.ball, brick17)
                if brick18.bool == True:
                    collision(self.ball, brick18)
                if brick19.bool == True:
                    collision(self.ball, brick19)
                if brick20.bool == True:
                    collision(self.ball, brick20)
                if brick21.bool == True:
                    collision(self.ball, brick21)
                if brick22.bool == True:
                    collision(self.ball, brick22)
                if brick23.bool == True:
                    collision(self.ball, brick23)
                if brick24.bool == True:
                    collision(self.ball, brick24)
                if brick25.bool == True:
                    collision(self.ball, brick25)
                if brick26.bool == True:
                    collision(self.ball, brick26)
                if brick27.bool == True:
                    collision(self.ball, brick27)
                if brick28.bool == True:
                    collision(self.ball, brick28)
                if brick29.bool == True:
                    collision(self.ball, brick29)
                if brick30.bool == True:
                    collision(self.ball, brick30)
                if brick31.bool == True:
                    collision(self.ball, brick31)
                if brick32.bool == True:
                    collision(self.ball, brick32)

                text = font.render(str(self.score), 1, (130, 105, 20))
                text2 = font2.render(str(self.lvl), 1, (130, 105, 20))
                self.screen.blit(text, (1115, 420))
                self.screen.blit(text2, (1115, 260))
                self.screen.blit(self.ball.draw(), (int(self.ball.pos.x), int(self.ball.pos.y)))

                temp = self.ball.pos.y

                # self.screen.blit(, (int(self.button.pos.x), int(self.button.pos.y)))
                self.draw()
                if temp > 700:
                    self.button.bool = True
                    youlost()
                if self.score == 1:
                    self.button2.bool = True
                    nextlevelbutton()

                    # Chwila przerwy przed rozpoczeciem
                wait(-3, 3)

                pygame.display.flip()


        if level7()==0:
            self.score = 0
            level8()

        ########## LEVEL 9 ###################

        def level9():
            global colorb
            self.button = Button(310, 300, 400, 100, False)
            self.button2 = Button(310, 300, 400, 100, False)
            self.player.pos = Vector2(460, 650)

            brick1.pos = Vector2(70, 70)
            brick2.pos = Vector2(70, 144)
            brick3.pos = Vector2(70, 218)
            brick4.pos = Vector2(144, 218)
            brick5.pos = Vector2(144, 292)
            brick6.pos = Vector2(144, 366)
            brick7.pos = Vector2(218, 366)
            brick8.pos = Vector2(218, 440)
            brick9.pos = Vector2(218, 514)
            brick10.pos = Vector2(292,514)
            brick11.pos = Vector2(292, 440)
            brick12.pos = Vector2(292, 366)
            brick13.pos = Vector2(366, 366)
            brick14.pos = Vector2(440, 366)
            brick15.pos = Vector2(514, 366)
            brick16.pos = Vector2(514, 292)
            brick17.pos = Vector2(588, 292)
            brick18.pos = Vector2(588, 218)
            brick19.pos = Vector2(662, 218)
            brick20.pos = Vector2(662, 292)
            brick21.pos = Vector2(662, 366)
            brick22.pos = Vector2(736, 366)
            brick23.pos = Vector2(736, 440)
            brick24.pos = Vector2(736, 514)
            brick25.pos = Vector2(810, 514)
            brick26.pos = Vector2(810, 588)
            brick27.pos = Vector2(884, 588)
            brick28.pos = Vector2(884, 514)
            brick29.pos = Vector2(884, 440)
            brick30.pos = Vector2(884, 366)
            brick31.pos = Vector2(884, 292)
            brick32.pos = Vector2(884, 214)

            brick1.bool = True
            brick2.bool = True
            brick3.bool = True
            brick4.bool = True
            brick5.bool = True
            brick6.bool = True
            brick7.bool = True
            brick8.bool = True
            brick9.bool = True
            brick10.bool = True
            brick11.bool = True
            brick12.bool = True
            brick13.bool = True
            brick14.bool = True
            brick15.bool = True
            brick16.bool = True
            brick17.bool = True
            brick18.bool = True
            brick19.bool = True
            brick20.bool = True
            brick21.bool = True
            brick22.bool = True
            brick23.bool = True
            brick24.bool = True
            brick25.bool = True
            brick26.bool = True
            brick27.bool = True
            brick28.bool = True
            brick29.bool = True
            brick30.bool = True
            brick31.bool = True
            brick32.bool = True
            self.player.moveX = 4
            self.ball.pos.x = 500
            self.ball.pos.y = 500
            self.button2.bool = False
            self.screen.blit(self.ball.draw(), (int(self.ball.pos.x), int(self.ball.pos.y)))

            self.lvl = 9

            self.i = 0

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
                        else:
                            colorb = (255, 0, 0)
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if self.button2.bool == True and isOver(self.button2, mpos):
                            return 0
                        if self.button.bool == True and isOver(self.button, mpos):
                            brick1.bool = True
                            brick2.bool = True
                            brick3.bool = True
                            brick4.bool = True
                            brick5.bool = True
                            brick6.bool = True
                            brick7.bool = True
                            brick8.bool = True
                            brick9.bool = True
                            brick10.bool = True
                            brick11.bool = True
                            brick12.bool = True
                            brick13.bool = True
                            brick14.bool = True
                            brick15.bool = True
                            brick16.bool = True
                            brick17.bool = True
                            brick18.bool = True
                            brick19.bool = True
                            brick20.bool = True
                            brick21.bool = True
                            brick22.bool = True
                            brick23.bool = True
                            brick24.bool = True
                            brick25.bool = True
                            brick26.bool = True
                            brick27.bool = True
                            brick28.bool = True
                            brick29.bool = True
                            brick30.bool = True
                            brick31.bool = True
                            brick32.bool = True
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

                # ticking

                self.tps_delta += self.tps_clock.tick() / 120.0
                while self.tps_delta > 1 / self.tps_max:
                    self.tick()
                    self.tps_delta -= 1 / self.tps_max

                # drawing
                self.screen.fill((130, 130, 130))
                self.screen.blit(interface, (0, 0))

                if brick1.bool == True:
                    collision(self.ball, brick1)
                if brick2.bool == True:
                    collision(self.ball, brick2)
                if brick3.bool == True:
                    collision(self.ball, brick3)
                if brick4.bool == True:
                    collision(self.ball, brick4)
                if brick5.bool == True:
                    collision(self.ball, brick5)
                if brick6.bool == True:
                    collision(self.ball, brick6)
                if brick7.bool == True:
                    collision(self.ball, brick7)
                if brick8.bool == True:
                    collision(self.ball, brick8)
                if brick9.bool == True:
                    collision(self.ball, brick9)
                if brick10.bool == True:
                    collision(self.ball, brick10)
                if brick11.bool == True:
                    collision(self.ball, brick11)
                if brick12.bool == True:
                    collision(self.ball, brick12)
                if brick13.bool == True:
                    collision(self.ball, brick13)
                if brick14.bool == True:
                    collision(self.ball, brick14)
                if brick15.bool == True:
                    collision(self.ball, brick15)
                if brick16.bool == True:
                    collision(self.ball, brick16)
                if brick17.bool == True:
                    collision(self.ball, brick17)
                if brick18.bool == True:
                    collision(self.ball, brick18)
                if brick19.bool == True:
                    collision(self.ball, brick19)
                if brick20.bool == True:
                    collision(self.ball, brick20)
                if brick21.bool == True:
                    collision(self.ball, brick21)
                if brick22.bool == True:
                    collision(self.ball, brick22)
                if brick23.bool == True:
                    collision(self.ball, brick23)
                if brick24.bool == True:
                    collision(self.ball, brick24)
                if brick25.bool == True:
                    collision(self.ball, brick25)
                if brick26.bool == True:
                    collision(self.ball, brick26)
                if brick27.bool == True:
                    collision(self.ball, brick27)
                if brick28.bool == True:
                    collision(self.ball, brick28)
                if brick29.bool == True:
                    collision(self.ball, brick29)
                if brick30.bool == True:
                    collision(self.ball, brick30)
                if brick31.bool == True:
                    collision(self.ball, brick31)
                if brick32.bool == True:
                    collision(self.ball, brick32)

                text = font.render(str(self.score), 1, (130, 105, 20))
                text2 = font2.render(str(self.lvl), 1, (130, 105, 20))
                self.screen.blit(text, (1115, 420))
                self.screen.blit(text2, (1115, 260))
                self.screen.blit(self.ball.draw(), (int(self.ball.pos.x), int(self.ball.pos.y)))

                temp = self.ball.pos.y

                # self.screen.blit(, (int(self.button.pos.x), int(self.button.pos.y)))
                self.draw()
                if temp > 700:
                    self.button.bool = True
                    youlost()
                if self.score == 1:
                    self.button2.bool = True
                    nextlevelbutton()

                    # Chwila przerwy przed rozpoczeciem
                wait(-3, 3)

                pygame.display.flip()


        if level8()==0:
            self.score = 0
            level9()


        ######## LEVEL 10 ##########
        




        if level9()==0:
            self.score = 0
            level10()
        else:
            sys.exit(0)



        ##############WYWOLYWANIE GRY############


    def tick(self):
        # checking Inputs

        self.player.tick()
        self.ball.tick()
        if self.ball.pos.x > (self.player.pos.x-5) and self.ball.pos.x < (self.player.pos.x+105) and (self.ball.pos.y>self.player.pos.y-20):
            if self.ball.pos.y<self.player.pos.y+20:
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



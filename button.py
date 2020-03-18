import pygame

from pygame.math import Vector2

class Button(object):
    def __init__(self,x,y,width,height,bool):

        self.bool=bool
        self.pos=Vector2(x,y)
        self.width=width

        self.height=height

    def draw(self):
        button=[int(self.pos.x),int(self.pos.y), int(self.width), int(self.height)]
        return button

        # if self.text!="":
        #     font=pygame.font.SysFont(None,60)
        #     text=font.render(self.text,1,(0,0,0))
        #     self.screen.blit(text, ((self.pos.x+self.width/2 - text.get_width()/2),(self.pos.y+self.height/2 - text.get_height()/2)))







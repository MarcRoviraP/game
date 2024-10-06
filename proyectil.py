import pygame,utils,time
from utils import colores

class Proyectil:
    def __init__(self,x,y):

        self.shape = pygame.Rect(0,0,utils.PROYECTILSIZEX,utils.PROYECTILSIZEY)
        self.shape.center = (x,y)
        self.img = pygame.image.load("assets//img//disparar//municio.png")
        
        
    def draw(self,screen):
        
        #pygame.draw.rect(screen,colores.red,self.shape)
        screen.blit(self.img,self.shape)
        
    def movment(self):
        self.shape.y -= 5
        if self.shape.y <= 0:
            return True
        else:
            return False
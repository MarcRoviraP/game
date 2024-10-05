import pygame,utils
from utils import colores

class Proyectil:
    def __init__(self,x,y):
        self.shape = pygame.Rect(0,0,10,20)
        self.shape.center = (x,y)
        self.shape.y -= 2
        
        
    def draw(self,screen):
        
        pygame.draw.rect(screen,colores.red,self.shape)
        

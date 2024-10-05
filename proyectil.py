import pygame,utils,time
from utils import colores

class Proyectil:
    def __init__(self,x,y):
        print(pygame.time.get_ticks())
        self.shape = pygame.Rect(0,0,utils.PROYECTILSIZEX,utils.PROYECTILSIZEY)
        self.shape.center = (x,y)
        
        
    def draw(self,screen):
        
        pygame.draw.rect(screen,colores.red,self.shape)
        
    def movment(self):
        self.shape.y -= 5
        if self.shape.y <= 0:
            return True
        else:
            return False
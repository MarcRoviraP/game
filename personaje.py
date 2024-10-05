import pygame,utils
from utils import colores

class Personaje:
    def __init__(self,x,y,animacio):
        self.flip = False
        self.animacio = animacio
        
        #Imagen actual de la animacio
        self.frameIndex = 0 
        self.img = animacio[self.frameIndex]
        
        #Temps de la ultima actualitzacio
        self.timeUpdate = pygame.time.get_ticks()
        
        #Crea la figura del jugador
        self.shape = pygame.Rect(0,0,utils.PSIZEX,utils.PSIZEY)
        self.shape.center = (x,y)
        
        
    def draw(self,screen):
        #Invertix en la x la img 
        imagFlip = pygame.transform.flip(self.img,self.flip,False)
        screen.blit(imagFlip,self.shape)
        
        #Vore hitbox
        #pygame.draw.rect(screen,colores.yellow,self.shape,1)
        
    def movment (self, mov_x, mov_y):
        self.shape.x += mov_x
        self.shape.y += mov_y
    
    def update(self):
        cooldown = 100
        self.img = self.animacio[self.frameIndex]
        
        if pygame.time.get_ticks() - self.timeUpdate >= cooldown:
            self.frameIndex += 1
            self.timeUpdate = pygame.time.get_ticks()
            
        if self.frameIndex >= len(self.animacio):
            self.frameIndex = 0
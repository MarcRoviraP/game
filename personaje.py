import pygame,utils
from utils import colores
class Personaje(pygame.sprite.Sprite):
    def __init__(self,x,y,animacio):
        super().__init__()
        self.flip = False
        self.animacio = animacio
        
        #Imagen actual de la animacio
        self.frameIndex = 0 
        self.img = animacio[self.frameIndex]
        
        #Temps de la ultima actualitzacio
        self.timeUpdate = pygame.time.get_ticks()
        
        #Crea la figura del jugador
        self.shape = pygame.Rect(0,0,utils.PSIZEX,utils.PSIZEY)
        
                
        self.rect = self.shape
        self.rect.inflate_ip(9, 9)
        
    def draw(self,screen):
        #Invertix en la x la img cuant es true
        imagFlip = pygame.transform.flip(self.img,self.flip,False)
        screen.blit(imagFlip,self.shape)
        
        #Vore hitbox
        #pygame.draw.rect(screen,colores.yellow,self.shape,1)
        
    def movment (self, mov_x, mov_y):
        self.shape.x += mov_x
        self.shape.y += mov_y
    
    def update(self):
        #Actualiza la animacio del jugador
        cooldown = utils.VELOCITATJOC_COOLDOWN
        self.img = self.animacio[self.frameIndex]
        
        if pygame.time.get_ticks() - self.timeUpdate >= cooldown:
            self.frameIndex += 1
            self.timeUpdate = pygame.time.get_ticks()
            
        if self.frameIndex >= len(self.animacio):
            self.frameIndex = 0
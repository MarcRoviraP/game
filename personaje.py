import pygame,utils
from utils import colores
class Personaje(pygame.sprite.Sprite):
    def __init__(self,x,y,animacio):
        super().__init__()
        self.flip = False
        self.animacio = animacio
        self.health = 100
        self.ultimHit = 0
        
        #Imagen actual de la animacio
        self.frameIndex = 0 
        self.img = animacio[self.frameIndex]
        
        #Temps de la ultima actualitzacio
        self.timeUpdate = pygame.time.get_ticks()
        
        #Crea la figura del jugador
        self.shape = pygame.Rect(x,y,utils.PSIZEX,utils.PSIZEY)
        
                
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
        #Actualizar img

        if self.health in range(0,26):
            self.img = pygame.image.load(f"{utils.rutaIMG}jugador//nave_3.png")
        elif self.health in range(26,51):
            self.img = pygame.image.load(f"{utils.rutaIMG}jugador//nave_2.png")
        elif self.health in range(51,76):
            self.img = pygame.image.load(f"{utils.rutaIMG}jugador//nave_1.png")
    
    def update(self):
        #Actualiza la animacio del jugador
        cooldown = utils.VELOCITATJOC_COOLDOWN
        self.img = self.animacio[self.frameIndex]
        
        if pygame.time.get_ticks() - self.timeUpdate >= cooldown:
            self.frameIndex += 1
            self.timeUpdate = pygame.time.get_ticks()
            
        if self.frameIndex >= len(self.animacio):
            self.frameIndex = 0
        
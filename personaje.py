import pygame,utils
class Personaje(pygame.sprite.Sprite):
    def __init__(self,x,y,animacio):
        super().__init__()
        self.flip = False
        self.animacio = animacio
        self.health = 4
        self.ultimHit = 0
        
        #Imagen actual de la animacio
        self.frameIndex = 0 
        self.img = animacio[self.frameIndex]
        
        #Temps de la ultima actualitzacio
        self.timeUpdate = pygame.time.get_ticks()
        
        #Crea la figura del jugador
        self.shape = pygame.Rect(x,y,utils.PERSONATGESIZEX,utils.PERSONATGESIZEY)
        
                
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
        
        if self.shape.x <= 0:
            self.shape.x = utils.SCREEN_WIDTH
        elif self.shape.x >= utils.SCREEN_WIDTH:
            self.shape.x = 0
        elif self.shape.y <= 0:
            self.shape.y -= mov_y
        elif self.shape.y >= utils.SCREEN_HEIGHT -20:
            self.shape.y -= mov_y
            
        #Actualizar img
        if self.health == 1:
            self.img = pygame.image.load(f"{utils.rutaIMG}jugador/nave_3.png")
        elif self.health == 2:
            self.img = pygame.image.load(f"{utils.rutaIMG}jugador/nave_2.png")
        elif self.health == 3:
            self.img = pygame.image.load(f"{utils.rutaIMG}jugador/nave_1.png")
    
    def update(self):
        #Actualiza la animacio del jugador
        cooldown = utils.VELOCITATJOC_COOLDOWN
        self.img = self.animacio[self.frameIndex]
        
        if pygame.time.get_ticks() - self.timeUpdate >= cooldown:
            self.frameIndex += 1
            self.timeUpdate = pygame.time.get_ticks()
            
        if self.frameIndex >= len(self.animacio):
            self.frameIndex = 0
        
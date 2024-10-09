import pygame,utils

class Proyectil(pygame.sprite.Sprite):
    def __init__(self,x,y,id):
        super().__init__()
        self.id = id
        y -= 30
        self.img = pygame.image.load(f"{utils.rutaIMG}disparar//municio.png")
        self.rect = self.img.get_rect()    
            
        self.rect.topleft = (x, y)
        
        self.shape = self.rect
        self.shape.center = (x,y)
    def __str__(self):
        return f"Proyectil {self.id}"

        
        
    def draw(self,screen):
        
        #pygame.draw.rect(screen,colores.red,self.shape)
        screen.blit(self.img,self.shape)
        #Dibuixar hitbox
        #pygame.draw.rect(screen,utils.colores.azure,self.rect,1)
        
    def movment(self):
        self.shape.y -= (40.0 / utils.PROYECTILCOOLDOWN * 25.0) + 1
        
        return self.shape.y <= 0
       
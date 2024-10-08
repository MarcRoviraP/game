import pygame,utils

class Enemic(pygame.sprite.Sprite):
    def __init__(self,x,y,id):
        super().__init__()
        
        self.id = id
        self.img = pygame.image.load("assets//img//enemic//virus1.png")
        self.rect = self.img.get_rect()        
        self.rect.topleft = (x, y)

        self.shape = self.rect
        self.shape.center = (x,-y)

        self.timeUpdate = pygame.time.get_ticks()
        self.valorX = utils.MOVENEMIC

        #Augmenta el tamany de la hitbox
        self.rect.inflate_ip(15, 15)  
    
    def __str__(self):
        return f"Enemic {self.id}"
                
    def draw(self, screen,juagdor):
            
        #Escalar la img
        self.img = pygame.transform.scale(self.img, (juagdor.shape.width, juagdor.shape.height))        
        screen.blit(self.img, self.shape)
        #Dibuixar hitbox
        #pygame.draw.rect(screen,utils.colores.azure,self.rect,1)
        
    def update(self):
        cooldown = utils.VELOCITATJOC_COOLDOWN

        if pygame.time.get_ticks() - self.timeUpdate > cooldown:
            self.shape.centerx += self.valorX

            # Si toca la paret canvia de direcció
            if self.shape.centerx >= utils.SCREEN_WIDTH - 10 or self.shape.centerx <= 0:
                self.valorX = -self.valorX
                self.shape.centery += abs(self.valorX) * 2

            self.timeUpdate = pygame.time.get_ticks()
        return self.shape.centery >= utils.SCREEN_HEIGHT - 100

import pygame,utils

class Enemic:
    def __init__(self):
        self.img = pygame.image.load("assets//img//enemic//virus1.png")

        self.shape = self.img.get_rect()
        self.shape.center = (10,-10)

        self.timeUpdate = pygame.time.get_ticks()
        self.valorX = utils.MOVENEMIC
                
    def draw(self, screen,juagdor):
            
        #Escalar la img
        self.img = pygame.transform.scale(self.img, (juagdor.shape.width, juagdor.shape.height))        
        screen.blit(self.img, self.shape)
        
    def update(self):
        cooldown = 10
        

        if pygame.time.get_ticks() - self.timeUpdate > cooldown:
            print(self.shape.center)
            self.shape.centerx += self.valorX
            
            #Si toca la paret canvia de direcció
            if self.shape.centerx >= utils.SCREEN_WIDTH-10:
                self.shape.centerx += -self.valorX
                self.shape.centery += (self.valorX * 2)
                self.valorX = -self.valorX
                
            if self.shape.centerx <= 0:
                self.shape.centerx += -self.valorX
                self.shape.centery += (abs(self.valorX) * 2)
                self.valorX = abs(self.valorX)
                
            
            self.timeUpdate = pygame.time.get_ticks()
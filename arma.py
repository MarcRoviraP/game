import pygame,utils

class Arma:
    def __init__(self, animacio):
        self.animacio = animacio
        
        #Frame de la animacion
        self.frameIndex = 0
        self.imgOrig = animacio[self.frameIndex]
        
        #Temps de la ultima actualitzacio
        self.timeUpdate = pygame.time.get_ticks()
        
        
        self.shape = self.imgOrig.get_rect()    
        
        
    def animacioCargarTorreta (self,personaje):
        cooldown = utils.VELOCITATJOC_COOLDOWN
        
        if pygame.time.get_ticks() - self.timeUpdate > cooldown:
            self.frameIndex += 1
            if self.frameIndex >= len(self.animacio):
                self.frameIndex = 0
            self.imgOrig = self.animacio[self.frameIndex]
            self.timeUpdate = pygame.time.get_ticks()
        
        self.update(personaje)
        
    def draw (self,screen):
        screen.blit(self.imgOrig,self.shape)
        
    def update(self,personaje):
        
        self.shape.centerx = personaje.shape.centerx+8
        self.shape.centery = personaje.shape.centery

import pygame,utils

class ProyectilEnemic(pygame.sprite.Sprite):
    def __init__(self, x, y,id):
        super().__init__()
        self.id = id
        self.img = pygame.image.load(f"{utils.rutaIMG}enemic/municio.png")
        self.rect = self.img.get_rect()
        self.rect.topleft = (x, y)
        self.shape = self.rect
        self.shape.center = (x, y)
        
    def __str__(self):
        return f"Proyectil {self.id}"
    
    def draw(self, screen):
        screen.blit(self.img, self.shape)
        #Hitbox
        #pygame.draw.rect(screen, utils.colores.red, self.shape, 1)
        
        
    def movment(self):
        self.shape.y += (40.0 / utils.PROYECTILCOOLDOWN * 25.0) + 1
        
        return self.shape.y >= utils.SCREEN_HEIGHT
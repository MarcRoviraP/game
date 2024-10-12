import math,pygame
#Determina la velocitat del joc
VELOCITATJOC_COOLDOWN = 100

tema = "space"
rutaIMG = f"assets/{tema}/img/"
rutaAudio = f"assets/{tema}/audio/"
rutaFonts = f"assets/{tema}/font/"


SCREEN_WIDTH = 1800
SCREEN_HEIGHT = 480

PERSONATGESIZEX = 20
PERSONATGESIZEY = 20
 
FPS = 60
SPAWN_PLAYERX = SCREEN_WIDTH/2
SPAWN_PLAYERY = SCREEN_HEIGHT-100

PROYECTILSIZEX = 10
PROYECTILSIZEY = 20

PROYECTILCOOLDOWN = VELOCITATJOC_COOLDOWN * 3
VELOCITAT =math.ceil(20 / VELOCITATJOC_COOLDOWN * 25) + 1

MOVENEMIC = 20

randomEnemic = 1000
animacioExplosio = []
for i in range(12):
    img = pygame.image.load(f"{rutaIMG}explosio/explosio_{i}.png")
    #Redimensionar la imatge
    img = pygame.transform.scale(img,(PERSONATGESIZEX+10,PERSONATGESIZEX+10))
    animacioExplosio.append(img)
        
class Explocio(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.frameIndex = 0
        self.img = animacioExplosio[self.frameIndex]
        self.rect = self.img.get_rect()
        self.rect.topleft = (x,y)
        self.timeUpdate = pygame.time.get_ticks()
        self.contUpdate = 0
    
    def draw(self,screen):
        
        if pygame.time.get_ticks() - self.timeUpdate >= VELOCITATJOC_COOLDOWN/2:
            self.frameIndex += 1
            self.timeUpdate = pygame.time.get_ticks()
            self.img = animacioExplosio[self.frameIndex]
            screen.blit(self.img,self.rect)
            self.contUpdate += 1
    
      
    

class colores:
    red = (255, 0, 0)
    blue = (0, 0, 255)
    green = (0, 255, 0)
    white = (255, 255, 255)
    black = (0, 0, 0)
    yellow = (255, 255, 0)
    cyan = (0, 255, 255)
    magenta = (255, 0, 255)
    silver = (192, 192, 192)
    gray = (128, 128, 128)
    maroon = (128, 0, 0)
    olive = (128, 128, 0)
    purple = (128, 0, 128)
    teal = (0, 128, 128)
    navy = (0, 0, 128)
    orange = (255, 165, 0)
    pink = (255, 192, 203)
    brown = (165, 42, 42)
    gold = (255, 215, 0)
    beige = (245, 245, 220)
    ivory = (255, 255, 240)
    wheat = (245, 222, 179)
    tan = (210, 180, 140)
    khaki = (240, 230, 140)
    lavender = (230, 230, 250)
    violet = (238, 130, 238)
    plum = (221, 160, 221)
    orchid = (218, 112, 214)
    turquoise = (64, 224, 208)
    cyan = (0, 255, 255)
    skyblue = (135, 206, 235)
    azure = (240, 255, 255)
    aquamarine = (127, 255, 212)
    mint = (189, 252, 201)
    honeydew = (240, 255, 240)
    lime = (0, 255, 0)
    limegreen = (50, 205, 50)
    forestgreen = (34, 139, 34)
    greenyellow = (173, 255, 47)
    chartreuse = (127, 255, 0)
    lawngreen = (124, 252, 0)
    
backColor = colores.black
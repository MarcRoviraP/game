import pygame,utils
from personaje import Personaje
from proyectil import Proyectil
from utils import colores
from arma import Arma
from enemic import Enemic
    

pygame.init()

#Crea la pantalla en un tamany x,y i li asigna un nom
screen = pygame.display.set_mode((utils.SCREEN_WIDTH, utils.SCREEN_HEIGHT))
pygame.display.set_caption("Mi Juego")


movment_W = False
movment_A = False
movment_S = False
movment_D = False
shoot = False

fps = pygame.time.Clock()
run = True


#Simular animacio tirs

animacioJugador = []


animacioJugador.append(pygame.image.load(f"assets//img//disparar//disparar_{0}.png"))

#Crea un objeto de la clase Personaje
jugador = Personaje(50,50,animacioJugador)

#Crear arma del jugador

animacioTorreta = []

for i in range(1,7):
    animacioTorreta.append(pygame.image.load(f"assets//img//disparar//disparar_{i}.png"))    
    
torreta = Arma(animacioTorreta)

llistaProyectils = []

#Temporizador per als tirs
ultimTir = 0

llistaEnemics = []

grupColisionsEnemy = pygame.sprite.Group()
grupColisionsProyectil = pygame.sprite.Group()

# Genera enemics amb intervals adequats
for i in range(1, 31):
    for j in range(1, 4):
        x_pos = i * 100  # Ajusta l'interval horitzontal
        y_pos = j * 60   # Ajusta l'interval vertical
        enemy = Enemic(x_pos, y_pos)
        llistaEnemics.append(enemy)
        grupColisionsEnemy.add(enemy)
        
while run:
    # Controlar els fps del programa
    fps.tick(utils.FPS)
    screen.fill(colores.black)
    
    #Comprobar colisions entre bales i enemics
    
    colisions = pygame.sprite.groupcollide(grupColisionsProyectil, grupColisionsEnemy, True, True)
    if colisions:
        print("Colision")
    
    # Dibuixar els proyectils
    for proyectil in llistaProyectils:
        if proyectil.movment():
            llistaProyectils.remove(proyectil)
        proyectil.draw(screen)
    
    # Calcular el moviment del jugador
    mov_x = 0
    mov_y = 0
    
    if movment_W:
        mov_y -= utils.VELOCITAT
    if movment_A:
        mov_x -= utils.VELOCITAT
    if movment_S:
        mov_y += utils.VELOCITAT
    if movment_D:
        mov_x += utils.VELOCITAT

    # Moure al jugador
    jugador.movment(mov_x, mov_y)

    # Actualitzar posició de la torreta en cada iteració per seguir al jugador
    torreta.update(jugador)
    
    
    for enemy in llistaEnemics:
        
        if enemy.update():
            llistaEnemics.remove(enemy)
        enemy.draw(screen,jugador)
        
    if shoot:
        # Dibuixar la torreta
        torreta.draw(screen)
        
        # Simular animació de disparar
        torreta.animacioCargarTorreta(jugador)

        # Crear un proyectil si el cooldown ho permet
        if pygame.time.get_ticks() - ultimTir >= utils.PROYECTILCOOLDOWN:
            ultimTir = pygame.time.get_ticks()
            proyectil = Proyectil(jugador.shape.centerx, jugador.shape.centery)
            llistaProyectils.append(proyectil)
            grupColisionsProyectil.add(proyectil)
    
    # Dibuixar el jugador
    jugador.draw(screen)
   
    # Actualitza la pantalla
    pygame.display.update()

    # Detectar els esdeveniments
    for event in pygame.event.get():
        # Si detecta que es tanca la pantalla el programa s'acaba
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                movment_A = True
            if event.key == pygame.K_s:
                movment_S = True
            if event.key == pygame.K_d:
                movment_D = True
            if event.key == pygame.K_w:
                movment_W = True
            if event.key == pygame.K_SPACE:
                shoot = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                movment_A = False
            if event.key == pygame.K_s:
                movment_S = False
            if event.key == pygame.K_d:
                movment_D = False
            if event.key == pygame.K_w:
                movment_W = False
            if event.key == pygame.K_SPACE:
                shoot = False
                jugador.img = pygame.image.load("assets//img//disparar//disparar_0.png")

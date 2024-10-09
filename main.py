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

enemyTimeUpdate = 0
#Simular animacio tirs

animacioJugador = []


animacioJugador.append(pygame.image.load(f"{utils.rutaIMG}disparar//disparar_{0}.png"))

#Crea un objeto de la clase Personaje
jugador = Personaje(200,200,animacioJugador)

#Crear arma del jugador

animacioTorreta = []

for i in range(1,7):
    animacioTorreta.append(pygame.image.load(f"{utils.rutaIMG}disparar//disparar_{i}.png"))    
    
torreta = Arma(animacioTorreta)

llistaProyectils = []

#Temporizador per als tirs
ultimTir = 0

llistaEnemics = []

grupColisionsEnemy = pygame.sprite.Group()
grupColisionsProyectil = pygame.sprite.Group()
colisioJugador = pygame.sprite.GroupSingle()


score = 0


explosions = []

        
while run:
    # Controlar els fps del programa
    fps.tick(utils.FPS)
    screen.fill(colores.black)
    #Crear label score
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, colores.white)
    textRect = text.get_rect()
    textRect.center = (utils.SCREEN_WIDTH // 2, 50)
    textRect.y = 10
    #Dibuixar el text
    screen.blit(text, textRect)
    
    
    #Generar explosions
    for explosion in explosions:
        print(explosions)
        explosion.draw(screen)
        if explosion.contUpdate >= 11:
            explosions.remove(explosion)
    #Spawn mobs
    if enemyTimeUpdate + utils.VELOCITATJOC_COOLDOWN * 4 <= pygame.time.get_ticks():
        enemyTimeUpdate = pygame.time.get_ticks()
        enemy = Enemic(0, 0, pygame.time.get_ticks())  
        llistaEnemics.append(enemy)
        grupColisionsEnemy.add(enemy)
        
    colisioJugador.add(jugador)
    
    # Comprovar colisions entre proyectils i enemics i eliminar-los si hi ha colisio els booleans True indiquen que s'han de borrar
    colisions = pygame.sprite.groupcollide(grupColisionsProyectil, grupColisionsEnemy, True, True)
    
    colisionsEnemiPlayer = pygame.sprite.groupcollide(colisioJugador, grupColisionsEnemy, False, False)
    
    if jugador.ultimHit + utils.VELOCITATJOC_COOLDOWN*3 <= pygame.time.get_ticks():
        if colisionsEnemiPlayer:
            jugador.health -= 25
            jugador.ultimHit = pygame.time.get_ticks()
            jugador.shape.centerx = 200
            jugador.shape.centery = 200
            if jugador.health <= 0:
                run = False
                print("Has perdut")
        
    if colisions:
        #Imprimir la balas que han colisionat
        score += 10
        for proyectil in colisions.keys():
            #Borrar proyectil de la llista
            llistaProyectils.remove(proyectil)
        for enemy in colisions.values():
            #Borrar enemic de la llista
            llistaEnemics.remove(enemy[0])
            
            #Guardar explosions en una llista
            explosion = utils.Explocio(enemy[0].shape.centerx, enemy[0].shape.centery)
            explosions.append(explosion)
                            
    # Dibuixar els proyectils
    for proyectil in llistaProyectils:
        if proyectil.movment():
            llistaProyectils.remove(proyectil)
            grupColisionsProyectil.remove(proyectil)
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
            proyectil = Proyectil(jugador.shape.centerx, jugador.shape.centery, pygame.time.get_ticks())
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
                jugador.img = pygame.image.load(f"{utils.rutaIMG}disparar//disparar_0.png")

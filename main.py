import pygame,utils
from personaje import Personaje
from proyectil import Proyectil
from utils import colores
from arma import Arma
from enemic import Enemic
import time
from proyectilEnemic import ProyectilEnemic
class main():
    def __init__(self):
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
        jugador = Personaje(utils.SPAWN_PLAYERX,utils.SPAWN_PLAYERY,animacioJugador)

        #Crear arma del jugador

        animacioTorreta = []

        for i in range(1,7):
            animacioTorreta.append(pygame.image.load(f"{utils.rutaIMG}disparar//disparar_{i}.png"))    
            
        torreta = Arma(animacioTorreta)

        llistaProyectils = []
        llistaProyectilsEnemics = []
        #Temporizador per als tirs
        ultimTir = 0

        llistaEnemics = []

        #Grups de colisions
        grupColisionsProyectilEnemy = pygame.sprite.Group()
        grupColisionsEnemy = pygame.sprite.Group()
        grupColisionsProyectil = pygame.sprite.Group()
        colisioJugador = pygame.sprite.GroupSingle()


        score = 0


        explosions = []

        #Crear img vides jugador
        imgVides = pygame.image.load(f"{utils.rutaIMG}jugador//vides//vides_4.png")
        while run:

            # Controlar els fps del programa
            fps.tick(utils.FPS)
            screen.fill(utils.backColor)
            
            #Cada 100 punts de score augmenta random enemic
            #Comprobar cada 10 sec
            if pygame.time.get_ticks() % 10000 <= 50:
                
                if utils.randomEnemic > 100:
                    utils.randomEnemic -= score//100
                
            for proyectilEnemic in llistaProyectilsEnemics:
                if proyectilEnemic.movment():
                    llistaProyectilsEnemics.remove(proyectilEnemic)
                    grupColisionsProyectilEnemy.remove(proyectilEnemic)
                proyectilEnemic.draw(screen)
            
            #Generar explosions
            for explosion in explosions:
                explosion.draw(screen)
                if explosion.contUpdate >= 11:
                    explosions.remove(explosion)
            
            #Spawn mobs
            if enemyTimeUpdate + utils.VELOCITATJOC_COOLDOWN * 4 <= pygame.time.get_ticks():
                
                #Audio spawn
                audioSpawn = pygame.mixer.Sound(f"{utils.rutaAudio}spawn.wav")
                #Apujar el volumen del audio 1 = 100%
                audioSpawn.set_volume(1)
                audioSpawn.play()
                
                enemyTimeUpdate = pygame.time.get_ticks()
                enemy = Enemic(0, 0, pygame.time.get_ticks())  
                llistaEnemics.append(enemy)
                grupColisionsEnemy.add(enemy)
                
            colisioJugador.add(jugador)
            
            # Comprovar colisions entre proyectils i enemics i eliminar-los si hi ha colisio els booleans True indiquen que s'han de borrar
            
            #Colisio proyectil enemic
            colisions = pygame.sprite.groupcollide(grupColisionsProyectil, grupColisionsEnemy, True, True)
            
            #Colisio jugador enemic
            colisionsEnemiPlayer = pygame.sprite.groupcollide(colisioJugador, grupColisionsEnemy, False, False)
            
            #Colisio proyectilEnemic jugador
            colisionsProyectilEnemicPlayer = pygame.sprite.groupcollide(grupColisionsProyectilEnemy, colisioJugador, True, False)
            
            if jugador.ultimHit + utils.VELOCITATJOC_COOLDOWN*3 <= pygame.time.get_ticks():
                if colisionsEnemiPlayer or colisionsProyectilEnemicPlayer:
                    jugador.health -= 1
                    imgVides = pygame.image.load(f"{utils.rutaIMG}jugador//vides//vides_{jugador.health}.png")
                    jugador.ultimHit = pygame.time.get_ticks()
                    jugador.shape.centerx = utils.SPAWN_PLAYERX
                    jugador.shape.centery = utils.SPAWN_PLAYERY
                    time.sleep(0.5)
                    if jugador.health <= 0:
                        import ggScreen
                        ggScreen.ggScreen()
                        run = False
                        break
                
            if colisions:
                #Imprimir la balas que han colisionat
                score += 10
                #Audio explocio
                audioExplocio = pygame.mixer.Sound(f"{utils.rutaAudio}explosion.wav")
                audioExplocio.play()
                
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
                if enemy.potDisparar:
                    proyectilEnemic = ProyectilEnemic(enemy.rect.x, enemy.rect.y, pygame.time.get_ticks())
                    grupColisionsProyectilEnemy.add(proyectilEnemic)
                    llistaProyectilsEnemics.append(proyectilEnemic)
                
                enemy.draw(screen,jugador)
                
            if shoot:
                # Dibuixar la torreta
                torreta.draw(screen)
                
                # Simular animació de disparar
                torreta.animacioCargarTorreta(jugador)

                # Crear un proyectil si el cooldown ho permet
                if pygame.time.get_ticks() - ultimTir >= utils.PROYECTILCOOLDOWN:
                    #Audio tirs
                    audioTir = pygame.mixer.Sound(f"{utils.rutaAudio}laser.wav")
                    audioTir.play()
                    ultimTir = pygame.time.get_ticks()
                    proyectil = Proyectil(jugador.shape.centerx, jugador.shape.centery, pygame.time.get_ticks())
                    llistaProyectils.append(proyectil)
                    grupColisionsProyectil.add(proyectil)
            
            # Dibuixar el jugador
            jugador.draw(screen)
        
        
            #Crear label score
            #Carrega font PressStart2P
            
            font = pygame.font.Font(f"{utils.rutaFonts}Press_Start_2P//PressStart2P-Regular.ttf", 30)
            text = font.render(f"Score: {score}", True, colores.white)
            textRect = text.get_rect()
            textRect.center = (utils.SCREEN_WIDTH // 2, 50)
            textRect.y = 10
            #Dibuixar el text
            screen.blit(text, textRect)
            
            #Dibuixa les vides del jugador
            imgVides = pygame.transform.scale(imgVides,(140,20))
            screen.blit(imgVides,(utils.SCREEN_WIDTH - 170,10))
            
            # Actualitza la pantalla
            pygame.display.update()

            # Detectar els esdeveniments
            for event in pygame.event.get():
                # Si detecta que es tanca la pantalla el programa s'acaba
                if event.type == pygame.QUIT:
                    run = False
                    #Eixir del while
                    break 
                

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
    

import pygame,utils

class ventanaInicio():
    def __init__(self):
        pygame.init()

        #Carrega font PressStart2P
        
        font = pygame.font.Font(f"{utils.rutaFonts}Press_Start_2P/PressStart2P-Regular.ttf", 25)


        # Configuración de la pantalla
        screen = pygame.display.set_mode((utils.SCREEN_WIDTH, utils.SCREEN_HEIGHT+200))
        pygame.display.set_caption("Menú de Inicio")

   

        # Botones
        buttons = [
            {"text": "Space Invders", "rect": pygame.Rect((utils.SCREEN_WIDTH/2)-200, 300, 500, 100)},
            {"text": "Moros i Crisitians", "rect": pygame.Rect(utils.SCREEN_WIDTH/2-200, 500, 500, 100)},
        ]

        # Bucle principal
        run = True
        
        while run:
            for event in pygame.event.get():
                if run == False:
                    break
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    for button in buttons:
                        if button["rect"].collidepoint(x, y):
                            
                            if button["text"] == "Space Invders":
                                utils.tema = "space"
                                utils.rutaAudio = f"assets/{utils.tema}/audio/"
                                utils.rutaIMG = f"assets/{utils.tema}/img/"
                                utils.rutaFonts = f"assets/{utils.tema}/font/"
                                utils.backColor = utils.colores.black
                                
                            elif button["text"] == "Moros i Crisitians":

                                utils.tema = "morosicristians"
                                
                                utils.rutaAudio = f"assets/{utils.tema}/audio/"
                                utils.rutaIMG = f"assets/{utils.tema}/img/"
                                utils.rutaFonts = f"assets/{utils.tema}/font/"
                                utils.backColor = utils.colores.khaki
                            import main
                            main.main()
                            run = False
                            #Eixir fora del while
                            break
                            
                        
                        
                        
            if run == False:
                break
            screen.fill(utils.colores.black)

            for button in buttons:
                pygame.draw.rect(screen, utils.colores.white, button["rect"])
                text = font.render(button["text"], True, utils.colores.black)
                text_rect = text.get_rect(center=button["rect"].center)
                screen.blit(text, text_rect)
             #Crear label score
            text = font.render(f"Elegix el tema en el que vols jugar", True, utils.colores.white)
            textRect = text.get_rect()
            textRect.center = (utils.SCREEN_WIDTH // 2, 50)
            textRect.y = 100
            #Dibuixar el text
            screen.blit(text, textRect)
            pygame.display.flip()

        pygame.quit()

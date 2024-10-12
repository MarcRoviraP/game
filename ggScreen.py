import pygame,utils


class ggScreen():    
    def __init__(self,score):
        pygame.init()
        #Carrega font PressStart2P
        
        font = pygame.font.Font(f"{utils.rutaFonts}Press_Start_2P//PressStart2P-Regular.ttf", 30)

        # Configuración de la pantalla
        screen = pygame.display.set_mode((utils.SCREEN_WIDTH, utils.SCREEN_HEIGHT+200))
        pygame.display.set_caption("Buena Partida")


        # Botones
        buttons = [
            {"text": "Eixir", "rect": pygame.Rect((utils.SCREEN_WIDTH/2)-200, 300, 500, 100)},
            {"text": "Tornar a jugar", "rect": pygame.Rect(utils.SCREEN_WIDTH/2-200, 500, 500, 100)},
        ]

        # Bucle principal
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    for button in buttons:
                        if button["rect"].collidepoint(x, y):
                            
                            if button["text"] == "Eixir":
                                run = False
                                
                            elif button["text"] == "Tornar a jugar":
                                import ventanaIncio
                                ventanaIncio.ventanaInicio()
                                run = False
                        
                        
                        
            if run == False:
                break
            screen.fill(utils.colores.black)

            for button in buttons:
                pygame.draw.rect(screen, utils.colores.white, button["rect"])
                text = font.render(button["text"], True, utils.colores.black)
                text_rect = text.get_rect(center=button["rect"].center)
                screen.blit(text, text_rect)

            #Crear label score
            text = font.render(f"Score: {score}", True, utils.colores.white)
            textRect = text.get_rect()
            textRect.center = (utils.SCREEN_WIDTH // 2, 50)
            textRect.y = 100
            #Dibuixar el text
            screen.blit(text, textRect)
            pygame.display.flip()

        pygame.quit()

import pygame,utils,sys


class ggScreen():    
    def __init__(self):
        pygame.init()

        #Crear un menu de inici

        # Configuración de la pantalla
        screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Buena Partida")

        # Fuentes
        font = pygame.font.Font(None, 36)

        # Botones
        buttons = [
            {"text": "Eixir", "rect": pygame.Rect(200, 300, 300, 50)},
            {"text": "Tornar a jugar", "rect": pygame.Rect(200, 400, 300, 50)},
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

            pygame.display.flip()

        pygame.quit()

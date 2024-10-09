import pygame,utils

pygame.init()

#Crear un menu de inici

# Configuración de la pantalla
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Menú de Inicio")

# Fuentes
font = pygame.font.Font(None, 36)

# Botones
buttons = [
    {"text": "Space Invders", "rect": pygame.Rect(200, 300, 300, 50)},
    {"text": "Moros i Crisitians", "rect": pygame.Rect(200, 400, 300, 50)},
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
                    
                    if button["text"] == "Space Invders":
                        utils.tema = "space"
                        utils.rutaAudio = f"assets//{utils.tema}//audio//"
                        utils.rutaIMG = f"assets//{utils.tema}//img//"
                        utils.rutaFonts = f"assets//{utils.tema}//font//"
                        utils.backColor = utils.colores.black
                         
                    elif button["text"] == "Moros i Crisitians":
                        utils.tema = "morosicristians"
                        
                        utils.rutaAudio = f"assets//{utils.tema}//audio//"
                        utils.rutaIMG = f"assets//{utils.tema}//img//"
                        utils.rutaFonts = f"assets//{utils.tema}//font//"
                        utils.backColor = utils.colores.khaki
                    run = False
                    import main
                
                   
                

    screen.fill(utils.colores.black)

    for button in buttons:
        pygame.draw.rect(screen, utils.colores.white, button["rect"])
        text = font.render(button["text"], True, utils.colores.black)
        text_rect = text.get_rect(center=button["rect"].center)
        screen.blit(text, text_rect)

    pygame.display.flip()

pygame.quit()

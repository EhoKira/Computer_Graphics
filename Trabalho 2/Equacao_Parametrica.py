import pygame
import sys
import math

# Configurações da tela
WIDTH, HEIGHT = 800, 800
BG_COLOR = (0, 0, 0)  # Cor de fundo preto
LINE_COLOR = (0,255,255)      # Cor da linha ciano
centrox = WIDTH // 2  # Coordenada x do centro da tela 
centroy = HEIGHT // 2 # Coordenada y do centro da tela
    
def circuloParametrica(screen, raio):
    x  = centrox + raio 
    y = centroy
    for t in range(-1, 360): 
        pygame.draw.rect(screen, LINE_COLOR, pygame.Rect(x, y, 1, 1))
        x = centrox + raio * math.cos((math.pi * t)/180)  
        y = centroy + raio * math.sin((math.pi * t)/180)
        
# -----------------------------------------------------------------------------------------------
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Círculo no Centro")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BG_COLOR)
        circuloParametrica(screen, 300)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()    
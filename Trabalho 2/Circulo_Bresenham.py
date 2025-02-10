import pygame
import sys
import math

# Configurações da tela
WIDTH, HEIGHT = 600, 600
BG_COLOR = (0, 0, 0)  # Cor de fundo preto
LINE_COLOR = (0,255,255)      # Cor da linha ciano
centrox = WIDTH // 2  # Coordenada x do centro da tela 
centroy = HEIGHT // 2 # Coordenada y do centro da tela

# ---------------------------------------------------------------------------------------------
def desenho_pontos_simetricos(screen, xc, yc, x, y):
    pygame.draw.rect(screen, LINE_COLOR, pygame.Rect(xc + x, yc + y, 1, 1))
    pygame.draw.rect(screen, LINE_COLOR, pygame.Rect(xc - x, yc + y, 1, 1))
    pygame.draw.rect(screen, LINE_COLOR, pygame.Rect(xc + x, yc - y, 1, 1))
    pygame.draw.rect(screen, LINE_COLOR, pygame.Rect(xc - x, yc - y, 1, 1))
    pygame.draw.rect(screen, LINE_COLOR, pygame.Rect(xc + y, yc + x, 1, 1))
    pygame.draw.rect(screen, LINE_COLOR, pygame.Rect(xc - y, yc + x, 1, 1))
    pygame.draw.rect(screen, LINE_COLOR, pygame.Rect(xc + y, yc - x, 1, 1))
    pygame.draw.rect(screen, LINE_COLOR, pygame.Rect(xc - y, yc - x, 1, 1))
    
# ---------------------------------------------------------------------------------------------
def desenho_circulo_Bresenham(screen, xc, yc, raio):
    x = 0
    y = raio
    parametro = 1 - raio

    while x <= y:  
        desenho_pontos_simetricos(screen, centrox, centroy, x, y)
        if parametro >= 0:
            y = y - 1
            parametro = parametro + 2 * (x - y) + 5 
        else:
            parametro = parametro + 2 * x + 3
        x = x + 1

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
        desenho_circulo_Bresenham(screen,centrox,centroy,250)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
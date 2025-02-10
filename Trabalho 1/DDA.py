import pygame
import sys

WIDTH, HEIGHT = 650, 650
BG_COLOR = (0, 0, 0)  # Cor de fundo preto
LINE_COLOR = (0,255,255)  # Cor da linha ciano
THICKNESS =1  # Define a espessura da linha

# Função do Algoritmo DDA
def DDA(screen, x1, y1, x2, y2, thickness):
    dx = x2 - x1
    dy = y2 - y1

    if abs(dx) > abs(dy):  # Linha mais horizontal
        if (dx != 0):
            inc = dy / dx
        else: 
            inc = 0
        y = y1
        for x in range(x1, x2 + 1):
            pygame.draw.rect(screen, LINE_COLOR, pygame.Rect(x, HEIGHT - y, thickness, thickness)) 
            y += inc
    else:  # Linha mais vertical
        inc = dx / dy
        x = x1
        for y in range(y1, y2 + 1):
            pygame.draw.rect(screen, LINE_COLOR, pygame.Rect(x, HEIGHT - y, thickness, thickness)) 
            x += inc

# Função principal
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Desenho de Linha DDA - Espessura Ajustável")

    # Coordenadas dos pontos inicial e final da linha
    x1, y1, x2, y2 = 0, 20, 400, 100
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BG_COLOR)
            
        DDA(screen, x1, y1, x2, y2, THICKNESS)
                
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
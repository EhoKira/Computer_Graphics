import pygame
import sys

WIDTH, HEIGHT = 500, 500
BG_COLOR = (255, 255, 255)  # Cor de fundo (branco)
LINE_COLOR = (0, 0, 0)      # Cor da linha (preto)

# Função do Algoritmo Bresenham
def Bresenham(screen, x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    passo = dy > dx

    if passo:
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    error = dx // 2
    y = y1
    ystep = 1 if y1 < y2 else -1

    for x in range(x1, x2 + 1):
        if passo:
            pygame.draw.rect(screen, LINE_COLOR, pygame.Rect(y, HEIGHT - x, 1, 1))
        else:
            pygame.draw.rect(screen, LINE_COLOR, pygame.Rect(x, HEIGHT - y, 1, 1))
        
        error -= dy
        if error < 0:
            y += ystep
            error += dx

# Função principal
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Desenho de Linha Bresenham")

    # Coordenadas dos pontos inicial e final da linha
    x1, y1, x2, y2 = 100, 30,150,80
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BG_COLOR)
            
        Bresenham(screen, x1,y1,x2,y2)
                
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

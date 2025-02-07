import pygame
import sys

WIDTH, HEIGHT = 300, 300
BG_COLOR = (255, 255, 255)  # Cor de fundo (branco)
LINE_COLOR = (0, 0, 0)      # Cor da linha (preto)

# Função do Algoritmo Analítico
def analitico(screen, x1, y1, x2, y2):
    if x1 == x2:
        for y in range(y1, y2 + 1):
            pygame.draw.rect(screen, LINE_COLOR, pygame.Rect(x1, HEIGHT - y, 1, 1))
    else:
        m = (y2 - y1) / (x2 - x1)
        b = y2 - (m * x2)
        for x in range(x1, x2 + 1):
            y = m * x + b
            pygame.draw.rect(screen, LINE_COLOR, pygame.Rect(x, HEIGHT - y, 1, 1))

# Função principal
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Desenho de Linha Analítico")

    # Coordenadas dos pontos inicial e final da linha
    x1, y1, x2, y2 = 10, 80, 10, 220
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BG_COLOR)
            
        analitico(screen, x1,y1,x2,y2)
                
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
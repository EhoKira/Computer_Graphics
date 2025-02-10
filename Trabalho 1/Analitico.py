import pygame
import sys

WIDTH, HEIGHT = 500, 500
BG_COLOR = (0, 0, 0)  # Cor de fundo (branco)
LINE_COLOR = (0,255,255)  # Cor da linha ciano
thickness = 3  # Ajuste aqui para mudar a espessura da linha

# Função do Algoritmo Analítico com Espessura Ajustável
def analitico(screen, x1, y1, x2, y2, thickness=3):
    if x1 == x2:  # Linha vertical
        for y in range(y1, y2 + 1):
            pygame.draw.rect(screen, LINE_COLOR, pygame.Rect(x1 - thickness // 2, HEIGHT - y, thickness, thickness))
    else:
        m = (y2 - y1) / (x2 - x1)
        b = y2 - (m * x2)
        for x in range(x1, x2 + 1):
            y = m * x + b
            pygame.draw.rect(screen, LINE_COLOR, pygame.Rect(x - thickness // 2, HEIGHT - y - thickness // 2, thickness, thickness))

# Função principal
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Desenho de Linha Analítico")

    # Coordenadas dos pontos inicial e final da linha
    x1, y1, x2, y2 = 50, 40, 400, 180 # x1, y1, x2, y2 = 10, 40, 100, 80
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BG_COLOR)
        analitico(screen, x1, y1, x2, y2, thickness)  # Passa a espessura como parâmetro
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
# import pygame
# import sys

# WIDTH, HEIGHT = 500, 500
# BG_COLOR = (0, 0, 0)  # Cor de fundo preto
# LINE_COLOR = (0,255,255)      # Cor da linha ciano
# THICKNESS = 1  # Define a espessura da linha

# # Função do Algoritmo Bresenham
# def Bresenham(screen, x1, y1, x2, y2, thickness):
#     # Calcula as diferenças absolutas entre as coordenadas dos pontos
#     dx = abs(x2 - x1)
#     dy = abs(y2 - y1)
#     # Determina se a linha tem uma inclinação maior que 45º
#     passo = dy > dx
    
#     # Se for uma linha mais inclinada verticalmente, trocamos x e y
#     if passo:
#         x1, y1 = y1, x1
#         x2, y2 = y2, x2
#     # Garante que estamos sempre desenhando da esquerda para a direita
#     if x1 > x2:
#         x1, x2 = x2, x1
#         y1, y2 = y2, y1
#     # Recalcula as diferenças após possíveis trocas
#     dx = abs(x2 - x1)
#     dy = abs(y2 - y1)
    
#     # Define a variável de erro inicial
#     error = dx // 2
    
#     # Define o sentido do crescimento de y
#     y = y1
#     ystep = 1 if y1 < y2 else -1

#     for x in range(x1, x2 + 1):
#          # Se a linha era "passo", significa que trocamos x e y antes, então devemos inverter de volta
#         if passo:
#             pygame.draw.rect(screen, LINE_COLOR, pygame.Rect(y - thickness // 2, HEIGHT - x - thickness // 2, thickness, thickness))
#         else:
#             pygame.draw.rect(screen, LINE_COLOR, pygame.Rect(x - thickness // 2, HEIGHT - y - thickness // 2, thickness, thickness))
        
#         # Atualiza o erro acumulado
#         error -= dy
#         if error < 0:
#             y += ystep
#             error += dx  # Ajuste do erro acumulado

# # Função principal
# def main():
#     pygame.init()
#     screen = pygame.display.set_mode((WIDTH, HEIGHT))
#     pygame.display.set_caption("Desenho de Linha Bresenham")

#     # Coordenadas dos pontos inicial e final da linha
#     x1, y1, x2, y2 = 0, 40, 100, 400
    
#     running = True
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False

#         screen.fill(BG_COLOR)
            
#         Bresenham(screen, x1,y1,x2,y2, THICKNESS)
                
#         pygame.display.flip()

#     pygame.quit()
#     sys.exit()

# if __name__ == "__main__":
#     main()


import pygame
import sys

WIDTH, HEIGHT = 650, 650
BG_COLOR = (0, 0, 0)  # Cor de fundo preto
LINE_COLOR = (0, 255, 255)  # Cor da linha ciano
THICKNESS = 1  # Espessura da linha

# Implementação correta do Algoritmo de Bresenham
def Bresenham(screen, x1, y1, x2, y2, thickness):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    
    p = 2 * dy - dx  # Parâmetro de decisão inicial

    x, y = x1, y1

    # Desenha o primeiro pixel
    pygame.draw.rect(screen, LINE_COLOR, pygame.Rect(x, HEIGHT - y, thickness, thickness))

    while x != x2 or y != y2:
        if p >= 0:
            y += sy
            p -= 2 * dx
        x += sx
        p += 2 * dy

        # Desenha o pixel calculado
        pygame.draw.rect(screen, LINE_COLOR, pygame.Rect(x, HEIGHT - y, thickness, thickness))

# Função principal
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Desenho de Linha Bresenham")

    # Coordenadas dos pontos inicial e final da linha
    x1, y1, x2, y2 = 0, 20, 400, 100

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BG_COLOR)
        Bresenham(screen, x1, y1, x2, y2, THICKNESS)
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
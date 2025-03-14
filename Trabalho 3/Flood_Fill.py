import pygame
import sys
import time
from collections import deque

# Função para desenhar uma linha usando o algoritmo de Bresenham
def draw_line(surface, x0, y0, x1, y1, color):
    dx = abs(x1 - x0)  # Diferença absoluta entre as coordenadas x
    dy = abs(y1 - y0)  # Diferença absoluta entre as coordenadas y
    
    sx = 1 if x0 < x1 else -1  # Direção do deslocamento horizontal
    sy = 1 if y0 < y1 else -1  # Direção do deslocamento vertical
    
    err = dx - dy  # Erro inicial para o algoritmo

    while True:
        if 0 <= x0 < surface.get_width() and 0 <= y0 < surface.get_height():
            surface.set_at((x0, y0), color)  # Define a cor do pixel na posição (x0, y0)
        pygame.display.flip()
        time.sleep(0.002)
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x0 += sx  # Move no eixo x
        if e2 < dx:
            err += dx
            y0 += sy  # Move no eixo y

# Função para desenhar um polígono conectando pontos com linhas de Bresenham
def draw_polygon(surface, points, color):
    for i in range(len(points)):
        x0, y0 = points[i]
        x1, y1 = points[(i + 1) % len(points)]  # Conecta o último ponto ao primeiro
        draw_line(surface, x0, y0, x1, y1, color)

# Algoritmo de Bresenham para desenhar um círculo
def draw_circle_bresenham(surface, xc, yc, r, color):
    x, y = 0, r
    d = 3 - (2 * r)  # Parâmetro inicial da equação do círculo

    # Função auxiliar para plotar os pontos simétricos do círculo
    def plot_circle_points(xc, yc, x, y):
        points = [(xc + x, yc + y), (xc - x, yc + y),
                  (xc + x, yc - y), (xc - x, yc - y),
                  (xc + y, yc + x), (xc - y, yc + x),
                  (xc + y, yc - x), (xc - y, yc - x)]
        for point in points:
            if 0 <= point[0] < surface.get_width() and 0 <= point[1] < surface.get_height():
                surface.set_at(point, color)
        pygame.display.flip()
        time.sleep(0.002)

    plot_circle_points(xc, yc, x, y)  # Plota os primeiros pontos

    while y >= x:
        x += 1
        if d > 0:
            y -= 1
            d = d + (4 * (x - y)) + 10
        else:
            d = d + (4 * x) + 6
        plot_circle_points(xc, yc, x, y)  # Atualiza a visualização

# Função para desenhar um retângulo usando o algoritmo de Bresenham
def draw_rectangle_bresenham(surface, x1, y1, width, height, color):
    draw_polygon(surface, [(x1, y1), (x1 + width, y1), (x1 + width, y1 + height), (x1, y1 + height)], color)

# Função para desenhar um polígono específico (Figura C)
def draw_figure_c(surface, color):
    center_x, center_y = 300, 300  # Define o centro do polígono
    scale = 5

    # Lista de pontos do polígono
    points_c = [
        (center_x + scale * -20, center_y + scale * -15),
        (center_x + scale * 5, center_y + scale * -25),
        (center_x + scale * 30, center_y + scale * -5),
        (center_x + scale * 26, center_y + scale * 5),
        (center_x + scale * -10, center_y + scale * 10),
        (center_x + scale * -5, center_y + scale * -2)
    ]

    draw_polygon(surface, points_c, color)
    return points_c

# Função para desenhar um polígono específico (Figura D)
def draw_figure_d(surface, color):
    center_x, center_y = 300, 300  # Define o centro do polígono
    scale = 5

    # Lista de pontos do polígono
    points_d = [
        (center_x + scale * -15, center_y + scale * -15),
        (center_x + scale * 0, center_y + scale * -15),
        (center_x + scale * 8, center_y + scale * -8),
        (center_x + scale * 15, center_y + scale * -15),
        (center_x + scale * 30, center_y + scale * -15),
        (center_x + scale * 30, center_y + scale * 0),
        (center_x + scale * 8, center_y + scale * 13),
        (center_x + scale * -15, center_y + scale * 0)
    ]

    draw_polygon(surface, points_d, color)
    return points_d

# Algoritmo de preenchimento Flood Fill
def flood_fill(surface, x, y, fill_color, border_color):
    queue = deque([(x, y)])  # Fila de pontos a serem preenchidos
    target_color = surface.get_at((x, y))

    if target_color == fill_color or target_color == border_color:
        return

    while queue:
        x, y = queue.popleft()
        if surface.get_at((x, y)) != target_color:
            continue

        surface.set_at((x, y), fill_color)
        pygame.display.flip()
        time.sleep(0.000001)

        # Adiciona os vizinhos à fila
        queue.append((x + 1, y))
        queue.append((x - 1, y))
        queue.append((x, y + 1))
        queue.append((x, y - 1))

# Função principal
def main():
    pygame.init()
    screen = pygame.display.set_mode((700, 700))
    pygame.display.set_caption("Flood Fill com Bresenham - Polígonos")
    screen.fill((255,255,255))

    shape = "d"  # Escolha da figura ("a" para círculo, "b" para retângulo, "c" para polígono C, "d" para polígono D)

    if shape == "a":
        draw_circle_bresenham(screen, 350, 350, 100, (0, 0, 0))
    elif shape == "b":
        draw_rectangle_bresenham(screen, 250, 250, 200, 100, (0, 0, 0))
    elif shape == "c":
        points_c = draw_figure_c(screen, (0, 0, 0))
    elif shape == "d":
        points_d = draw_figure_d(screen, (0, 0, 0))

    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                flood_fill(screen, x, y, (0,255,255), (0, 0, 0))

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
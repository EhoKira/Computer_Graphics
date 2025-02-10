import pygame
import sys
import time
import math

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
        if x0 == x1 and y0 == y1:  # Se o ponto inicial chegou ao destino, para o loop
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

# Algoritmo de preenchimento Scanline
def scanline_fill(surface, points, fill_color):
    edges = []
    min_y = min(points, key=lambda p: p[1])[1]  # Encontra a menor coordenada Y
    max_y = max(points, key=lambda p: p[1])[1]  # Encontra a maior coordenada Y

    # Determina as arestas do polígono
    for i in range(len(points)):
        x0, y0 = points[i]
        x1, y1 = points[(i + 1) % len(points)]
        if y0 != y1:  # Evita arestas horizontais
            if y0 > y1:
                x0, y0, x1, y1 = x1, y1, x0, y0  # Garante que y0 < y1
            edges.append((y0, y1, x0, (x1 - x0) / (y1 - y0)))  # Salva os coeficientes

    edges.sort()

    for y in range(min_y, max_y + 1):
        active_edges = []
        for edge in edges:
            if edge[0] <= y < edge[1]:  # Se a linha atual estiver dentro da aresta
                active_edges.append(edge[2] + (y - edge[0]) * edge[3])

        active_edges.sort()

        for i in range(0, len(active_edges), 2):  # Percorre pares de pontos
            x_start = math.ceil(active_edges[i])
            x_end = math.floor(active_edges[i + 1])
            for x in range(x_start, x_end + 1):
                surface.set_at((x, y), fill_color)  # Preenche a linha horizontal
        pygame.display.flip()
        time.sleep(0.002)

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

    plot_circle_points(xc, yc, x, y)

    while y >= x:
        x += 1
        if d > 0:
            y -= 1
            d = d + (4 * (x - y)) + 10
        else:
            d = d + (4 * x) + 6
        plot_circle_points(xc, yc, x, y)

# Algoritmo Scanline para preencher um círculo
def scanline_fill_circle(surface, xc, yc, r, fill_color):
    for y in range(yc - r, yc + r + 1):
        dx = int(math.sqrt(r ** 2 - (y - yc) ** 2))
        x_start = xc - dx
        x_end = xc + dx
        for x in range(x_start, x_end + 1):
            surface.set_at((x, y), fill_color)
        pygame.display.flip()
        time.sleep(0.002)

# Função para desenhar a Figura C
def draw_figure_c(surface, color):
    center_x, center_y = 350, 350  
    scale = 5

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

# Função para desenhar a Figura D
def draw_figure_d(surface, color):
    center_x, center_y = 300, 300  
    scale = 5 

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

# Função principal
def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 800))  
    pygame.display.set_caption("Varredura com Análise Geométrica")
    screen.fill((255, 255, 255))  

    shape = "c"  # Escolha da figura ("a" para círculo, "b" para retângulo, "c" para polígono C, "d" para polígono D)

    if shape == "a":
        draw_circle_bresenham(screen, 250, 250, 100, (0, 0, 0))
        scanline_fill_circle(screen, 250, 250, 100, (255, 255, 0))
    elif shape == "b":
        points_b = [(150, 150), (350, 150), (350, 250), (150, 250)]
        draw_polygon(screen, points_b, (0, 0, 0))
        scanline_fill(screen, points_b, (0,255,255))
    elif shape == "c":
        points_c = draw_figure_c(screen, (0, 0, 0))
        scanline_fill(screen, points_c, (0, 255, 0))
    elif shape == "d":
        points_d = draw_figure_d(screen, (0, 0, 0))
        scanline_fill(screen, points_d, (254, 156, 0))

    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()  

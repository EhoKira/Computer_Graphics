import matplotlib.pyplot as plt

# Função para verificar se um ponto está dentro de uma borda
def inside(p, edge):
    x, y = p
    edge_type, edge_value = edge
    if edge_type == "left":
        return x >= edge_value
    elif edge_type == "right":
        return x <= edge_value
    elif edge_type == "bottom":
        return y >= edge_value
    elif edge_type == "top":
        return y <= edge_value
    return False

# Função para calcular a interseção de um segmento com a borda
def intersection(p1, p2, edge):
    x1, y1 = p1
    x2, y2 = p2
    edge_type, edge_value = edge

    if edge_type in ["left", "right"]:
        x = edge_value
        y = y1 + (y2 - y1) * (x - x1) / (x2 - x1)
    else:
        y = edge_value
        x = x1 + (x2 - x1) * (y - y1) / (y2 - y1)

    return (x, y)

# Algoritmo de recorte Sutherland-Hodgman
def sutherland_hodgman_clip(polygon, clip_window):
    clipped_polygon = polygon

    for edge in clip_window:
        new_polygon = []
        for i in range(len(clipped_polygon)):
            current_point = clipped_polygon[i]
            prev_point = clipped_polygon[i - 1]

            current_inside = inside(current_point, edge)
            prev_inside = inside(prev_point, edge)

            if prev_inside and current_inside:
                new_polygon.append(current_point)
            elif prev_inside and not current_inside:
                new_polygon.append(intersection(prev_point, current_point, edge))
            elif not prev_inside and current_inside:
                new_polygon.append(intersection(prev_point, current_point, edge))
                new_polygon.append(current_point)

        clipped_polygon = new_polygon

    return clipped_polygon

# Definição dos polígonos para os testes
polygons = {
    "Retângulo": [(-1, 2), (1, 2), (1, 0.5), (0.5, 0.5), (0.5, 1.25), (-0.5, 1.25), (-0.5, 0.5), (-1, 0.5)],
    "Triangular Inclinado": [(-0.5, 2), (1.5, -0.5), (-0.5, -0.5)],
    "Cruz": [(-0.5, 0), (0.5, 0), (0.5, -0.5), (1, -0.5), (1, -1.5), (0.5, -1.5), (0.5, -2), (-0.5, -2), (-0.5, -1.5), (-1, -1.5), (-1, -0.5), (-0.5, -0.5)],
    "Pentágono": [(-1.5, -0.5), (-2, 0.5), (-1, 1.5), (0, 0.5), (-0.5, -0.5)]
}

# Definição da janela de recorte [Xmin, Xmax, Ymin, Ymax]
clip_window = [("left", -1), ("right", 1), ("bottom", -1), ("top", 1)]

# Criar gráfico com subplots
fig, axes = plt.subplots(2, 2, figsize=(10, 10))
axes = axes.flatten()

for ax, (name, polygon) in zip(axes, polygons.items()):
    # Aplicar recorte
    clipped_polygon = sutherland_hodgman_clip(polygon, clip_window)

    # Desenhar a janela de recorte
    window_x = [-1, 1, 1, -1, -1]
    window_y = [-1, -1, 1, 1, -1]
    ax.plot(window_x, window_y, 'r-', label="Janela de Recorte")

    # Desenhar o polígono original
    polygon_x, polygon_y = zip(*polygon + [polygon[0]])
    ax.fill(polygon_x, polygon_y, 'b', alpha=0.3, label="Polígono Original")

    # Desenhar o polígono recortado
    if clipped_polygon:
        clipped_x, clipped_y = zip(*clipped_polygon + [clipped_polygon[0]])
        ax.fill(clipped_x, clipped_y, 'g', alpha=0.6, label="Polígono Recortado")

    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_title(name)
    ax.legend()
    ax.grid(True)

# Ajustar layout e exibir
plt.tight_layout()
plt.show()

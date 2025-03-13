import numpy as np
import matplotlib.pyplot as plt
import scipy.special  # Para calcular o binômio de Newton

# Função para calcular os polinômios de Bernstein
def bernstein(n, i, t):
    return scipy.special.comb(n, i) * (t ** i) * ((1 - t) ** (n - i))

# Função para subdividir os pontos de controle
def subdivide_curve(points):
    M01 = (points[0] + points[1]) / 2
    M12 = (points[1] + points[2]) / 2
    M23 = (points[2] + points[3]) / 2

    M012 = (M01 + M12) / 2
    M123 = (M12 + M23) / 2

    M0123 = (M012 + M123) / 2

    first_half = [points[0], M01, M012, M0123]
    second_half = [M0123, M123, M23, points[3]]

    return first_half, second_half, M0123

# Função para calcular a curva de Bézier usando a equação paramétrica
def bezier_curve(points, num_points=100):
    n = len(points) - 1
    t_values = np.linspace(0, 1, num_points)
    curve = np.zeros((num_points, 2))

    for i in range(n + 1):
        curve += np.outer(bernstein(n, i, t_values), points[i])

    return curve

# Função recursiva para calcular a curva de Bézier usando o algoritmo de Casteljau
def casteljau(points, t=0.005):
    curve_points = []
    
    def recursive_subdivision(ctrl_points):
        p0, p3 = ctrl_points[0], ctrl_points[-1]
        dist = np.linalg.norm(p3 - p0)

        if dist > t:
            first_half, second_half, midpoint = subdivide_curve(ctrl_points)
            recursive_subdivision(first_half)
            recursive_subdivision(second_half)
        else:
            curve_points.append(ctrl_points[-1])

    recursive_subdivision(points)
    return np.array(curve_points)

# Pontos de controle
control_points = np.array([[0, 0], [1, 3], [3, 3], [4, 0]])
control_points_2 = np.array([[0, 0], [1, 3], [3, 3], [4, 0]])

# Geração das curvas
curve_parametric = bezier_curve(control_points)
curve_casteljau = casteljau(control_points_2)

# Plot das curvas
plt.figure(figsize=(8, 6))

# Curva pela equação paramétrica
plt.plot(curve_parametric[:, 0], curve_parametric[:, 1], label="Bézier Paramétrica", linestyle="--")

# Curva pelo algoritmo de Casteljau
plt.plot(curve_casteljau[:, 0], curve_casteljau[:, 1], label="Bézier Casteljau", linestyle="-")

# Pontos de controle
plt.plot(control_points[:, 0], control_points[:, 1], "ro-", label="Pontos de Controle")

plt.legend()
plt.title("Curvas de Bézier - Equação Paramétrica vs Casteljau")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid()
plt.show()
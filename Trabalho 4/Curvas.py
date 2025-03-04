import numpy as np
import matplotlib.pyplot as plt
import scipy.special  # Para calcular o binômio de Newton

# Função para calcular os polinômios de Bernstein
def bernstein(n, i, t):
    return scipy.special.comb(n, i) * (t ** i) * ((1 - t) ** (n - i))

# Função para calcular a curva de Bézier usando a equação paramétrica
def bezier_curve(points, num_points=100):
    n = len(points) - 1
    t_values = np.linspace(0, 1, num_points)
    curve = np.zeros((num_points, 2))

    for i in range(n + 1):
        curve += np.outer(bernstein(n, i, t_values), points[i])

    return curve

# Função recursiva para calcular a curva de Bézier usando o algoritmo de Casteljau
def casteljau(points, t):
    if len(points) == 1:
        return points[0]
    
    new_points = [(1 - t) * points[i] + t * points[i + 1] for i in range(len(points) - 1)]
    return casteljau(new_points, t)

# Função para gerar pontos da curva de Bézier via Casteljau
def bezier_casteljau(points, num_points=100):
    t_values = np.linspace(0, 1, num_points)
    return np.array([casteljau(points, t) for t in t_values])

# Pontos de controle
control_points = np.array([[0, 0], [1, 3], [3, 3], [4, 0]])
control_points_2 = np.array([[0, 0], [1, 3.5], [3, 3.5], [4, 0]])

# Geração das curvas
curve_parametric = bezier_curve(control_points)
curve_casteljau = bezier_casteljau(control_points_2)

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
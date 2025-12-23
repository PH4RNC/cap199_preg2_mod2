
import numpy as np
import matplotlib.pyplot as plt

# Función
def f(x):
    return np.sin(x)

# Derivada de f(x)
def df(x):
    return np.cos(x)

# Puntos de las tangentes
points = [0, np.pi / 4, np.pi / 2, np.pi, 3 * np.pi / 2]
colors = ['red', 'green', 'blue', 'purple', 'cyan']
labels = ['Tangente en x = 0', 'Tangente en x = π/4', 'Tangente en x = π/2', 'Tangente en x = π', 'Tangente en x = 3π/2']

# Rango de valores de x
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
y = f(x)

# Gráfica
plt.figure(figsize=(12, 6))
plt.plot(x, y, label='f(x) = sin(x)', color='black', linewidth=2)

# Grafica de las rectas tangentes
for point, color, label in zip(points, colors, labels):
    y_point = f(point)
    slope = df(point)
    # Longitud de la recta tangente
    x_tangent = np.array([point - 1, point + 1])
    y_tangent = slope * (x_tangent - point) + y_point

    plt.plot(x_tangent, y_tangent, color=color, label=label, linewidth=2)
    plt.scatter(point, y_point, color=color, s=80)  # Punto de tangente

# Ajuste de los límites de los ejes
plt.xlim(-0.5, 6.25)
plt.ylim(-1.25, 1.5)

plt.title('Rectas tangentes a f(x) = sin(x)', fontweight='bold')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.legend(fontsize='x-small')
plt.show()

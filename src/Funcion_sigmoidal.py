import numpy as np
import matplotlib.pyplot as plt

# Definición de la función sigmoid
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Función para graficar la sigmoid
def plot_sigmoid():
    # Generar datos para graficar la función sigmoid
    x_values = np.linspace(-10, 10, 100)
    y_values = sigmoid(x_values)

    # Graficar la función sigmoid
    plt.plot(x_values, y_values, label="Sigmoid")
    plt.title("Función de Activación Sigmoid")
    plt.xlabel("x")
    plt.ylabel("sigmoid(x)")
    plt.grid(True)
    plt.legend()
    plt.show()

import matplotlib.pyplot as plt
from src import graficar_sigmoide
from src import graficar_relu
from src import graficar_tanh
from src import graficar_escalon
from src import graficar_identidad
from src import graficar_gaussiana
from src import graficar_lineal_tramos
from src import graficar_sinusoidal

def graficar_todo():
    # Crear una figura con 8 subgráficas (2 filas, 4 columnas)
    fig, axs = plt.subplots(2, 4, figsize=(20, 10))

    # Graficar cada función en su respectiva subgráfica
    graficar_sigmoide(axs[0, 0])
    graficar_relu(axs[0, 1])
    graficar_tanh(axs[0, 2])
    graficar_escalon(axs[0, 3])
    graficar_identidad(axs[1, 0])
    graficar_gaussiana(axs[1, 1])
    graficar_lineal_tramos(axs[1, 2])
    graficar_sinusoidal(axs[1, 3])

    # Ajustar el espacio entre subgráficas
    plt.tight_layout()

    # Mostrar la figura
    plt.show()

if __name__ == "__main__":
    graficar_todo()
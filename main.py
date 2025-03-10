import matplotlib.pyplot as plt
from src.Funcion_Sigmoidal import graficar_sigmoide
from src.Funcion_ReLu import graficar_relu
from src.Funcion_TanH import graficar_tanh
from src.Funcion_Identidad import graficar_identidad
from src.Funcion_Escalon import graficar_escalon
from src.Funcion_Gaussiana import graficar_gaussiana
from src.Funcion_Lineal_a_Tramos import graficar_lineal_tramos
from src.Funcion_Sinusoidal import graficar_sinusoidal

def graficar_todo():
    # Crear una figura con 2 filas y 4 columnas de subgráficas
    fig, axs = plt.subplots(2, 4, figsize=(20, 10))  # Ajusta el tamaño si es necesario

    # Graficar cada función en su respectiva subgráfica
    graficar_sigmoide(axs[0, 0])
    graficar_relu(axs[0, 1])
    graficar_tanh(axs[0, 2])
    graficar_identidad(axs[0, 3])
    graficar_escalon(axs[1, 0])
    graficar_gaussiana(axs[1, 1])
    graficar_lineal_tramos(axs[1, 2])
    graficar_sinusoidal(axs[1, 3])

    # Ajustar el espacio entre subgráficas
    plt.tight_layout()

    # Mostrar la figura con todas las gráficas
    plt.show()

if __name__ == "__main__":
    graficar_todo()
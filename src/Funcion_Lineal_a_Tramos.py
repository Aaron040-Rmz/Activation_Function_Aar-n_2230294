import numpy as np
import matplotlib.pyplot as plt

def graficar_lineal_tramos(ax):

    # Definimos la función lineal a tramos
    def lineal_tramos(x):
        """
        Se calcula la función lineal a tramos.
        - Devuelve 0 si x < 0.
        - Devuelve x si 0 <= x <= 1.
        - Devuelve 1 si x > 1.
        """
        return np.piecewise(x, [x < 0, (x >= 0) & (x <= 1), x > 1], [0, lambda x: x, 1])
    
    # Definimos la derivada de la función lineal a tramos
    def derivada_lineal_tramos(x):
        """
        Calcula la derivada de la función lineal a tramos.
        - La derivada es 0 si x < 0.
        - La derivada es 1 si 0 <= x <= 1.
        - La derivada es 0 si x > 1.
        """
        return np.piecewise(x, [x < 0, (x >= 0) & (x <= 1), x > 1], [0, 1, 0])
    
    # Generamos un rango de valores para x
    x = np.linspace(-2, 2, 1000)  # Crea 1000 puntos entre -2 y 2
    
    # Calculamos los valores de la función lineal a tramos y su derivada
    y = lineal_tramos(x)
    y_derivada = derivada_lineal_tramos(x)
    
    # Graficamos la función lineal a tramos
    ax.plot(x, y, label="Lineal a Tramos", color="magenta")
    
    # Graficamos la derivada de la función lineal a tramos como una línea punteada
    ax.plot(x, y_derivada, label="Derivada de Lineal a Tramos", linestyle="--", color="teal")
    
    # Se configura la gráfica
    ax.set_title("Función Lineal a Tramos y su Derivada")
    ax.set_xlabel("x")
    ax.set_ylabel("Lineal_tramos(x)")
    ax.grid(True)
    ax.legend(loc="upper left")
   


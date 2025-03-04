import numpy as np
import matplotlib.pyplot as plt

def graficar_gaussiana(ax):

    # Definimos la función gaussiana
    def gaussiana(x):
        
        # Se calcula la función gaussiana.
        #La gaussiana es una función que decae rápidamente a medida que x se aleja de 0.
        
        return np.exp(-x**2)
    
    # Definimos la derivada de la función gaussiana
    def derivada_gaussiana(x):
    
        return -2 * x * np.exp(-x**2)  # Derivada de la gaussiana
    
    # Generamos un rango de valores para x
    x = np.linspace(-10, 10, 1000)  # Crea 1000 puntos entre -10 y 10
    
    # Calculamos los valores de la función gaussiana y su derivada
    y = gaussiana(x)
    y_derivada = derivada_gaussiana(x)
    
    # Graficamos la función gaussiana
    ax.plot(x, y, label="Gaussiana", color="brown")
    
    # Graficamos la derivada de la función gaussiana como una línea punteada
    ax.plot(x, y_derivada, label="Derivada de la Gaussiana", linestyle="--", color="green")
    
    # Se configuró la gráfica
    ax.set_title("Función Gaussiana y su Derivada")
    ax.set_xlabel("x")
    ax.set_ylabel("Gaussiana(x)")
    ax.grid(True)
    ax.legend(loc="upper left")
    


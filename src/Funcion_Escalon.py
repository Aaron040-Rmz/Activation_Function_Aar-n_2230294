import numpy as np
import matplotlib.pyplot as plt

def graficar_escalon(ax):
   
    def escalon(x):
        #Se calcula la función escalón (Heaviside).
        #Devuelve 1 si x >= 0, y 0 en caso contrario.
        return np.where(x >= 0, 1, 0)
    
    def derivada_escalon(x):
        
        #Calcula la derivada de la función escalón.
        #La derivada es 0 en todos los puntos excepto en x = 0, donde no está definida.
        
        return np.where(x == 0, np.nan, 0) 
    
    # Generamos un rango de valores para x
    x = np.linspace(-10, 10, 1000)  # Crea 1000 puntos entre -10 y 10
    
    # Calculamos los valores de la función escalón y su derivada
    y = escalon(x)
    y_derivada = derivada_escalon(x)
    
    # Graficamos la función escalón
    ax.plot(x, y, label="Escalón", color="purple")
    
    # Graficamos la derivada de la función escalón como una línea punteada
    ax.plot(x, y_derivada, label="Derivada del Escalón", linestyle="--", color="brown")
    
    # Se configuró la gráfica
    ax.set_title("Función Escalón y su Derivada")
    ax.set_xlabel("x")
    ax.set_ylabel("Escalón(x)")
    ax.grid(True)
    ax.legend(loc="upper left")
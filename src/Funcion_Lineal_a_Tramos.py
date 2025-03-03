import numpy as np
import matplotlib.pyplot as plt

def graficar_lineal_tramos(ax):
  
    def lineal_tramos(x):
        return np.piecewise(x, [x < 0, (x >= 0) & (x <= 1), x > 1], [0, lambda x: x, 1])

   

    x = np.linspace(-2, 2, 1000)
    

    y = lineal_tramos(x)

 
    ax.plot(x, y, label="Lineal a Tramos", color="magenta")
    ax.set_title("Función Lineal a Tramos")
    ax.set_xlabel("x")
    ax.set_ylabel("lineal_tramos(x)")
    ax.grid(True)
    ax.legend()
   


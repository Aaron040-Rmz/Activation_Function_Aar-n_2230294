import numpy as np
import matplotlib.pyplot as plt

def graficar_identidad(ax):
  
    def identidad(x):
        return x  
  


    x = np.linspace(-10, 10, 1000)
    
  
    y = identidad(x)

  
    ax.plot(x, y, label="Identidad", color="orange")
    ax.set_title("Función Identidad")
    ax.set_xlabel("x")
    ax.set_ylabel("identidad(x)")
    ax.grid(True)
    ax.legend()
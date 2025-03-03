import numpy as np
import matplotlib.pyplot as plt

def graficar_gaussiana(ax):
    
    def gaussiana(x):
        return np.exp(-x**2) 

   
    x = np.linspace(-10, 10, 1000)
    
    
    y = gaussiana(x)

   
    ax.plot(x, y, label="Gaussiana", color="brown")
    ax.set_title("Función Gaussiana")
    ax.set_xlabel("x")
    ax.set_ylabel("gaussiana(x)")
    ax.grid(True)
    ax.legend()
    


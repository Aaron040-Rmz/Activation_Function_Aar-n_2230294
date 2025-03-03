import numpy as np
import matplotlib.pyplot as plt

def graficar_sinusoidal(ax):
   
    def sinusoidal(x):
        return np.sin(x)  
    
    
   
    x = np.linspace(-10, 10, 1000)
    
   
    y = sinusoidal(x)

  
    ax.plot(x, y, label="Sinusoidal", color="lime")
    ax.set_title("Función Sinusoidal")
    ax.set_xlabel("x")
    ax.set_ylabel("sinusoidal(x)")
    ax.grid(True)
    ax.legend()
    


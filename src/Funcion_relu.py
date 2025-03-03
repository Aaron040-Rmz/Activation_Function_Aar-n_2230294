import numpy as np
import matplotlib.pyplot as plt

def graficar_relu(ax):
 
    def relu(x):
        return np.maximum(0, x)  

    
  
    x = np.linspace(-10, 10, 1000)
    
  
    y = relu(x)

  
    ax.plot(x, y, label="ReLU", color="green")
    ax.set_title("Función ReLU")
    ax.set_xlabel("x")
    ax.set_ylabel("ReLU(x)")
    ax.grid(True)
    ax.legend()
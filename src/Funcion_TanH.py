import numpy as np
import matplotlib.pyplot as plt

def graficar_tanh(ax):
  
    def tanh(x):
        return np.tanh(x) 
    
    
    
    x = np.linspace(-10, 10, 1000)
    
   
    y = tanh(x)


    ax.plot(x, y, label="tanh", color="red")
    ax.set_title("Función TanH")
    ax.set_xlabel("x")
    ax.set_ylabel("TanH(x)")
    ax.grid(True)
    ax.legend()
    


  
import numpy as np  
import matplotlib.pyplot as plt  

def graficar_sigmoide(ax):
 
    def sigmoide(x):
        return 1 / (1 + np.exp(-x))  

 
  
    x = np.linspace(-10, 10, 1000)
    
   
    y = sigmoide(x)

  
    ax.plot(x, y, label="Sigmoide", color="blue")  
    ax.set_title("Función Sigmoide")  
    ax.set_xlabel("x") 
    ax.set_ylabel("sigmoide(x)") 
    ax.grid(True)  
    ax.legend()     
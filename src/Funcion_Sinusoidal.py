import numpy as np
import matplotlib.pyplot as plt

def graficar_sinusoidal():
   
    def sinusoidal(x):
        return np.sin(x)  

   
    x = np.linspace(-10, 10, 1000)
    
   
    y = sinusoidal(x)

  
    plt.plot(x, y, label="Sinusoidal", color="gray")
    plt.title("Función Sinusoidal")
    plt.xlabel("x")
    plt.ylabel("sinusoidal(x)")
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    graficar_sinusoidal()
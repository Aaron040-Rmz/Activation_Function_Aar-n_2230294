import numpy as np
import matplotlib.pyplot as plt

def graficar_identidad():
  
    def identidad(x):
        return x  
  
    x = np.linspace(-10, 10, 1000)
    
  
    y = identidad(x)

  
    plt.plot(x, y, label="Identidad", color="orange")
    plt.title("Función Identidad")
    plt.xlabel("x")
    plt.ylabel("identidad(x)")
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    graficar_identidad()
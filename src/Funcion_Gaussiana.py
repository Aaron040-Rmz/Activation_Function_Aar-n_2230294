import numpy as np
import matplotlib.pyplot as plt

def graficar_gaussiana():
    
    def gaussiana(x):
        return np.exp(-x**2) 

   
    x = np.linspace(-10, 10, 1000)
    
    
    y = gaussiana(x)

   
    plt.plot(x, y, label="Gaussiana", color="brown")
    plt.title("Función Gaussiana")
    plt.xlabel("x")
    plt.ylabel("gaussiana(x)")
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    graficar_gaussiana()
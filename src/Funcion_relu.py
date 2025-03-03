import numpy as np
import matplotlib.pyplot as plt

def graficar_relu():
 
    def relu(x):
        return np.maximum(0, x)  

  
    x = np.linspace(-10, 10, 1000)
    
  
    y = relu(x)

  
    plt.plot(x, y, label="ReLU", color="green")
    plt.title("Función ReLU")
    plt.xlabel("x")
    plt.ylabel("ReLU(x)")
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    graficar_relu()
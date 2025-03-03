import numpy as np
import matplotlib.pyplot as plt

def graficar_tanh():
  
    def tanh(x):
        return np.tanh(x) 

 
    x = np.linspace(-10, 10, 1000)
    
   
    y = tanh(x)


    plt.plot(x, y, label="tanh", color="red")
    plt.title("Función tanh")
    plt.xlabel("x")
    plt.ylabel("tanh(x)")
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    graficar_tanh()
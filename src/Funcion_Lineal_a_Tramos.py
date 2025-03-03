import numpy as np
import matplotlib.pyplot as plt

def graficar_lineal_tramos():
  
    def lineal_tramos(x):
        return np.piecewise(x, [x < 0, (x >= 0) & (x <= 1), x > 1], [0, lambda x: x, 1])

   
    x = np.linspace(-2, 2, 1000)
    

    y = lineal_tramos(x)

 
    plt.plot(x, y, label="Lineal a Tramos", color="pink")
    plt.title("Función Lineal a Tramos")
    plt.xlabel("x")
    plt.ylabel("lineal_tramos(x)")
    plt.grid(True)
    plt.legend()
    plt.show()


if __name__ == "__main__":
    graficar_lineal_tramos()
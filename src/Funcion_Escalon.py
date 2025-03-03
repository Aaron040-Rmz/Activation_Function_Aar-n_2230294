import numpy as np
import matplotlib.pyplot as plt

def graficar_escalon():
   
    def escalon(x):
        return np.where(x >= 0, 1, 0) 


    x = np.linspace(-10, 10, 1000)

    y = escalon(x)

    plt.plot(x, y, label="Escalón", color="purple")
    plt.title("Función Escalón")
    plt.xlabel("x")
    plt.ylabel("escalón(x)")
    plt.grid(True)
    plt.legend()
    plt.show()
    
if __name__ == "__main__":
    graficar_escalon()
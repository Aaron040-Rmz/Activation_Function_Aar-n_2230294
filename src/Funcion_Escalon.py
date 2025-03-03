import numpy as np
import matplotlib.pyplot as plt

def graficar_escalon(ax):
   
    def escalon(x):
        return np.where(x >= 0, 1, 0) 

    

    x = np.linspace(-10, 10, 1000)

    y = escalon(x)

    ax.plot(x, y, label="Escalón", color="purple")
    ax.set_title("Función Escalón")
    ax.set_xlabel("x")
    ax.set_ylabel("escalón(x)")
    ax.grid(True)
    ax.legend()
    


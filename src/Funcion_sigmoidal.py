import numpy as np  
import matplotlib.pyplot as plt  

def graficar_sigmoide():
 
    def sigmoide(x):
        return 1 / (1 + np.exp(-x))  

  
    x = np.linspace(-10, 10, 1000)
    
   
    y = sigmoide(x)

  
    plt.plot(x, y, label="Sigmoide", color="blue")  
    plt.title("Función Sigmoide")  
    plt.xlabel("x") 
    plt.ylabel("sigmoide(x)") 
    plt.grid(True)  
    plt.legend()  
    plt.show()  

if __name__ == "__main__":
    graficar_sigmoide()
# 🤖 Funciones de Activación para Redes Neuronales 🤖

**Estudiante**: Aarón Enrique Ramírez González  
**Tarea 1**: Gráficas de las funciones de activación con su derivada  
**Materia**: Sistemas de Visión Artificial  

---

## 📝 Descripción

Este repositorio contiene la implementación y gráficas de **ocho funciones de activación** utilizadas en redes neuronales, junto con sus correspondientes derivadas. El proyecto fue desarrollado en **Python 3.12.14**, utilizando las bibliotecas `NumPy` y `Matplotlib` para los cálculos numéricos y la visualización de las gráficas.

### 🤔 ¿Qué son las funciones de activación?

Las funciones de activación en redes neuronales son funciones matemáticas que se aplican a la salida de cada neurona para determinar si debe activarse (enviar información a la siguiente capa) o no. Estas funciones introducen **no linealidades** en el modelo, lo que permite que la red aprenda y represente relaciones complejas en los datos.

---

## 📋 Requisitos

Para ejecutar este proyecto, necesitas tener instaladas las siguientes bibliotecas de Python:

- **NumPy**: Para cálculos numéricos y manejo de arreglos.
- **Matplotlib**: Para la generación de gráficas.

Puedes instalar estas dependencias utilizando `pip`: 

```
pip install numpy matplotlib
```
## 🗂️ Estructura del Proyecto
El proyecto está organizado de la siguiente manera:
```
TAREA_1/
│
├── src/
│   ├── Function_EScalon.py          # Función Escalón y su derivada
│   ├── Function_Gaussiana.py        # Función Gaussiana y su derivada
│   ├── Function_Identidad.py        # Función Identidad y su derivada
│   ├── Function_Lineal_a_Tramos.py  # Función Lineal a Tramos y su derivada
│   ├── Function_Relu.py             # Función ReLU y su derivada
│   ├── Function_Sigmoidal.py        # Función Sigmoide y su derivada
│   ├── Function_Sinusoidal.py       # Función Sinusoidal y su derivada
│   └── Function_TanH.py             # Función Tangente Hiperbólica y su derivada
│
├── .gitignore                       # Archivo para ignorar archivos no deseados en Git
├── main.py                          # Script principal para generar las gráficas
├── README.md                        # Este archivo
└── Requirements.txt                 # Lista de dependencias
```

## 🛠️ Funcionalidades
## 🛠️ Funcionalidades

El proyecto incluye la implementación y gráficas de las siguientes **ocho funciones de activación**:

1. **Función Escalón (Step Function)**:
   - **Función**: Devuelve 1 si el valor de entrada es mayor o igual a 0; de lo contrario, devuelve 0.
   - **Derivada**: No está definida en x = 0; en otros puntos, es 0.

2. **Función Sigmoide (Sigmoid Function)**:
   - **Función**: Mapea cualquier valor a un rango entre 0 y 1.
   - **Derivada**: `sigmoide(x) * (1 - sigmoide(x))`.

3. **Función Tangente Hiperbólica (TanH)**:
   - **Función**: Mapea cualquier valor a un rango entre -1 y 1.
   - **Derivada**: `1 - tanh(x)^2`.

4. **Función ReLU (Rectified Linear Unit)**:
   - **Función**: Devuelve 0 si el valor de entrada es menor que 0; de lo contrario, devuelve el valor de entrada.
   - **Derivada**: 0 si x < 0; 1 si x >= 0.

5. **Función Lineal a Tramos (Piecewise Linear Function)**:
   - **Función**: Devuelve 0 si x < 0; x si 0 <= x <= 1; 1 si x > 1.
   - **Derivada**: 0 si x < 0; 1 si 0 <= x <= 1; 0 si x > 1.

6. **Función Gaussiana (Gaussian Function)**:
   - **Función**: `exp(-x^2)`.
   - **Derivada**: `-2 * x * exp(-x^2)`.   

7. **Función Sinusoidal (Sinusoidal Function)**:
   - **Función**: `sin(x)`.
   - **Derivada**: `cos(x)`.

8. **Función Identidad (Identity Function)**:
   - **Función**: Devuelve el mismo valor de entrada.
   - **Derivada**: 1 para todos los valores de x.



## 🚀 Pasos para Ejecutar el Repositorio y Ver las Gráficas
 
Sigue estos pasos para clonar el repositorio, instalar las dependencias y generar las gráficas:

### Clona el repositorio 🖥️:
Abre una terminal y ejecuta el siguiente comando para clonar el repositorio en tu computadora:

```bash
git clone https://github.com/tu-usuario/TAREA_1.git
```
Luego, accede a la carpeta del proyecto:
```bash
cd TAREA_1
```
### Instala las dependencias 📦:
Asegúrate de tener instaladas las bibliotecas necesarias. Ejecuta el siguiente comando para instalarlas:

```bash
pip install -r Requirements.txt
```
### Ejecuta el script principal 🚀:
Para generar las gráficas de las funciones de activación y sus derivadas, ejecuta el siguiente comando:
```bash
python main.py
```
### Visualiza las gráficas 📊:

Las gráficas se mostrarán en una ventana emergente.
Puedes navegar entre las gráficas usando los botones de la ventana.
Si quieres guardar las gráficas, modifica el código en `main.py` para usar `plt.savefig("ruta/de/la/grafica.png")`.

## 🛠️ Tecnologías Utilizadas
 -**Python**: Lenguaje de programación principal.
 -**NumPy**: Para cálculos numéricos.
 -**Matplotlib**: Para la generación de gráficas.

## ✨ Notas adicionales

Muchas gracias por leer mi primer README, te deseo un muy buen día 😊
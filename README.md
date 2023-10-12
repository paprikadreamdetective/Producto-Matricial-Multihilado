# Producto-Matricial-Multihilado
# 1. Funcionamiento.
Este programa multihilado calcula el producto de matrices de la forma $A$ x $B$ $=$ $C$ donde cada una de estas matrices es de dimension $n$ x $n$ (matrices cuadradas), usando un numero $n_{H}$ de hilos que es provisto por el usuario, donde cada hilo realiza los calculos correspondientes para la matriz resultante. A cada hilo se le asigna un renglon especifico a calcular.

- Las matrices $A$ y $B$ son importadas de un archivo ```.txt```, para esto dos hilos son creados para importar cada una de las matrices.
- La matriz resultante $C$ es calculada por los $n_{H}$ hilos que el usuario indique. Esta matriz resultante es exportada en un archivo ```.txt``` por el hilo principal (main thread)

## Ejemplo del funcionamiento: 

![image](https://github.com/paprikadreamdetective/Producto-Matricial-Multihilado/assets/133156970/0dc8f844-3333-4252-a288-e22979741cbe)

De esta manera los hilos trabajan de manera mas eficiente, ya que al sumar el $n_{H}$ al iterador, se pueden repartir las tareas de una manera adecuada e ir realizando los calculos de los renglones de la matriz $C$.

# 2. Implementacion.

## 2.1. Modulos importados.

Los modulos que se importaron para este programa fueron los siguientes:

```python
import threading # Modulo encargados de proveer los hilos
import logging   # Modulo encargado de proveer utilidades de depuracion
import numpy as np # Modulo encargado de proveer matrices y metodos para importar y exportar

```
## 2.2. Importar las matrices A y B.
Las funciones que los hilos procesaran son las siguientes:
```python
# Funcion encargada de importar la matriz desde un archivo txt y retornar dicha matriz
def crearMatriz(nombre):
    matriz = np.loadtxt(nombre, usecols=range(12))
    logging.info("Matriz: " + str(nombre) + " cargada.")
    return matriz
# Funcion encargada de asignar la matriz importada a la nueva matriz que se pase por referencia
def asignarMatriz(nombre, nuevaMatriz):
    matriz = crearMatriz(nombre)
    nuevaMatriz[:] = matriz
```
Se crean dos hilos, uno para cargar el archivo de la matriz $A$ y otro para cargar la matriz $B$:
```python
# Se crean 2 hilos, los cuales son denotados para cada matriz, se asigna un nombre, el procedimiento a realizar
# y los parametros, que ene ste caso es el nombre del archivo y la matriz que se requiera.
hilo_carga_matrizA = threading.Thread(name="Hilo para cargar matriz A", target=asignarMatriz, args=('A.txt', A))
hilo_carga_matrizB = threading.Thread(name="Hilo para cargar matriz B", target=asignarMatriz, args=('B.txt', B))
# Los hilos empiezan su ejecucion.
hilo_carga_matrizA.start()
hilo_carga_matrizB.start()
# Finalizan su ejecucion
hilo_carga_matrizA.join()
hilo_carga_matrizB.join()
```
El modulo ```numpy``` provee metodos para importar y exportar matrices desde un ```.txt``` y a un ```.txt``` respectivamente. Una vez hecho esto las matrices estaran cargadas en el programa.

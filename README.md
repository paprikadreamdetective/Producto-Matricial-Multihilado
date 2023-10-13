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

## 2.3. Realizar el producto matricial y repartir las tareas.

Una vez importadas las matrices, se tienen que repartir los hilos que calcularan cada renglon de la matriz resultante del producto. 
```python
for i in range(nH):
        inicio = i # Se define el inicio del renglon a calcular
        fin = inicio + 1 # Se delimita el renglon a calcular
        # Se crea el hilo, se pasan como parametros inicio y fin, saber que renglon tiene que ser calculado
        hilo = threading.Thread(name=("Hilo-" + str(i+1)), target=asignarTarea, args=(inicio, fin)) 
        # Se agregan los hilos a una lista para posteriormente terminarlos mediante dicha lista
        hilos.append(hilo)
        # Se empiezan a ejecutar los hilos
        hilo.start()
```
La funcion ```productoMatricial()``` esta diseñada para realizar el producto de matrices, el bucle ```while(fin <= len(C))``` evalua esta condicion que a su vez va de la mano de los incrementos de los contadores ```inicio += nH``` y ```fin += nH``` . Se incrementan de tal forma que las tareas se reparten en los renglones correspondientes. El numero de hilos define cada cuando tiene que ejecutar su tarea el hilo.
```python
def productoMatricial(inicio, fin):
    if columnas_A != filas_B:
        print("No se pueden multiplicar las matrices. El número de columnas de A debe ser igual al número de filas de B.")
        exit()
    else:
        while(fin <= len(C)):
            for i in range(inicio, fin):
                for j in range(columnas_B):
                    for k in range(filas_B):
                        C[i][j] += A[i][k] * B[k][j]
            logging.info("Renglon procesado: " + str(inicio) + ".")
            inicio += nH
            fin += nH
```
Esta funcion sirve para invocar a la funcion de ```productoMatricial```, recibiendo los parametros que se especifican a la hora de la creacion de los hilos.
```python
def asignarTarea(inicio, fin):
    productoMatricial(inicio, fin)
```
Por ultimo la matriz $C$ es exportada por el hilo principal en un archivo ```.txt``` mediante la siguinete funcion:
```python
def exportarMatriz():
    np.savetxt('C.txt', C, fmt='%d', delimiter=' ')
    print(" ")
    logging.info("Matriz exportada.")
```
# 3. Resultado de implementacion.

Para esta ejecucion del programa, las matrices $A$ y $B$ ya han sido definidas en archivos de texto, las cuales tienen una dimension de $12$x$12$ e ingresaremos un numero de 3 hilos a ejecutar:

![image](https://github.com/paprikadreamdetective/Producto-Matricial-Multihilado/assets/133156970/5cf178a3-0215-410b-81df-7f6eae0663c2)

Se observa que en la parte superior aparece un mensaje que nos indica el nombre del hilo y se notifica si la matriz ha sido importada.

Una vez introducido el numero de hilos a ejecutar, se empieza a procesar el producto matricial (el numero de hilos tiene que ser mayor o igual a 2 de lo contrario el programa terminara su ejecucion):

![image](https://github.com/paprikadreamdetective/Producto-Matricial-Multihilado/assets/133156970/9b46e97b-6d6f-4731-9beb-674e50ca5dd2)

Observemos que el orden en que los hilos realizan las tareas siempre es el numero de renglon donde empiezan mas el numero de hilos que el usario introdujo, esto hace no se consuman recursos de mas, dividiendo las tareas lo mas equitativo posible.
Por ultimo, observemos que la matriz $C$ es importada por el hilo principal, ya que el mensaje notifica que ha realizado dicha accion.

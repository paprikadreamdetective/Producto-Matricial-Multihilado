# Producto-Matricial-Multihilado

Este programa multihilado calcula el producto de matrices de la forma $A$ x $B$ $=$ $C$ donde cada una de estas matrices es de dimension $n$ x $n$ (matrices cuadradas), usando un numero $n_{H}$ de hilos que es provisto por el usuario, donde cada hilo realiza los calculos correspondientes para la matriz resultante. A cada hilo se le asigna un renglon especifico a calcular.

- Las matrices $A$ y $B$ son importadas de un archivo ```.txt```, para esto dos hilos son creados para importar cada una de las matrices.
- La matriz resultante $C$ es calculada por los $n_{H}$ hilos que el usuario indique. Esta matriz resultante es exportada en un archivo ```.txt``` por el hilo principal (main thread)

## Ejemplo del funcionamiento: 

![image](https://github.com/paprikadreamdetective/Producto-Matricial-Multihilado/assets/133156970/0dc8f844-3333-4252-a288-e22979741cbe)

De esta manera los hilos trabajan de manera mas eficiente, ya que al sumar el $n_{H}$ al iterador, se pueden repartir las tareas de una manera adecuada e ir realizando los calculos de los renglones de la matriz $C$.

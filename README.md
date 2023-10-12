# Producto-Matricial-Multihilado

Este programa multihilado calcula el producto de matrices de $n$ x $n$ (matrices cuadradas), usando un numero $n_{H}$ de hilos que es provisto por el usuario, donde cada hilo realiza los calculos de la siguiente manera:


- Las matrices $A$ y $B$ son importadas de un archivo ```.txt```, para esto dos hilos son creados para importar cada una de las matrices.
- La matriz resultante $C$ es calculada por los $n_{H}$ hilos que el usuario indique. Esta matriz resultante es exportada en un archivo ```.txt``` por el hilo principal (main thread)

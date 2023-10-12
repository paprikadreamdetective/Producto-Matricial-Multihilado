import threading
import time
import datetime
import logging
import math
import numpy as np
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] (%(threadName)-s) %(message)s')

#matrizA = open("A.txt")
#matrizB = open("B.txt")
# Abre el archivo en modo lectura

    #     return(self.matriz)

     # def establecer_valor(self, nuevo_valor):
     #    self.valor = nuevo_valor
def crearMatriz(nombre):
     if (nombre):
         matriz = np.loadtxt(nombre, usecols=range(3))
         return (matriz)



matriz = crearMatriz("A.txt")


for fila in matriz:
    print(fila)



# Definir las matrices A y B
# A = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
#
# B = [[9, 8, 7],
#      [6, 5, 4],
#      [3, 2, 1]]

A = np.zeros((11, 11))
B = np.zeros((11, 11))
# B = [
#     [1, 2, 3, 4, 5, 6, 7, 8],
#     [9, 10, 1, 2, 3, 4, 5, 6],
#     [7, 8, 9, 10, 1, 2, 3, 4],
#     [5, 6, 7, 8, 9, 10, 1, 2],
#     [3, 4, 5, 6, 7, 8, 9, 10],
#     [1, 2, 3, 4, 5, 6, 7, 8],
#     [9, 10, 1, 2, 3, 4, 5, 6],
#     [7, 8, 9, 10, 1, 2, 3, 4],
#     [7, 8, 9, 10, 1, 2, 3, 4],
#     [7, 8, 9, 10, 1, 2, 3, 4],
#     [7, 8, 9, 10, 1, 2, 3, 4]
# ]

# Dimensiones de las matrices
filas_A = len(A)
columnas_A = len(A[0])
filas_B = len(B)
columnas_B = len(B[0])

# Verificar si se pueden multiplicar las matrices
if columnas_A != filas_B:
    print("No se pueden multiplicar las matrices. El número de columnas de A debe ser igual al número de filas de B.")
    exit()

# Matriz resultante de la multiplicación
C = [[0 for _ in range(columnas_B)] for _ in range(filas_A)]

# Número de hilos
numero_de_hilos = 3

# Función para realizar la multiplicación de matrices en bloques de filas
def multiplicar_filas(inicio, fin):
    logging.info("Consultando para el id " + str(inicio) + " fin " + str(fin))
    for i in range(inicio, fin):
        for j in range(columnas_B):
            for k in range(filas_B):
                C[i][j] += A[i][k] * B[k][j]

# Lista para almacenar los hilos
hilos = []

# Dividir las filas para que cada hilo procese un bloque de filas
# bloque_filas = filas_A // numero_de_hilos
# print("Bloque: ", bloque_filas)
bloque_filas = math.ceil(filas_A / numero_de_hilos)
print("Bloque: ", bloque_filas)
inicio = 0
fin = 0

# for i in range(numero_de_hilos):
#     inicio = i * bloque_filas
#     fin = min((i + 1) * bloque_filas, filas_A)
#
#     hilo = threading.Thread(target=multiplicar_filas, args=(inicio, fin))
#     hilos.append(hilo)
#     hilo.start()

# Esperar a que todos los hilos terminen
for hilo in hilos:
    hilo.join()

# Imprimir la matriz resultante C
for fila in C:
    print(fila)

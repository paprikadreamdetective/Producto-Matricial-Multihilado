import threading
import time
import datetime
import logging
import math
import numpy as np
import random

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] (%(threadName)-s) %(message)s')

# Crear la matriz A y B (en este ejemplo se generan aleatoriamente)
# A = np.zeros((8, 8))
# B = np.zeros((8, 8))

A = [
     [1, 2, 3, 4, 5, 6, 7, 8],
     [9, 10, 1, 2, 3, 4, 5, 6],
     [7, 8, 9, 10, 1, 2, 3, 4],
     [5, 6, 7, 8, 9, 10, 1, 2],
     [3, 4, 5, 6, 7, 8, 9, 10],
     [1, 2, 3, 4, 5, 6, 7, 8],
     [9, 10, 1, 2, 3, 4, 5, 6],
     [7, 8, 9, 10, 1, 2, 3, 4]
 ]

B = [
     [1, 2, 3, 4, 5, 6, 7, 8],
     [9, 10, 1, 2, 3, 4, 5, 6],
     [7, 8, 9, 10, 1, 2, 3, 4],
     [5, 6, 7, 8, 9, 10, 1, 2],
     [3, 4, 5, 6, 7, 8, 9, 10],
     [1, 2, 3, 4, 5, 6, 7, 8],
     [9, 10, 1, 2, 3, 4, 5, 6],
     [7, 8, 9, 10, 1, 2, 3, 4],
 ]

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
numero_de_hilos = 3  # Cambiar el número de hilos aquí

# Semáforo para controlar el acceso a las filas de C

# Función para realizar la multiplicación de matrices en bloques de filas
def multiplicar_filas(inicio, fin):
    #logging.info("Consultando para el id " + str(inicio) + " fin " + str(fin))
    #aux_inicio = inicio
    #aux_fin = fin

    #if aux_fin < 11:
    while(fin <= 8):
        for i in range(inicio, fin):
            for j in range(columnas_B):
                for k in range(filas_B):
                    C[i][j] += A[i][k] * B[k][j]
        #logging.info("inicio " + str(aux_inicio) + " fin " + str(aux_fin))
        logging.info("Renglon procesado: " + str(inicio))

        inicio += numero_de_hilos
        fin += numero_de_hilos

# Lista para almacenar los hilos
hilos = []
# Dividir las filas para que cada hilo procese un bloque de filas
bloque_filas = math.ceil(filas_A / numero_de_hilos)
#inicio = 0
# Función para que los hilos multipliquen renglones específicos
def worker(hilo_id, inicio, fin):
    #logging.info(f"Hilo {hilo_id} procesando filas {inicio} - {fin}")
    multiplicar_filas(inicio, fin)
# inicio = 0
# fin = 0
# Iniciar los hilos
for i in range(numero_de_hilos):
    #inicio = i  # Cada hilo inicia en una fila diferente
    #fin = filas_A
    inicio = i
    fin = inicio + 1
    hilo = threading.Thread(target=worker, args=(i+1, inicio, fin))
    hilos.append(hilo)
    hilo.start()

# Esperar a que todos los hilos terminen
for hilo in hilos:
    hilo.join()

# Imprimir la matriz resultante C
for fila in C:
    print(fila)


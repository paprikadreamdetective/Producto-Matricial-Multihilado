import threading
import logging
import numpy as np

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] (%(threadName)-s) %(message)s')

nH = 0
hilos = []
A = np.zeros((12, 12))
B = np.zeros((12, 12))
filas_A = len(A)
columnas_A = len(A[0])
filas_B = len(B)
columnas_B = len(B[0])
C = [[0 for _ in range(columnas_B)] for _ in range(filas_A)]

def crearMatriz(nombre):
    matriz = np.loadtxt(nombre, usecols=range(12))
    logging.info("Matriz: " + str(nombre) + " cargada.")
    return matriz

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

def asignarTarea(inicio, fin):
    productoMatricial(inicio, fin)

def asignarMatriz(nombre, nuevaMatriz):
    matriz = crearMatriz(nombre)
    nuevaMatriz[:] = matriz

def exportarMatriz():
    np.savetxt('C.txt', C, fmt='%d', delimiter=' ')
    print(" ")
    logging.info("Matriz exportada.")

if __name__ == "__main__":
    hilo_carga_matrizA = threading.Thread(name="Hilo para cargar matriz A", target=asignarMatriz, args=('A.txt', A))
    hilo_carga_matrizB = threading.Thread(name="Hilo para cargar matriz B", target=asignarMatriz, args=('B.txt', B))
    hilo_carga_matrizA.start()
    hilo_carga_matrizB.start()
    hilo_carga_matrizA.join()
    hilo_carga_matrizB.join()

    print("Matriz A: ")
    for renglon in A:
        print(renglon)
    print(" ")
    print("Matriz B: ")
    for renglon in B:
        print(renglon)

    nH = int(input("\n Ingrese el numero de hilos: "))
    for i in range(nH):
        inicio = i
        fin = inicio + 1
        hilo = threading.Thread(name=("Hilo-" + str(i+1)), target=asignarTarea, args=(inicio, fin))
        hilos.append(hilo)
        hilo.start()

    for hilo in hilos:
        hilo.join()
    print("\n Matriz C: ")
    for fila in C:
        print(fila)

    exportarMatriz()

import time
import numpy as np
from itertools import repeat
from multiprocessing import Pool, cpu_count


M = 5_000
N = 5_000

def mult_vector_vector(x, y):
    suma = 0

    for i in range(len(x)):
        suma += x[i] * y[i]
    
    return suma


def main(mat_M, vector_A, pool_size):
    p = Pool(processes=pool_size)
    args = zip(mat_M, repeat(vector_A))
    resultados = p.starmap(mult_vector_vector, args)
    p.close()
    p.join()

    return resultados


if __name__ == "__main__":
    mat_M = np.random.randint(100, size=(M, N))
    vector_A = np.random.randint(100, size=(N, ))

    pool_sizes = [2, 4, 8, 16, 32]
    tiempos = list()

    for pool_size in pool_sizes:
        for i in range(10):
            print(f"Procesando iteracion {i} de pool size: {pool_size}")
            tiempos_parciales = list()
            inicio = time.perf_counter()
            main(mat_M, vector_A, pool_size)
            fin = time.perf_counter()
            tiempos_parciales.append(fin - inicio)
        tiempos_parciales.sort()
        tiempo_parcial = tiempos_parciales[len(tiempos_parciales) // 2]
        tiempos.append([pool_size, tiempo_parcial])

    for item in tiempos:
        print(f"Pool size: {item[0]}\tTiempo: {item[1]:.2f} segundos")

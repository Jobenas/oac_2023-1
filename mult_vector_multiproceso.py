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


if __name__ == "__main__":
    mat_M = np.random.randint(100, size=(M, N))
    vector_A = np.random.randint(100, size=(N, ))

    inicio = time.perf_counter()
    p = Pool(processes=cpu_count())
    args = zip(mat_M, repeat(vector_A))
    resultados = p.starmap(mult_vector_vector, args)
    fin = time.perf_counter()

    print(f"Tiempo de ejecucion multiproceso: {fin - inicio:.2f} segundos")

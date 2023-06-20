import time
from multiprocessing import Pool, cpu_count

def potencia(n: int, div: int = 2):
    res = 1

    for _ in range(n // div):
        res *= n
    
    return res


if __name__ == "__main__":
    p = Pool(processes=cpu_count())
    args = [100_000] * 2

    inicio = time.perf_counter()
    resultados = p.map(potencia, args)
    p.close()
    p.join()
    resultado = resultados[0] * resultados[1]
    fin = time.perf_counter()

    print(f"Tiempo de ejecucion: {fin - inicio} segundos")

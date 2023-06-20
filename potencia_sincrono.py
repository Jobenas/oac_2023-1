import time

def potencia(n: int, div: int = 1) -> int:
    res = 1

    for _ in range(n // div):
        res *= n
    
    return res


if __name__ == "__main__":
    inicio = time.perf_counter()
    resultado = potencia(100_000)
    fin = time.perf_counter()

    print(f"Tiempo de ejecucion: {fin - inicio} segundos")

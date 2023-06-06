import time

inicios = dict()

resultados = list()


def custom_sleep(idx: int, secs: int): 
    if not idx in inicios.keys():
        inicios[idx] = time.perf_counter()
        return False
    
    if (time.perf_counter() - inicios[idx] >= secs):
        return True
    
    return False

def count(idx: int):
    if not idx in inicios.keys():
        print(f"[{idx}] One")

    res = custom_sleep(idx,1)

    if res:
        print(f"[{idx}] Two")

    return res


if __name__ == "__main__":
    resultados = [False, False, False]
    inicio = time.perf_counter()
    while not resultados[0] and not resultados[1] and not resultados[2]:
        if not resultados[0]:
            resultados[0] = count(0)

        if not resultados[1]:
            resultados[1] = count(1)
        
        if not resultados[2]:
            resultados[2] = count(2)
    fin = time.perf_counter()

    print(f"Tiempo total de ejecucion: {fin - inicio} segundos")


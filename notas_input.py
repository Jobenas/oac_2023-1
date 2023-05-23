import time

def registra_numero(pista: str) -> float:
    num_flag = False

    while not num_flag:
        num = input(pista)
        try:
            num_val = float(num)
            if num_val < 0 or num_val > 20:
                continue
            num_flag = True
        except ValueError:
            pass
    
    return num_val


if __name__ == '__main__':
    inicio_total = time.perf_counter()
    pa_list = list()
    pb_list = list()

    inicio_es = time.perf_counter()
    for i in range(4):
        pa = registra_numero(f"Ingrese la nota de la Pa{i + 1}: ")
        pa_list.append(pa)
    
    for i in range(5):
        pb = registra_numero(f"Ingrese la nota de la Pb{i + 1}: ")
        pb_list.append(pb)

    e1 = registra_numero(f"Ingrese la nota del examen 1: ")
    e2 = registra_numero(f"Ingrese la nota del examen 2: ")
    fin_es = time.perf_counter()

    inicio_cpu = time.perf_counter()
    pa_list.sort()
    pb_list.sort()

    nota_pa = sum(pa_list[1:]) / len(pa_list[1:])
    nota_pb = sum(pb_list[1:]) / len(pb_list[1:])

    nota_final = ((3 * nota_pa) + (3 * nota_pb) + (2 * e1) + (2 * e2)) / 10.0
    fin_cpu = time.perf_counter()

    print(f"Nota final: {nota_final}")
    fin_total = time.perf_counter()

    print(f"Tiempo total de operaciones E/S: {fin_es - inicio_es} segundos")
    print(f"Tiempo total de CPU: {fin_cpu - inicio_cpu} segundos")
    print(f"Tiempo total de ejecucion: {fin_total - inicio_total} segundos")

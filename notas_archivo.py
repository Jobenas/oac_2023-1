import time


def calcular_notas() -> dict:
    inicio_total = time.perf_counter()
    inicio_entrada = time.perf_counter()
    with open("notas.csv", "r") as f:
        contenido = f.read()
    fin_entrada = time.perf_counter()
    
    inicio_cpu = time.perf_counter()
    filas = contenido.split("\n")
    cabecera = filas[0]
    filas = filas[1:]

    notas_finales = list()
    for fila in filas:
        fila = fila.split(",")
        pa_list = list()
        for i in range(1, 5):
            pa_list.append(float(fila[i]))
        
        pb_list = list()
        for i in range(5, 10):
            pb_list.append(float(fila[i]))
        
        e1 = float(fila[10])
        e2 = float(fila[11])

        pa_list.sort()
        pb_list.sort()

        pa = sum(pa_list[1:]) / len(pa_list[1:])
        pb = sum(pb_list[1:]) / len(pb_list[1:])

        nota_final = ((3 * pa) + (3 * pb) + (2 * e1) + (2 * e2)) / 10.0

        notas_finales.append([fila[0], nota_final])
    fin_cpu = time.perf_counter()

    inicio_salida = time.perf_counter()
    print(notas_finales)
    fin_salida = time.perf_counter()
    fin_total = time.perf_counter()

    tiempo_total = fin_total - inicio_total
    tiempo_cpu = fin_cpu - inicio_cpu
    tiempo_entrada = fin_entrada - inicio_entrada
    tiempo_salida = fin_salida - inicio_salida
    tiempo_es = tiempo_entrada + tiempo_salida

    tiempo_dict = {
        "tiempo_total": tiempo_total,
        "tiempo_cpu": tiempo_cpu,
        "tiempo_entrada": tiempo_entrada,
        "tiempo_salida": tiempo_salida,
        "tiempo_es": tiempo_es
    }

    return tiempo_dict


if __name__ == '__main__':
    total_list = list()
    cpu_list = list()
    entrada_list = list()
    salida_list = list()
    es_list = list()

    for _ in range(10):
        res = calcular_notas()
        total_list.append(res["tiempo_total"])
        cpu_list.append(res["tiempo_cpu"])
        entrada_list.append(res["tiempo_entrada"])
        salida_list.append(res["tiempo_salida"])
        es_list.append(res["tiempo_es"])

    total_list.sort()
    cpu_list.sort()
    entrada_list.sort()
    salida_list.sort()
    es_list.sort()

    print("************************************************************")
    print(f"Mediana de tiempo total de ejecucion: {total_list[len(total_list) // 2]}")
    print(f"Mediana de tiempo de cpu: {cpu_list[len(cpu_list) // 2]}")
    print(f"Mediana de tiempo de entrada: {entrada_list[len(entrada_list) // 2]}")
    print(f"Mediana de tiempo de salida: {salida_list[len(salida_list) // 2]}")
    print(f"Mediana de tiempo de E/S: {es_list[len(es_list) // 2]}")

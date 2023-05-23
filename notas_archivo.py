import time

if __name__ == '__main__':
    inicio_total = time.perf_counter()
    inicio_es = time.perf_counter()
    with open("notas.csv", "r") as f:
        contenido = f.read()
    fin_es = time.perf_counter()
    
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

    print(notas_finales)
    fin_total = time.perf_counter()

    print(f"Tiempo total de operaciones E/S: {fin_es - inicio_es} segundos")
    print(f"Tiempo total de CPU: {fin_cpu - inicio_cpu} segundos")
    print(f"Tiempo total de ejecucion: {fin_total - inicio_total} segundos")

import time


if __name__ == '__main__':
    inicio = time.perf_counter()
    num_flag = False

    while not num_flag:
        input_inicio = time.perf_counter()
        num = input("Ingrese un numero: ")
        input_fin = time.perf_counter()

        conv_inicio = time.perf_counter()
        try:
            num_val = float(num)
            num_flag = True
        except ValueError:
            pass
        conv_fin = time.perf_counter()
    
    cpu_inicio = time.perf_counter()
    num_val_sqrd = num_val ** 2
    cpu_fin = time.perf_counter()

    fin = time.perf_counter()

    print(f"Numero ingresado: {num_val}, y su valor al cuadrado es {num_val_sqrd}")
    print(f"Tiempo de ejecucion de entrada: {input_fin - input_inicio} segundos")
    print(f"Tiempo de ejecucion de conversion: {conv_fin - conv_inicio} segundos")
    print(f"Tiempo de ejecucion de procesamiento: {cpu_fin - cpu_inicio} segundos")
    print(f"Tiempo de ejecucion de todo el programa: {fin - inicio} segundos")
    
import time

if __name__ == '__main__':
    inicio = time.perf_counter()
    f = open("README.md", "r")
    contenido = f.read()
    f.close()
    fin = time.perf_counter()

    print(contenido)
    print(type(contenido))
    print(f"Tiempo total de lectura: {fin - inicio} segundos")

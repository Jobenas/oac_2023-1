import time


def count(count_id: int):
    print(f"{count_id} One")
    time.sleep(1)
    print(f"{count_id} Two")


def main():
    for i in range(1, 4):
        count(i)


if __name__ == "__main__":
    inicio = time.perf_counter()
    main()
    fin = time.perf_counter()

    print(f"Tiempo de ejecucion: {fin - inicio} segundos")

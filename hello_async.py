import asyncio
import time
import random


async def count(count_id: int):
    print(f"{count_id} One")
    await asyncio.sleep(random.randint(1, 6))
    print(f"{count_id} Two")


async def main():
    await asyncio.gather(*(count(i) for i in range(1, 4)))


if __name__ == "__main__":
    inicio = time.perf_counter()
    asyncio.run(main())
    fin = time.perf_counter()

    print(f"Tiempo total de ejecucion: {fin - inicio} segundos")

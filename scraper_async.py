import time
import asyncio
import aiohttp

async def download_site(url, session):
    async with session.get(url) as response:
        print(f"Lei {len(await response.read())} bytes de {url}")


async def download_all_sites(sites):
    async with aiohttp.ClientSession() as session:
        tasks = list()
        for url in sites:
            task = asyncio.ensure_future(download_site(url, session))
            tasks.append(task)
    await asyncio.gather(*tasks, return_exceptions=True)


if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice"
    ] * 80

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    inicio = time.perf_counter()
    loop.run_until_complete(download_all_sites(sites))
    fin = time.perf_counter()

    print(f"Descargado {len(sites)} de manera asincrona en {fin - inicio} segundos")
import requests
import time


def download_site(url, session):
    with session.get(url) as response:
        pass
        # print(f"Lei {len(response.content)} bytes de {url}")


def download_all_sites(sites):
    with requests.Session() as session:
        for url in sites:
            download_site(url, session)


if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice"
    ] * 80

    inicio = time.perf_counter()
    download_all_sites(sites)
    fin = time.perf_counter()

    print(f"Descargado {len(sites)} de manera sincrona en {fin - inicio} segundos")


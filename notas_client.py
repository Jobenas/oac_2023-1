import random
import socket
import time


SOCK_BUFFER = 1024


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("192.168.1.13", 5000)

    print(f"Conectando a {server_address[0]}:{server_address[1]}")

    sock.connect(server_address)

    try:
        for _ in range(15):
            msg = f"{20230001 + random.randint(0, 41)}"
            sock.sendall(msg.encode("utf-8"))
            data = sock.recv(SOCK_BUFFER)
            print(f"Recibi: {data}")
            time.sleep(2)
    finally:
        print("Cerrando la conexion")
        sock.close()

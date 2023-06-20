import socket
import time
from threading import Thread

SOCK_BUFFER = 1024
num_clientes = 0


def client_handler(conn, client_address):
    global num_clientes
    num_clientes += 1
    print(f"Numero de clientes conectados: {num_clientes}")
    try:
        print(f"Conectado desde {client_address[0]}")
        
        while True:
            data = conn.recv(SOCK_BUFFER)
            print(f"Recibi: {data}")
            if data:
                print(f"Enviando: {data}")
                conn.sendall(data)
            else:
                print("No hay mas datos")
                break
    except ConnectionResetError:
        print("El cliente ha cerrado la conexion de manera abrupta")
    finally:
        print("Cerrando la conexion con el cliente")
        num_clientes -= 1
        conn.close()


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('localhost', 5000)
    print(f"Iniciando conexion en {server_address[0]}:{server_address[1]}")
    sock.bind(server_address)

    sock.listen(1)

    while True:
        print("Esperando conexiones")

        conn, client_address = sock.accept()

        client_thread = Thread(target=client_handler, args=(conn, client_address))
        client_thread.start()
        
        time.sleep(0.01)

        while num_clientes >= 2:
            pass

import socket

SOCK_BUFFER = 1024


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("192.168.1.13", 5000)

    print(f"Conectando a {server_address[0]}:{server_address[1]}")

    sock.connect(server_address)

    try:
        msg = "Hola Mundo"
        sock.sendall(msg.encode("utf-8"))
        data = sock.recv(SOCK_BUFFER)
        print(f"Recibi: {data}")

    finally:
        print("Cerrando la conexion")
        sock.close()

import socket

SOCK_BUFFER = 1024


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ("0.0.0.0", 5000)
    print(f"Iniciando en servidor {server_address[0]} en el puerto {server_address[1]}")
    sock.bind(server_address)

    sock.listen(5)

    while True:
        print("Esperando conexion...")
        try:
            conn, client_address = sock.accept()
            print(f"Conexion desde {client_address[0]} en puerto {client_address[1]}")

            try:
                while True:
                    data = conn.recv(SOCK_BUFFER)
                    print(f"Recibi: {data}")
                    if data:
                        print(f"enviando {data}")
                        conn.sendall(data)
                    else:
                        print("No hay mas datos")
                        break
            except ConnectionResetError:
                print("El cliente ha cerrado la conexion de manera abrupta")
            finally:
                print("Cerrando conexion con el cliente")
                conn.close()
        except KeyboardInterrupt:
            print("El usuario ha terminado el programa")
            break
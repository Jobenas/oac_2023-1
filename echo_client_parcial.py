import socket
import random
import time

SOCK_BUFFER = 4

msgs = ["Hola Mundo", "Esto tiene una eñe", "¿Cómo estás?", "Mensaje en ASCII"]

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("localhost", 5000)

    print(f"Conectando a {server_address[0]}:{server_address[1]}")

    sock.connect(server_address)

    try:
        for i in range(10):
            msg = f"Hola mundo {i}"
            sock.sendall(msg.encode("utf-8"))
            # amnt_expected = len(msg.encode("utf-8"))
            amnt_expected = len(msg)
            amnt_recvd = 0
            total_msg_bytes = b''
            
            while amnt_recvd < amnt_expected:
                data = sock.recv(SOCK_BUFFER)
                print(f"Recibi: {data}")
                amnt_recvd += len(data)
                total_msg_bytes += data
            print(f"Mensaje total: {total_msg_bytes.decode('utf-8')}")

            time.sleep(2)
    finally:
        print("Cerrando la conexion")
        sock.close()

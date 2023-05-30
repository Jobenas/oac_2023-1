import socket

SOCK_BUFFER = 1024

def valida_data(codigo: str) -> bool:
    try:
        cmd = int(codigo)
    except ValueError:
        return False
    
    if 20230001 <= cmd <= 20230040:
        return True
    
    return False


def calcula_nota(fila: list[str]) -> float:
    notas = [int(valor) for valor in fila]
    
    pa_list = notas[1:5]
    pb_list = notas[5:10]
    e1 = notas[10]
    e2 = notas[11]

    pa_list.sort()
    pb_list.sort()

    pa = sum(pa_list[1:]) / len(pa_list[1:])
    pb = sum(pb_list[1:]) / len(pb_list[1:])

    nota_final = ((3 * pa) + (3 * pb) + (2 * e1) + (2 * e2)) / 10.0

    return nota_final


def genera_nota(codigo: str) -> float:
    with open("notas.csv", "r") as f:
        contenido = f.read()
    
    filas = contenido.split("\n")

    for fila in filas:
        fila = fila.split(",")
        if fila[0] == codigo:
            nota_final = calcula_nota(fila)
            return nota_final
    
    return -1.0


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ("0.0.0.0", 5000)
    print(f"Iniciando en servidor {server_address[0]} en el puerto {server_address[1]}")
    sock.bind(server_address)

    sock.listen(1)

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
                        if valida_data(data.decode("utf-8")):
                            nota = genera_nota(data.decode("utf-8"))
                            conn.sendall(f"Nota para codigo {data.decode('utf-8')}: {nota}".encode("utf-8"))
                        else:
                            conn.sendall("Requerimiento invalido".encode("utf-8"))
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
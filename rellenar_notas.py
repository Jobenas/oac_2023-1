import random


if __name__ == '__main__':
    contenido_nuevo = ""
    codigo_inicio = 20230003

    for i in range(38):
        notas = [f"{str(random.randint(0, 21))}," for _ in range(11)]
        notas_txt = f"{codigo_inicio + i},{''.join(notas)[:-1]}\n"
        contenido_nuevo += notas_txt

    with open("notas.csv", "r") as f:
        contenido = f.read()
    
    contenido += f"\n{contenido_nuevo[:-1]}"

    with open("notas.csv", "w+") as f:
        f.write(contenido)
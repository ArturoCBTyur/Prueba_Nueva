# r  -> Solo lectura
# r+ -> Lectura y escritura
# w  -> Solo escritura. Sobre escribe el archivo si existe. Crea el archivo si no existe
# w+ -> Escritura y lectura. Sobre escribe el archivo si existe. Crea el archivo si no existe
# a  -> Añadido (agregar contenido). Crea el archivo si éste no existe
# a+ -> Añadido (agregar contenido) y lectura. Crea el archivo si éste no existe.

def read():
    numbers = []
    with open("./files/numbers.txt", "r",encoding="UTF-8") as file:
        for line in file:
            numbers.append(int(line))
        print(numbers)

def write():
    names = ["Yhojan","Pepe","Miguel","Cristian","Rocío"]
    with open("./files/names.txt","w",encoding="UTF-8") as file:
        for name in names:
            file.write(name)
            file.write("\n")

def main():
    write()


if __name__ == "__main__":
    main()
titulos = [""] * 20
ejemplares = [0] * 20
cantidad_de_libros = 0

def cargar():
    global cantidad_de_libros
    maximo = int(input("Ingresa cuantos libros quiere (hasta 20): "))
    
    for i in range(maximo):
        if cantidad_de_libros < 20:
            nombre = input(f"Ingrese el titulo {cantidad_de_libros+1}: ")
            ejemplar = int(input("Ingrese cuantos ejemplares quiere: "))
            titulos[cantidad_de_libros] = nombre
            ejemplares[cantidad_de_libros] = ejemplar
            cantidad_de_libros += 1
        else:
            print("Alcanzaste el maximo de libros")
            break
def catalogo():
    print("---Catalogo completo de libros---")
    for i in range(cantidad_de_libros):
        print(f"{titulos[i]} --> {ejemplares} ejemplares")


def consultar_disponibilidad():
    titulo = input("Ingrese el titulo a consultar: ")
    encontrado = False
    for i in range(cantidad_de_libros):
        if titulos[i] == titulo:
            print(f"{titulos[i]} tiene {ejemplares[i]} ejemplares disponibles.")
            encontrado = True
            break
    if not encontrado:
        print("Ese libro no esta en el catalogo.")

def libros_agotados():
    print("---Libros Agotados---")
    agotados = False
    for i in range(cantidad_de_libros):
        if ejemplares[i] == 0:
            print(titulos[i])
            agotados = True
    if not agotados:
        print("No hay libros agotados.")

def agregar_titulo():
    global cantidad_de_libros
    if cantidad_de_libros < 20:
        nombre = input("Ingrese el nuevo titulo: ")
        ejemplar = int(input("Ingrese cuantos ejemplares quiere: "))
        titulos[cantidad_de_libros] = nombre
        ejemplares[cantidad_de_libros] = ejemplar
        cantidad_de_libros += 1
        print("Libro agregado")
    else:
        print("Alcanzaste el maximo de libros")

def actualizar_ejemplares():
    nombre = input("Ingrese el título a actualizar: ")
    encontrado = False
    for i in range(cantidad_de_libros):
        if titulos[i] == nombre:
            nuevo = int(input("Ingrese la nueva cantidad de ejemplares que quiere: "))
            ejemplares[i] = nuevo
            print("Cantidad actualizada")
            encontrado = True
            break
    if not encontrado:
        print("Ese libro no esta")
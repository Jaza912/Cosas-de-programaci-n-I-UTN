def primera_aparicion(numero, valor):
    for i in range(len(numero)):
        if numero[i] == valor:
            return i + 1
    return -1

numero = [0] * 5
for i in range(5):
    numero[i] = int(input(f"Ingrese sus números {i+1}: "))
buscar = int(input("Ingrese el número a buscar: "))
posicion = primera_aparicion(numero,buscar)

if posicion != -1:
    print("El número se encontro en la posición:", posicion)
else:
    print("El número no esta en el array")
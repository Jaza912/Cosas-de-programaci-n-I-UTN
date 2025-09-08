numeros = [0] * 10
encontrado = False
for i in range (10):
    numeros [i] = int(input(f"Ingrese un número {i+1}: "))

verificar = int(input("Ingrese el número a buscar: "))
encontrado = False

for i in range (10):
    if numeros[i] == verificar:
        print("El número se encuentra en la posición:", i)
        encontrado = True
        break

if not encontrado:
    print("El número no se encuentra en el array:")
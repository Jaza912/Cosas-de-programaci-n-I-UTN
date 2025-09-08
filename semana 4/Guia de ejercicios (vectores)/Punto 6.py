numeros = [0] * 7
for i in range (7):
    numeros [i] = int(input(f"Ingrese un número {i+1}: "))

mayor = numeros[0]
posicion = 1
for i in range (1,7):
    if numeros[i] > mayor:
        mayor = numeros[i]
        posicion = i+1
print("El número mayor es:", mayor,"Y su posición es: ", posicion)
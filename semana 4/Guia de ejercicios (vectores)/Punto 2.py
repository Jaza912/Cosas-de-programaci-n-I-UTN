numeros = [0] * 10
suma = 0
for i in range (10):
    numeros [i] = int(input(f"Ingrese un número {i+1}: "))
    suma += numeros[i]
print("La suma de todos los elementos es:", suma)
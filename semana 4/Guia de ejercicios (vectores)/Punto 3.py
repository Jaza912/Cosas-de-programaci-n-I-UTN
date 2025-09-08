numeros = [0] * 6
suma = 0
for i in range (6):
    numeros [i] = float(input(f"Ingrese un número {i+1}: "))
    suma += numeros[i]

promedio = suma / 6 
print("La promedio de todos los elementos es:", promedio)
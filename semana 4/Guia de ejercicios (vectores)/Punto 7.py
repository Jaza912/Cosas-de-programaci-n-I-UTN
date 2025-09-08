numeros = [0] * 6
for i in range (6):
    numeros [i] = int(input(f"Ingrese un número {i+1}: "))

print("Array desde el ultimo hasta el primero:")
for i in range (5, -1, -1):
    print(numeros[i])
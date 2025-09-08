numeros = [0] * 8
contador = 0

for i in range(8):
    numeros[i] = int(input(f"Ingrese el número {i+1}: "))
    if numeros[i] > 100:
        contador += 1

print("Cantidad de números mayores a 100:", contador)

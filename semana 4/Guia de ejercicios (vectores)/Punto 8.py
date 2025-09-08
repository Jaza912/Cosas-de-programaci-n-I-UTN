numeros = [0] * 5
numeros2 = [0] * 5

print("---------Primer array---------")
for i in range (5):
    numeros [i] = int(input(f"Ingrese un número {i+1}: "))

print("n/---------Segundo array---------")
for i in range (5):
    numeros2 [i] = int(input(f"Ingrese un número {i+1}: "))
iguales = False
for i in range (5):
    if numeros == numeros2:
        print("Los arrays SON IGUALES")
        iguales = True
        break
if not iguales:
    print("Los arrays NO SON IGUALES")
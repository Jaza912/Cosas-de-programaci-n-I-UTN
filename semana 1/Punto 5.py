def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
    
num = int(input("Ingrese un número para verr si es par: "))
if es_par(num):
    print(f"Su numero {num} es par")
else:
    print(f"Su numero {num} es impar")
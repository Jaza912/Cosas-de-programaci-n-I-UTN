def verificacion_número(num):
    if num % 2 == 0:
        return True
    else:
        return False

numero = int(input("Ingrese un número: "))
if verificacion_número(numero):
        print("El número", numero,"es par")
else:
        print("El número",numero,"es impar")  
def verificacion_número(num):
    if num % 2 == 0:
        print("El número", num,"es par")
    else:
        print("El número",num,"es impar")  

num = int(input("Ingrese un número: "))
verificacion_número(num)
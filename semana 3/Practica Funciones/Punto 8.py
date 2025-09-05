def número_mayor(A,B,C):
    mayor = A
    if B > A:
        mayor = B
    elif C > A:
        mayor = C
    return mayor

num = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))
num3 = int(input("Ingrese otro número: "))
print("El número mayor es:",número_mayor(num,num2,num3))
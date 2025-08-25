def buscar_mayor (num1, num2, num3):
    numeros = [num1, num2, num3]
    numeros.sort(reverse = True)
    return numeros

numero1 = int(input("Ingrese un número: "))
numero2 = int(input("Ingrese otro número: "))
numero3 = int(input("Ingrese otro número: "))

resultado = buscar_mayor(numero1, numero2,numero3 )
print(f"los numeros ordenados: {resultado}")
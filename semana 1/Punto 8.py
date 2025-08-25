def calcular_edad(año_nacimiento):
    año_actual = 2025
    edad = año_actual - año_nacimiento
    return edad
año_que_nacio = int(input("Ingrese su año de nacimiento: "))
edad_usuario = calcular_edad(año_que_nacio)
print(f"Usted tiene {edad_usuario} años")
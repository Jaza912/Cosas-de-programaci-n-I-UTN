def verifificar_acceso(edad):
    return edad >= 18
edad_usuario = int(input("Inserte su edad: "))
if verifificar_acceso(edad_usuario):
    print("Sos mayor de edad, acceso permitido")
else:
    print("No sos mayor de edad, acceso denegado")
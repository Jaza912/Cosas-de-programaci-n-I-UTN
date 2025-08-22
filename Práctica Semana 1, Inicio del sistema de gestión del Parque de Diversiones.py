print("Bienvenido a PythonLand")
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

precio_montaña = 1500
precio_terror = 1200
precio_carrusel = 800

costo_total = 0
atracciones_usadas = ""

cantidad = int(input("¿Cuántas atracciones quiere usar? (máx. 3): "))

for x in range(cantidad):
    print("\nOpciones: 1) Montaña Rusa  2) Casa del Terror  3) Carrusel")
    opcion = int(input("Elija el número de la atracción: "))

    if opcion == 1:
        if edad >= 12:
            print("Puede subir a la Montaña Rusa")
            atracciones_usadas += "Montaña Rusa, "
            costo_total += precio_montaña
        else:
            print("No puede subir a la Montaña Rusa")
    elif opcion == 2:
        if edad >= 6:
            print("Puede entrar a la Casa del Terror")
            atracciones_usadas += "Casa del Terror, "
            costo_total += precio_terror
        else:
            print("No puede entrar a la Casa del Terror")
    elif opcion == 3:
        print("Puede subir al Carrusel")
        atracciones_usadas += "Carrusel, "
        costo_total += precio_carrusel
    else:
        print("Opción inválida")

print("RESUMEN")
print("Nombre:", nombre)
print("Edad:", edad)
print("Atracciones usadas:", atracciones_usadas)
print("Costo total: $", costo_total)
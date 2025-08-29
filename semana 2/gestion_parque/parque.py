def mostrar_atracciones():
    print("\nOpciones: ")
    print("1) Montaña Rusa  ($1500, desde 12 años)")
    print("2) Casa del Terror  ($1200, desde 6 años)")
    print("3) Carrusel  ($800, todas las edades)")


def puede_subir(edad, atraccion):
    if atraccion == 1 and edad >= 12:
        return True
    elif atraccion == 2 and edad >= 6:
        return True
    elif atraccion == 3:
        return True
    else:
        return False


def calcular_precio(atraccion):
    if atraccion == 1:
        return 1500
    elif atraccion == 2:
        return 1200
    elif atraccion == 3:
        return 800
    else:
        return 0


def registrar_visita():
    print("Bienvenido a PythonLand")
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))

    atracciones_usadas = ""
    costo_total = 0

    cantidad = int(input("¿Cuántas atracciones quiere usar? (máx. 3): "))

    for x in range(cantidad):
        mostrar_atracciones()
        opcion = int(input("Elija el número de la atracción: "))

        if puede_subir(edad, opcion):
            if opcion == 1:
                atracciones_usadas += "Montaña Rusa, "
            elif opcion == 2:
                atracciones_usadas += "Casa del Terror, "
            elif opcion == 3:
                atracciones_usadas += "Carrusel, "

            costo_total += calcular_precio(opcion)
            print("Puede usar esta atracción")
        else:
            print("No puede usar esta atracción")

    if cantidad >= 3:
        costo_total = int(costo_total * 0.9)

    resumen = {
        "nombre": nombre,
        "edad": edad,
        "atracciones": atracciones_usadas,
        "costo": costo_total
    }
    return resumen


def mostrar_resumen(resumen):
    print("\n--- RESUMEN ---")
    print("Nombre:", resumen["nombre"])
    print("Edad:", resumen["edad"])
    print("Atracciones usadas:", resumen["atracciones"])
    print("Costo total: $", resumen["costo"])

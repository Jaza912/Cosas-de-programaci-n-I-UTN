ATRACCIONES = {
    1: {"nombre": "Montaña Rusa", "precio": 1500, "edad_min": 12},
    2: {"nombre": "Casa del Terror", "precio": 1200, "edad_min": 6},
    3: {"nombre": "Carrusel", "precio": 800, "edad_min": 0},
}

def mostrar_atracciones():
    print("\nOpciones:")
    for clave, atraccion in ATRACCIONES.items():
        print(f"{clave}) {atraccion['nombre']} - ${atraccion['precio']}")

def puede_subir(edad, atraccion_id):
    atraccion = ATRACCIONES[atraccion_id]
    return edad >= atraccion["edad_min"]

def calcular_precio(atraccion_id):
    return ATRACCIONES[atraccion_id]["precio"]

def registrar_visita():
    print("Bienvenido a PythonLand")
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))

    costo_total = 0
    atracciones_usadas = []

    cantidad = int(input("¿Cuántas atracciones quiere usar? (máx. 3): "))

    for _ in range(cantidad):
        mostrar_atracciones()
        opcion = int(input("Elija el número de la atracción: "))

        if opcion in ATRACCIONES:
            if puede_subir(edad, opcion):
                atracciones_usadas.append(ATRACCIONES[opcion]["nombre"])
                costo_total += calcular_precio(opcion)
                print(f"Puede subir a {ATRACCIONES[opcion]['nombre']}")
            else:
                print(f"No puede subir a {ATRACCIONES[opcion]['nombre']}")
        else:
            print("Opción inválida")

    if len(atracciones_usadas) >= 3:
        costo_total *= 0.9

    resumen = {
        "nombre": nombre,
        "edad": edad,
        "atracciones": atracciones_usadas,
        "costo_total": costo_total
    }

    return resumen

def mostrar_resumen(resumen):
    print("\n--- RESUMEN ---")
    print("Nombre:", resumen["nombre"])
    print("Edad:", resumen["edad"])
    print("Atracciones usadas:", ", ".join(resumen["atracciones"]))
    print("Costo total: $", resumen["costo_total"])

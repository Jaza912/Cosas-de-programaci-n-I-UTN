from gestion_bibloteca import bibloteca

def main():
    opcion = 0
    while opcion != 7:
        print("\n--- Menu Bibloteca ---")
        print("1. Cargar titulos y ejemplares")
        print("2. Mostrar catalogo completo")
        print("3. Consultar disponibilidad")
        print("4. Listar titulos agotados")
        print("5. Agregar un nuevo titulo")
        print("6. Actualizar ejemplares (préstamo / devolución)")
        print("7. Salir")

        opcion = int(input("Elija una opcion: "))

        if opcion == 1:
            bibloteca.cargar()
        elif opcion == 2:
            bibloteca.catalogo()
        elif opcion == 3:
            bibloteca.consultar_disponibilidad()
        elif opcion == 4:
            bibloteca.libros_agotados()
        elif opcion == 5:
            bibloteca.agregar_titulo()
        elif opcion == 6:
            bibloteca.actualizar_ejemplares()
        elif opcion == 7:
            print("Usted salio del sistema")
        else:
            print("Opcion invalida, proba de nuevo.")

if __name__ == "__main__":
    main()
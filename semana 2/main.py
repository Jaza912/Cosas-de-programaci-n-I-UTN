from gestion_parque.parque import registrar_visita, mostrar_resumen

def main():
    print("Bienvenido a PythonLand")
    resumen = registrar_visita()
    mostrar_resumen(resumen)

if __name__ == "__main__":
    main()
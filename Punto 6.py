def convertir_minutos(minutos):
    horas = minutos // 60
    minutos_sobrantes = minutos % 60
    return horas, minutos_sobrantes

min = int(input("Ingrese la cantidad de minutos: "))
hs, mins = convertir_minutos(min)

print(f"{min} minutos equivalen a {hs} horas y {mins} minutos.")
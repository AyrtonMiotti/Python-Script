#Ejercicio 4: Alcancía mejorada.
print("ALCANCÍA MEJORADA")

objetivo = float(input("¿Cuánta plata querés ahorrar?: "))
while objetivo < 0:
    print("Por favor, escribí una cantidad positiva.")
    objetivo = float(input("¿Cuánta plata querés ahorrar?: "))

ahorrado = 0.0
while objetivo > ahorrado:
    ahorro = float(input("¿Cuánta plata querés meter en la alcancía?: "))
    while ahorro < 0:
        print("Por favor, escribí una cantidad positiva.")
        ahorro = float(input("¿Cuánta plata querés meter en la alcancía?: "))
    ahorrado += ahorro

print("Objetivo conseguido!", " Ahorraste $", ahorrado, " pesos")
#print(f"¡Objetivo conseguido! Ahorraste {ahorrado} pesos.") Avanzado.

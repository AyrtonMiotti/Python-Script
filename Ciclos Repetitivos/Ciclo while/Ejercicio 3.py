#Ejercicio 3: Alcancía
print("ALCANCÍA")
objetivo = float(input("¿Cuánta plata querés ahorrar?: "))
ahorrado = 0.0
while objetivo > ahorrado:
    ahorrado += float(input("¿Cuánta plata le vas a meter a la alcancía?: "))

print("Objetivo conseguido!", "Ahorraste $" ahorrado, " pesos")

#print(f"¡Objetivo conseguido! Ahorraste {ahorrado} pesos.") Más avanzada.

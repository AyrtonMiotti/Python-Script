# Ejercicio 3: Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista.

def sum (lista):
    suma = 0
    for i in lista:
        suma += i
    return suma
       
   
def multip (lista):
    multiplicacion = 1
    for i in lista:
        multiplicacion *= i
    return multiplicacion

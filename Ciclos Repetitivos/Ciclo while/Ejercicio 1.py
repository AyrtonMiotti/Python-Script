#Ejercicio 1: Escriba un programa que pregunte una y otra vez si desea continuar con el programa, siempre que se conteste exactamente sí (en minúsculas y con tilde).
  print("DIGA sí PARA CONTINUAR")
  respuesta = input("¿Desea continuar el programa?: ")

  while respuesta == "sí":
      respuesta = input("¿Desea continuar el programa?: ")

  print("¡Hasta la vista!")

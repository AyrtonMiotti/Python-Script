#Ejercicio 2: Escriba un programa que solicite una contraseña (el texto de la contraseña no es importante) y la vuelva a solicitar hasta que las dos contraseñas coincidan.

  print("CONFIRME SU CONTRASEÑA")
  password_1 = input("Escriba su contraseña: ")
  password_2 = input("Escriba de nuevo su contraseña: ")

  while password_1 != password_2:
      print("Las contraseñas no coinciden. Inténtelo de nuevo.")
      password_1 = input("Escriba su contraseña: ")
      password_2 = input("Escriba de nuevo su contraseña: ")

  print("Contraseña confirmada. ¡Nos vemosss!")

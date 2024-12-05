import secrets, string, os

def limpiar_consola():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')

def comprobar(largo):
  while not largo.isdigit() or int(largo) <= 0:
      largo = input("Por favor ingrese solo numeros mayores a 0: ")
      print()
  return int(largo)

def mostrar_clave(password):
  limpiar_consola()
  print("-" * 50)
  print("Su clave ha sido generada con EXITO!!!!!:")
  print("-" * 50)
  print("Su clave es: ",password)
  print("-" * 50)
  os.system("pause")
  limpiar_consola()

opcion = -1

diccionario = {
              'letras': string.ascii_letters,
              'numeros': string.digits,
              'caracteres': string.punctuation
}

print ("=============================================================")
print ("||Bienvenidos al programa de Generacion de Claves v1.0||")
print ("=============================================================")
print ()

while opcion != "0":
  print("Seleccione el tipo de clave a generar:\n")
  print("1. Generar contraseña solo de letras.")
  print("2. Generar contraseña solo de numeros.")
  print("3. Generar contraseña con letras y numeros.")
  print("4. Generar contraseña con letras, numeros y caracteres especiales.")
  print("0. Salir\n")
  
  opcion = input("Ingrese su opcion: ")
  
  print()

  password = ""

  match opcion:
      
      case "1":
        longitud = input("Ingrese la longitud de su clave: ")
        
        longitud = comprobar(longitud)
        print()

        for _  in range(longitud):
          password += secrets.choice(diccionario['letras'])
        
        mostrar_clave(password)
      
      case "2":
        longitud = input("Ingrese la longitud de su clave: ")
        
        longitud = comprobar(longitud)
        
        for _  in range(longitud):
          password += secrets.choice(diccionario['numeros'])
        
        mostrar_clave(password)
      
      case "3":
        longitud = input("Ingrese la longitud de su clave: ")
        
        longitud = comprobar(longitud)
        
        for _  in range(longitud):
          password += secrets.choice(diccionario['letras'] + diccionario['numeros'])
        
        mostrar_clave(password)
      
      case "4":
        longitud = input("Ingrese la longitud de su clave: ")
        
        longitud = comprobar(longitud)
        
        for _  in range(longitud):
          password += secrets.choice(diccionario['letras'] + diccionario['numeros'] + diccionario['caracteres'])
        
        mostrar_clave(password)
      
      case "0":
        print ("Muchas Gracias!!!")
        print ()
      
      case _:
        print ("Opcion no valida. Intente de nuevo.")
        print () 
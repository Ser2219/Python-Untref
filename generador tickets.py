import pickle, sys, os, random

def limpiar_consola():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')

def validar_continuar(comprobar):
	while comprobar != "N" and comprobar != "S":
		comprobar = input("Recuerde que solo debe responder S o N..... Desea generar otro ticket (S/N)?: ").upper()
						
		limpiar_consola()
	
	return comprobar

def validar_continuar2(comprobar):
	while comprobar != "N" and comprobar != "S":
		comprobar = input("Recuerde que solo debe responder S o N..... Desea verificar otro ticket (S/N)?: ").upper()
						
		limpiar_consola()
	
	return comprobar

def mostrar_ticket(j):
        print(f"""
###################### N° de ticket: {j["nroticket"]} ################################     
            
        Nombre: {j["nombre"]}	Sector: {j["sector"]}		Asunto: {j["asunto"]}
		
	Mensaje:{j["mensaje"]}

###########################################################################
"""
        )

opcion = -1

while opcion != 3:
		print("Seleccione una opción:\n")
		print("1. Generar un ticket")
		print("2. Ver un ticket ya generado")
		print("3. Salir\n")
		
		opcion = int(input ("Seleccione una opcion: "))
		print()

		match opcion:
	
			case 1:
				seguir = "S"
				while seguir != "N":
					print("Ingrese los datos para generar un nuevo Ticket\n")
					nombre = input("Ingrese su nombre y apellido: ")
					sector = input("Ingrese su sector: ")
					asunto = input("Ingrese el asunto del mensaje: ")
					mensaje = input("Ingrese la descripcion del problema: ")
					numero_random = random.randrange(1000, 9999)
				
					datos_ticket = {"nombre": nombre,"sector": sector,"asunto": asunto,"mensaje": mensaje, "nroticket": numero_random}
				
					mostrar_ticket(datos_ticket)
					print(f"""		POR FAVOR RECUERDE SU N° DE TICKET!!!

###########################################################################
"""
					)
					os.system("pause")
				
					ruta = "reclamo/ticket_"+str(numero_random)
				
					with open(ruta, "wb") as f:
						pickle.dump(datos_ticket, f)
					
					seguir = input("Desea generar otro ticket (S/N)?: ").upper()
					print ()
					
					seguir = validar_continuar(seguir)
					
					limpiar_consola()

				limpiar_consola()

			case 2:
				seguir = "S"
				while seguir != "N":
					n_ticket = input("Ingrese numero de ticket que desea verificar: ")
					
					rutax ="reclamo/ticket_"+n_ticket
					
					if os.path.isfile(rutax):
						with open(rutax, "rb") as f:
							ticketx = pickle.load(f)
							mostrar_ticket(ticketx)
							os.system("pause")
					else:
						print("No exite un ticket con ese numero")

					seguir = input("Desea verificar otro ticket (S/N)?: ").upper()
					print ()

					seguir = validar_continuar2(seguir)
					
					limpiar_consola()
				
				limpiar_consola()

			case 3:
				print ("Muchas Gracias!!!")
				print ()

			case _:
				print ("Opcion no valida. Intente de nuevo.")
				print ()
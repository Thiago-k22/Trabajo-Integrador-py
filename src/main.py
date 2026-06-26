from logica import crear_personaje, crear_enemigo, combate

print("=== CREACIÓN DE PERSONAJE ===")
print("1 - Guerrero")
print("2 - Mago")
print("3 - Arquero")
print("4 - Asesino")

opcion = int(input("Seleccione una clase: "))
nombre = input("Ingrese el nombre del personaje: ")

personaje = crear_personaje(opcion, nombre)

if personaje:

    print("Personaje creado correctamente.")

    enemigo = crear_enemigo()

    print(f"\nHa aparecido un enemigo: {enemigo.get_nombre()}!")

    combate(personaje, enemigo)

else:
    print("Opción inválida.")

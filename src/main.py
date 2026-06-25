from logica import crear_personaje

print("=== CREACIÓN DE PERSONAJE ===")
print("1 - Guerrero")
print("2 - Mago")
print("3 - Arquero")
print("4 - Asesino")

opcion = int(input("Seleccione una clase: "))
nombre = input("Ingrese el nombre del personaje: ")

personaje = crear_personaje(opcion, nombre)

if personaje:
    print(f"\nPersonaje creado correctamente.")
    print(f"Nombre: {personaje._nombre}")
else:
    print("Opción inválida.")

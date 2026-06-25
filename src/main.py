from Clases import Guerrero, Mago, Arquero

def crear_personaje(opcion, nombre):

    if opcion == 1:
        return Guerrero(nombre, 100, 15, 10)

    elif opcion == 2:
        return Mago(nombre, 80, 20, 50)

    elif opcion == 3:
        return Arquero(nombre, 90, 12, 20)

    elif opcion == 4:
        return Asesino(nombre, 60, 35, 25)

    else:
        return None


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

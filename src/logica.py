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

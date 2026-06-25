from clases import Guerrero, Mago, Arquero, Asesino

def crear_personaje(opcion, nombre):

    if opcion == 1:
        return Guerrero(nombre, 100, 15, 2, 10)

    elif opcion == 2:
        return Mago(nombre, 80, 20, 2, 50)

    elif opcion == 3:
        return Arquero(nombre, 90, 12, 2, 20)

    elif opcion == 4:
        return Asesino(nombre, 60, 35, 2, 25)

    else:
        return None

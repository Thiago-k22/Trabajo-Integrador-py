import random
from clases import Guerrero, Mago, Arquero, Asesino

def crear_personaje(opcion, nombre):

    if opcion == 1:
        return Guerrero(nombre, 100, 15, 2, 10)

    elif opcion == 2:
        return Mago(nombre, 80, 20, 2, 50)

    elif opcion == 3:
        return Arquero(nombre, 90, 12, 2, 20)

    elif opcion == 4:
        return Asesino(nombre, 60, 35, 2, 0.25)

    else:
        return None

def crear_enemigo():
    enemigos = [
        Guerrero("Orco", 100, 15, 0, 8),
        Mago("Hechicero", 80, 20, 0, 40),
        Arquero("Cazador", 90, 12, 0, 10),
        Asesino("Bandido", 70, 18, 0, 0.25)
    ]

    return random.choice(enemigos)


def combate(jugador, enemigo):

    print("\n===== COMBATE =====")

    while jugador.esta_vivo() and enemigo.esta_vivo():

        print(f"\n{jugador.get_nombre()} ({jugador.get_salud()} HP)")
        print(f"{enemigo.get_nombre()} ({enemigo.get_salud()} HP)")

        print("\n1. Atacar")
        print("2. Habilidad especial")
        print("3. Usar poción")

        opcion = input("Seleccione una acción: ")

        if opcion == "1":
            jugador.atacar(enemigo)

        elif opcion == "2":
            jugador.habilidad_especial(enemigo)

        elif opcion == "3":
            jugador.usar_pociones()

        else:
            print("Opción inválida.")
            continue

        if enemigo.esta_vivo():
            print(f"\nTurno de {enemigo.get_nombre()}")
            enemigo.atacar(jugador)

    print("\n===== FIN DEL COMBATE =====")

    if jugador.esta_vivo():
        print(f"¡{jugador.get_nombre()} ganó la batalla!")
    else:
        print(f"{enemigo.get_nombre()} ganó la batalla.")

import random #importamos la libreria random para trabajar con % y ia (osea, .choice,etc)
class Personaje:
    def __init__(self, nombre, salud, ataque):
        self._nombre = str(nombre) #encapsulamiento, utilizamos metodo get para obtener los resultados
        self._salud_maxima = int(salud)
        self._salud = int(salud)
        self._ataque = int(ataque)

    def get_nombre(self):
        return self._nombre 

    def get_salud(self):
        return self._salud

    def esta_vivo(self):
        return self._salud > 0

    def recibir_dmg(self, cantidad):
        self._salud -= int(cantidad)
        if self._salud < 0:
            self._salud = 0
        print(f"   {self._nombre} recibio {cantidad} de daño. (Salud: {self._salud}/{self._salud_maxima})")

    def atacar(self, objetivo):
        pass  #aplicamos polimorfismo (mismo metodos, pero se comportan dif)

    def habilidad_especial(self, objetivo):
        pass



#  SUBCLASES 


class Guerrero(Personaje):
    def __init__(self, nombre, salud, ataque, armadura):
        super().__init__(nombre, salud, ataque)
        self._armadura = int(armadura)

    def atacar(self, objetivo):
        daño_extra = random.randint(1, 5) #elige un numero entero entre a y b, sumando al danio total
        daño_total = self._ataque + daño_extra
        print(f"{self._nombre} golpea con su Espada Pesada a {objetivo.get_nombre()}!")
        objetivo.recibir_dmg(daño_total)

    def habilidad_especial(self, objetivo):
        multiplicador_impacto = random.randint(1, 3)
        daño_escudo = self._ataque + (self._armadura * multiplicador_impacto)
        print(f"{self._nombre} usa 'Golpe de Escudo' contra {objetivo.get_nombre()}!")
        objetivo.recibir_dmg(daño_escudo)


class Mago(Personaje):
    def __init__(self, nombre, salud, ataque, mana):
        super().__init__(nombre, salud, ataque)
        self._mana = int(mana)

    def atacar(self, objetivo):
        print(f"{self._nombre} lanza un 'Proyectil Magico' basico a {objetivo.get_nombre()}.")
        objetivo.recibir_dmg(self._ataque)

    def habilidad_especial(self, objetivo):
        if self._mana >= 15:
            self._mana -= 15
            daño_fuego = self._ataque + random.randint(15, 30)
            print(f" {self._nombre} gasta 15 de mana y desata una 'Bola de Fuego' sobre {objetivo.get_nombre()}! (Mana: {self._mana})")
            objetivo.recibir_dmg(daño_fuego)
        else:
            print(f"{self._nombre} no tiene suficiente mana ({self._mana}/15). ¡Su hechizo falla!")
            objetivo.recibir_dmg(3)


class Arquero(Personaje):
    def __init__(self, nombre, salud, ataque, flechas):
        super().__init__(nombre, salud, ataque)
        self._flechas = int(flechas)

    def atacar(self, objetivo):
        if self._flechas > 0:
            self._flechas -= 1
            daño = self._ataque + random.randint(2, 8)
            print(f" {self._nombre} dispara una flecha certera a {objetivo.get_nombre()}. (Flechas: {self._flechas})")
            objetivo.recibir_dmg(daño)
        else:
            print(f" {self._nombre} se quedo sin flechas! Golpea debilmente con el arco.")
            objetivo.recibir_dmg(4)

    def habilidad_especial(self, objetivo):
        if self._flechas >= 2:
            self._flechas -= 2
            daño_1 = self._ataque + random.randint(1, 4)
            daño_2 = self._ataque + random.randint(1, 4)
            daño_total = daño_1 + daño_2
            print(f" {self._nombre} gasta 2 flechas y ejecuta 'Disparo Doble' contra {objetivo.get_nombre()}!")
            objetivo.recibir_dmg(daño_total)
        else:
            print(f" {self._nombre} no tiene suficientes flechas para la habilidad especial.")


class Asesino(Personaje):
    def __init__(self, nombre, salud, ataque, probabilidad_critico):
        super().__init__(nombre, salud, ataque)
        self._critico = float(probabilidad_critico)

    def atacar(self, objetivo):
        if random.random() < self._critico: #.random elegi un porcentaje entre 0 y 1.0            
            daño_total = self._ataque * 2
            print(f"¡GOLPE CRITICO! {self._nombre} encontro un punto vital en {objetivo.get_nombre()}!")
        else:
            daño_total = self._ataque + random.randint(1, 3)
            print(f" {self._nombre} ataca rapidamente con sus dagas a {objetivo.get_nombre()}.")
        objetivo.recibir_dmg(daño_total)

    def habilidad_especial(self, objetivo):
        daño_veneno = self._ataque + random.randint(8, 15)
        print(f" {self._nombre} usa 'Hoja Envenenada' inyectando toxinas a {objetivo.get_nombre()}!")
        objetivo.recibir_dmg(daño_veneno)
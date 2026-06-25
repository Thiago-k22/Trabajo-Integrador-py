class Personaje:
    def __init__(self, nombre, vida, ataque):
       self.nombre = nombre
       self.vida = vida
       self.ataque = ataque
    
    def atacar(self):
       pass

class Enemigo(Personaje):
    def __init__(self, nombre, vida, ataque, debilidad):
        super().__init__(nombre, vida, ataque)
        self.debilidad = debilidad

    def atacar(self):
       if self.vida > 0:
        print(f"{self.nombre} tiene {self.vida} de vida, ataca con {self.ataque} y es débil a {self.debilidad}")

#personaje creado para demostracion del codigo
enemigo1= Enemigo("Demonio", 100, "puño de fuego", "lapizlazuli")
enemigo1.atacar()


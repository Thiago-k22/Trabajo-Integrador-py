class Personaje:
  def __init__(self, nombre, vida, ataque):
    self.nombre = nombre
    self.vida = vida
    self.ataque = ataque
    
  def atacar(self):
    pass

class Mago(Personaje):
    def __init__(self, nombre, vida, ataque, magia):
        super().__init__(nombre, vida, ataque)
        self.magia = magia
    
    def atacar(self):
        if self.vida > 0:
           print(f"{self.nombre} ataca con {self.ataque} y tiene {self.magia} de magia")

#personaje creado para demostracion del codigo
mago1= Mago("Willian",85,"postura de fuego",234)
mago1.atacar()

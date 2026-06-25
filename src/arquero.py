class Personaje:
  def __init__(self, nombre, vida, ataque):
    self.nombre = nombre
    self.vida = vida
    self.ataque = ataque
    
  def atacar(self):
    pass

class Arquero(Personaje):
    def __init__(self, nombre, vida, ataque,flechas):
      super().__init__(nombre, vida, ataque)
      self.flechas = flechas

    def atacar(self):
        if self.flechas > 0:
          print(f"{self.nombre} tiene {self.vida} de vida, ataca con {self.ataque} y tiene {self.flechas} flechas restantes")
          self.flechas -= 1
#personaje creado para demostracion del codigo
arquero1 = Arquero("Squeleton", 86,"arco encantado", 45 )
arquero1.atacar()
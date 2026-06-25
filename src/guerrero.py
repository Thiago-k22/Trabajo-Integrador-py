
class Personaje:
  def __init__(self, nombre, vida, ataque):
    self.nombre = nombre
    self.vida = vida
    self.ataque = ataque
    
  def atacar(self):
    pass



class Guerrero(Personaje):
  def __init__(self, nombre, vida, ataque, escudo):
    super().__init__(nombre, vida, ataque)
    self.escudo = escudo

  def atacar(self):
    if self.vida > 0:
      print(f"{self.nombre} tiene {self.vida} de vida, ataca con {self.ataque} y se protege {self.escudo}")
  

#personaje creado para demostracion del codigo
guerrero1= Guerrero("Levi",100,"patada guiratoria","bloqueo de escudo")
guerrero1.atacar()

Mermaidxp
 class PersonajeFactory {
       +crear_personaje(tipo) Personaje
   }

    class Personaje {
        -_nombre
        -_salud
        -_salud_maxima
        -_ataque
        -_pocion
        +get_nombre()
        +get_salud()
        +esta_vivo()
        +recibir_dmg()
        +atacar()
        +habilidad_especial()
        +usar_pociones()
    }

    class Guerrero {
        -_armadura
        +atacar()
        +habilidad_especial()
        +usar_pociones()

    }

    class Mago {
        -_mana
        +atacar()
        +habilidad_especial()
        +usar_pociones()
        

    }

    class Arquero {
        -_flechas
        +atacar()
        +habilidad_especial()
        +usar_pociones()
        
    }

    class Asesino {
        -_critico
        +atacar()
        +habilidad_especial()
        +usar_pociones()
        
    }

    Personaje <|-- Guerrero
    Personaje <|-- Mago
    Personaje <|-- Arquero
    Personaje <|-- Asesino
    PersonajeFactory ..> Personaje : crea




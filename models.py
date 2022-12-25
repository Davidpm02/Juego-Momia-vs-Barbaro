import random


"""La clase 'Dado' sera la encargada de proporcionarnos un numero aleatorio de entre una lista de numeros.
    args:
    
    mtds:
    - tira()
"""
class Dado():
    def tira():
        listaNumeros = [1,2,3,4,5,6]
        numeroElegido = random.choice(listaNumeros)
        return numeroElegido




"""La clase 'Personaje' inicializara los personajes protagonistas de nuestros juegos. Posteriormente,
   personajes se definiran en clases mas especificas que heredaran de la clase 'Personaje'.
   
   args:
   - nombre
   - vida
   - ataque
   - defensa
   
   mtds:
   - atacar()
   - estarVivo()
"""
class Personaje():
    def __init__(self,nombre,vida,ataque,defensa):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
    
    def atacar(self):
        listaResultados = []
        for num in range(self.ataque):
            listaResultados.append(Dado.tira())
        ataquesValidos = []
        for item in listaResultados:
            if item > 3:
                ataquesValidos.append(item)
        n_av = len(ataquesValidos)
        return n_av
    
    def estarVivo(self):
        if self.vida > 0:
            return True
        else:
            return False
    
    def __str__(self):
        return '''Nombre --> {}
                  Vida   --> {}
                  Ataque --> {}
                  Defensa -> {}'''.format(self.nombre,
                                          self.vida,
                                          self.ataque,
                                          self.defensa)




     # ------------------------------------------- CLASES MOMIA Y BARBARO ----------------------------------------------- #


""" Esta es la clase especifica que defina a uno de nuestros personajes protagonistas. La clase hereda de la superclase
    'Personaje', y anade un nuevo metodo.
    args:
    - nombre (Personaje)
    - vida (Personaje)
    - ataque (Personaje)
    - defensa (Personaje)
    
    mtds:
    - atacar (Personaje)
    - estarVivo (Personaje)
    - defender
"""
class Momia(Personaje):
    def __init__(self,nombre,vida,ataque,defensa):
        Personaje.__init__(self,nombre,vida,ataque,defensa)
    
    def defender(self, numImpactos): # Representa el numero de impactos de los que el personaje se tiene que intentar defender.
        contadorImpactos = 0
        for num in range(self.defensa):
            Dado.tira()
            if Dado != 6:
                contadorImpactos +=1
            else:
                pass
            numImpactos-=1
            if numImpactos == 0:
                self.vida -= contadorImpactos
                break
        return contadorImpactos
        
    
    def __str__(self):
        return Personaje.__str__(self)
    
 
 
    
   
    
""" Esta es la clase especifica que defina a uno de nuestros personajes protagonistas. La clase hereda de la superclase
    'Personaje', y anade un nuevo metodo.
    args:
    - nombre (Personaje)
    - vida (Personaje)
    - ataque (Personaje)
    - defensa (Personaje)
    
    mtds:
    - atacar (Personaje)
    - estarVivo (Personaje)
    - defender
"""
class Barbaro(Personaje):
    def __init__(self,nombre,vida,ataque,defensa):
        Personaje.__init__(self,nombre,vida,ataque,defensa)
    
    def defender(self, numImpactos): # Representa el numero de impactos de los que el personaje se tiene que intentar defender.
        contadorImpactos = 0
        for num in range(self.defensa):
            Dado.tira()
            if Dado !=5 or Dado !=6:
                contadorImpactos +=1
            else:
                pass
            numImpactos-=1
            if numImpactos == 0:
                self.vida -= contadorImpactos
                break
        return contadorImpactos
    
    def __str__(self):
        return Personaje.__str__(self)
    
    
    #--------------------------------------------------------------------------------------------------------------------#

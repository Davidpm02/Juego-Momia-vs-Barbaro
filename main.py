import random

from models import Momia, Barbaro

def comprobarVelocidad(personaje1,personaje2):
    if personaje1.velocidad > personaje2.velocidad:
        resultado = '''El personaje {} es mas rapido que el personaje {}!\nEl personaje {} comienza el ataque antes.'''.format(personaje1.nombre,
                                                                                                                              personaje2.nombre,
                                                                                                                              personaje1.nombre)
    elif personaje1.velocidad < personaje2.velocidad:
        resultado = '''El personaje {} es mas rapido que el personaje {}!\nEl personaje {} comienza el ataque antes.'''.format(personaje2.nombre,
                                                                                                                              personaje1.nombre,
                                                                                                                              personaje2.nombre)
    else:
        resultado = '''Ha ocurrido un error al comprobar la velocidad de los personajes.'''
        
    return print(resultado)
        

def jugarPartida(personaje1,personaje2):  #personaje1 = Barbaro, personaje2 = Momia
    totalTurnos = int(input("Seleccione el numero de turnos que desea jugar:"))
    
    print('\n'*5)
    print('*'*50)
    print('\n'*2)
    print("El numero total de turnos establecido es de {} turnos.".format(totalTurnos))
    print('\n'*2)
    comprobarVelocidad(personaje1,personaje2)
    print('*'*50)
    print('\n'*2)
    
    
    contador = 1
    while True:
        if totalTurnos > 0:
            try:
                assert personaje1.estarVivo() == True and personaje2.estarVivo() == True
                if personaje1.velocidad >= personaje2.velocidad:
                    print('# TURNO {} >> {} vs {}'.format(contador,
                                                          type(personaje1).__name__.upper(),
                                                          type(personaje2).__name__.upper()))
                    #-----------------
                    
                    tirada = 0
                    for num in range(1):
                        tirada = random.randint(1,2)
                        
                    if tirada == 1:     # ---> SI TIRADA ==1 , ATAQUE FISICO, SI TIRADA == 2, ATAQUE ESPECIAL
                    #-----------------
                        ataquesRealizados = personaje1.atacar()
                        personaje2.defender(ataquesRealizados)
                        print('{} {} no pudo bloquear {} impactos FISICOS y queda con {} de vida.'.format(type(personaje2).__name__,
                                                                                                          personaje2.nombre,
                                                                                                          ataquesRealizados,
                                                                                                          personaje2.vida))
                        posibleCritico = personaje1.atacar()   # .atacar() devuelve un entero que representa la cantidad de golpes validos
                        if personaje1.ataque_fisico < 3:
                            if posibleCritico == 2 :
                                nuevoAtaque = 1
                                personaje2.defender(nuevoAtaque)
                                print('**** {} {} no pudo bloquear {} GOLPE CRITICO y queda con {} de vida. ****'.format(type(personaje2).__name__,
                                                                                                                         personaje2.nombre,
                                                                                                                         nuevoAtaque,
                                                                                                                         personaje2.vida))
                        elif personaje1.ataque_fisico >= 3:
                            if posibleCritico == 3 :
                                nuevoAtaque = 1
                                personaje2.defender(nuevoAtaque)
                                print('**** {} {} no pudo bloquear {} GOLPE CRITICO y queda con {} de vida. ****'.format(type(personaje2).__name__,
                                                                                                                         personaje2.nombre,
                                                                                                                         nuevoAtaque,
                                                                                                                         personaje2.vida))
                                
                                
                        contador +=1
                        totalTurnos -=1
                        print("-----TURNOS RESTANTES: {} -----".format(totalTurnos))
                        ataquesRealizados = 0
                    
                    elif tirada == 2:
                        
                        ataquesRealizados = personaje1.atacarEspecial()
                        personaje2.defenderEspecial(ataquesRealizados)
                        print('{} {} no pudo bloquear {} impactos ESPECIALES y queda con {} de vida.'.format(type(personaje2).__name__,
                                                                                                             personaje2.nombre,
                                                                                                             ataquesRealizados,
                                                                                                             personaje2.vida))
                        
                        posibleCritico = personaje1.atacarEspecial()   # .atacar() devuelve un entero que representa la cantidad de golpes validos
                        if personaje1.ataque_especial < 3:
                            if posibleCritico == 2 :
                                nuevoAtaque = 1
                                personaje2.defenderEspecial(nuevoAtaque)
                                print('**** {} {} no pudo bloquear {} GOLPE CRITICO y queda con {} de vida. ****'.format(type(personaje2).__name__,
                                                                                                                            personaje2.nombre,
                                                                                                                            nuevoAtaque,
                                                                                                                            personaje2.vida))
                        elif personaje1.ataque_especial >= 3:
                            if posibleCritico == 3 :
                                nuevoAtaque = 1
                                personaje2.defenderEspecial(nuevoAtaque)
                                print('**** {} {} no pudo bloquear {} GOLPE CRITICO y queda con {} de vida. ****'.format(type(personaje2).__name__,
                                                                                                                            personaje2.nombre,
                                                                                                                            nuevoAtaque,
                                                                                                                            personaje2.vida))
                                
                                
                        contador +=1
                        totalTurnos -=1
                        print("-----TURNOS RESTANTES: {} -----".format(totalTurnos))
                        ataquesRealizados = 0
                        
                else:
                    print('# TURNO {} >> {} vs {}'.format(contador,
                                                         type(personaje2).__name__.upper(),
                                                         type(personaje1).__name__.upper()))
                    
                    #-----------------
                    
                    tirada = 0
                    for num in range(1):
                        tirada = random.randint(1,2)
                        
                    if tirada == 1:     # ---> SI TIRADA ==1 , ATAQUE FISICO, SI TIRADA == 2, ATAQUE ESPECIAL
                    #-----------------
                    
                        ataquesRealizados = personaje2.atacar()
                        personaje1.defender(ataquesRealizados)
                        print('El {} {} no pudo bloquear {} impactos FISICOS y queda con {} de vida.'.format(type(personaje1).__name__,
                                                                                                    personaje1.nombre,
                                                                                                    ataquesRealizados,
                                                                                                    personaje1.vida))
                        posibleCritico = personaje2.atacar()   # .atacar() devuelve un entero que representa la cantidad de golpes validos
                        if personaje2.ataque_fisico < 3:
                            if posibleCritico == 2:
                                nuevoAtaque = 1
                                personaje1.defender(nuevoAtaque)
                                print('**** El {} {} no pudo bloquear {} GOLPE CRITICO y queda con {} de vida. ****'.format(type(personaje1).__name__,
                                                                                                                            personaje1.nombre,
                                                                                                                            nuevoAtaque,
                                                                                                                            personaje1.vida))
                        elif personaje2.ataque_fisico >= 3:
                            if posibleCritico == 3:
                                nuevoAtaque = 1
                                personaje1.defender(nuevoAtaque)
                                print('**** El {} {} no pudo bloquear {} GOLPE CRITICO y queda con {} de vida. ****'.format(type(personaje1).__name__,
                                                                                                                            personaje1.nombre,
                                                                                                                            nuevoAtaque,
                                                                                                                            personaje1.vida))
                        contador +=1
                        totalTurnos -=1
                        print("-----TURNOS RESTANTES: {} -----".format(totalTurnos))
                        ataquesRealizados = 0
                    
                    elif tirada == 2:
                        
                        ataquesRealizados = personaje2.atacarEspecial()
                        personaje1.defenderEspecial(ataquesRealizados)
                        print('{} {} no pudo bloquear {} impactos ESPECIALES y queda con {} de vida.'.format(type(personaje1).__name__,
                                                                                                    personaje1.nombre,
                                                                                                    ataquesRealizados,
                                                                                                    personaje1.vida))
                        
                        posibleCritico = personaje2.atacarEspecial()   # .atacar() devuelve un entero que representa la cantidad de golpes validos
                        if personaje2.ataque_especial < 3:
                            if posibleCritico == 2 :
                                nuevoAtaque = 1
                                personaje1.defenderEspecial(nuevoAtaque)
                                print('**** {} {} no pudo bloquear {} GOLPE CRITICO y queda con {} de vida. ****'.format(type(personaje1).__name__,
                                                                                                                            personaje1.nombre,
                                                                                                                            nuevoAtaque,
                                                                                                                            personaje1.vida))
                        elif personaje2.ataque_especial >= 3:
                            if posibleCritico == 3 :
                                nuevoAtaque = 1
                                personaje1.defenderEspecial(nuevoAtaque)
                                print('**** {} {} no pudo bloquear {} GOLPE CRITICO y queda con {} de vida. ****'.format(type(personaje1).__name__,
                                                                                                                            personaje1.nombre,
                                                                                                                            nuevoAtaque,
                                                                                                                            personaje1.vida))
                                
                                
                        contador +=1
                        totalTurnos -=1
                        print("-----TURNOS RESTANTES: {} -----".format(totalTurnos))
                        ataquesRealizados = 0
                    
            except AssertionError:
                if personaje1.estarVivo() == False and personaje2.estarVivo() == True:
                    print("""> GANADOR {} {}
                           >>> {} {} con {} de vida.
                           >>> {} {} con {} de vida.""".format(type(personaje2).__name__.upper(),
                                                                    personaje2.nombre,
                                                                    type(personaje2).__name__,
                                                                    personaje2.nombre,
                                                                    personaje2.vida,
                                                                    type(personaje1).__name__,
                                                                    personaje1.nombre,
                                                                    0))
                    print('--- TOTAL TURNOS JUGADOS: {} ---'.format(contador -1))
                    print('\n'*2)
                    print('*'*50)
                    print('\n'*5)
                    totalTurnos = 0  
                elif personaje1.estarVivo() == True and personaje2.estarVivo() == False:
                    print("""> GANADOR {} {}
                           >>> {} {} con {} de vida.
                           >>> {} {} con {} de vida.""".format(type(personaje1).__name__.upper(),
                                                                  personaje1.nombre,
                                                                  type(personaje1).__name__,
                                                                  personaje1.nombre,
                                                                  personaje1.vida,
                                                                  type(personaje2).__name__,
                                                                  personaje2.nombre,
                                                                  0))
                    print('--- TOTAL TURNOS JUGADOS: {} ---'.format(contador -1))
                    print('\n'*2)
                    print('*'*50)
                    print('\n'*5)
                totalTurnos = 0
                break
                
            
            
            
            try:
                assert personaje1.estarVivo() == True and personaje2.estarVivo() == True
                if personaje2.velocidad < personaje1.velocidad:
                    print('# TURNO {} >> {} vs {}'.format(contador,
                                                               type(personaje2).__name__.upper(),
                                                               type(personaje1).__name__.upper()))
                    
                    #-----------------
                    
                    tirada = 0
                    for num in range(1):
                        tirada = random.randint(1,2)
                        
                    if tirada == 1:     # ---> SI TIRADA ==1 , ATAQUE FISICO, SI TIRADA == 2, ATAQUE ESPECIAL
                    #-----------------
                    
                        ataquesRealizados = personaje2.atacar()
                        personaje1.defender(ataquesRealizados)
                        print('El {} {} no pudo bloquear {} impactos FISICOS y queda con {} de vida.'.format(type(personaje1).__name__,
                                                                                                    personaje1.nombre,
                                                                                                    ataquesRealizados,
                                                                                                    personaje1.vida))
                        posibleCritico = personaje2.atacar()   # .atacar() devuelve un entero que representa la cantidad de golpes validos
                        if personaje2.ataque_fisico < 3:
                            if posibleCritico == 2:
                                nuevoAtaque = 1
                                personaje1.defender(nuevoAtaque)
                                print('**** El {} {} no pudo bloquear {} GOLPE CRITICO y queda con {} de vida. ****'.format(type(personaje1).__name__,
                                                                                                                            personaje1.nombre,
                                                                                                                            nuevoAtaque,
                                                                                                                            personaje1.vida))
                        elif personaje2.ataque_fisico >= 3:
                            if posibleCritico == 3:
                                nuevoAtaque = 1
                                personaje1.defender(nuevoAtaque)
                                print('**** El {} {} no pudo bloquear {} GOLPE CRITICO y queda con {} de vida. ****'.format(type(personaje1).__name__,
                                                                                                                            personaje1.nombre,
                                                                                                                            nuevoAtaque,
                                                                                                                            personaje1.vida))
                        contador +=1
                        totalTurnos -=1
                        print("-----TURNOS RESTANTES: {} -----".format(totalTurnos))
                        ataquesRealizados = 0
                    
                    elif tirada == 2:
                        ataquesRealizados = personaje2.atacarEspecial()
                        personaje1.defenderEspecial(ataquesRealizados)
                        print('{} {} no pudo bloquear {} impactos ESPECIALES y queda con {} de vida.'.format(type(personaje1).__name__,
                                                                                                             personaje1.nombre,
                                                                                                             ataquesRealizados,
                                                                                                             personaje1.vida))
                        
                        posibleCritico = personaje2.atacarEspecial()   # .atacar() devuelve un entero que representa la cantidad de golpes validos
                        if personaje2.ataque_especial < 3:
                            if posibleCritico == 2 :
                                nuevoAtaque = 1
                                personaje1.defenderEspecial(nuevoAtaque)
                                print('**** {} {} no pudo bloquear {} GOLPE CRITICO y queda con {} de vida. ****'.format(type(personaje1).__name__,
                                                                                                                         personaje1.nombre,
                                                                                                                         nuevoAtaque,
                                                                                                                         personaje1.vida))
                        elif personaje2.ataque_especial >= 3:
                            if posibleCritico == 3 :
                                nuevoAtaque = 1
                                personaje1.defenderEspecial(nuevoAtaque)
                                print('**** {} {} no pudo bloquear {} GOLPE CRITICO y queda con {} de vida. ****'.format(type(personaje1).__name__,
                                                                                                                         personaje1.nombre,
                                                                                                                         nuevoAtaque,
                                                                                                                         personaje1.vida))
                                
                                
                        contador +=1
                        totalTurnos -=1
                        print("-----TURNOS RESTANTES: {} -----".format(totalTurnos))
                        ataquesRealizados = 0
                    
                else:
                    print('# TURNO {} >> {} vs {}'.format(contador,
                                                             type(personaje1).__name__.upper(),
                                                             type(personaje2).__name__.upper()))
                    
                    #-----------------
                    
                    tirada = 0
                    for num in range(1):
                        tirada = random.randint(1,2)
                        
                    if tirada == 1:     # ---> SI TIRADA ==1 , ATAQUE FISICO, SI TIRADA == 2, ATAQUE ESPECIAL
                    #-----------------
                    
                        ataquesRealizados = personaje1.atacar()
                        personaje2.defender(ataquesRealizados)
                        print('La {} {} no pudo bloquear {} impactos FISICOS y queda con {} de vida.'.format(type(personaje2).__name__,
                                                                                                             personaje2.nombre,
                                                                                                             ataquesRealizados,
                                                                                                             personaje2.vida))
                        posibleCritico = personaje1.atacar()   # .atacar() devuelve un entero que representa la cantidad de golpes validos
                        if personaje1.ataque_fisico < 3:
                            if posibleCritico == 2:
                                nuevoAtaque = 1
                                personaje2.defender(nuevoAtaque)
                                print('**** La {} {} no pudo bloquear {} GOLPE CRITICO y queda con {} de vida. ****'.format(type(personaje2).__name__,
                                                                                                                            personaje2.nombre,
                                                                                                                            nuevoAtaque,
                                                                                                                            personaje2.vida))
                        elif personaje1.ataque_fisico >= 3:
                            if posibleCritico == 3:
                                nuevoAtaque = 1
                                personaje2.defender(nuevoAtaque)
                                print('**** La {} {} no pudo bloquear {} GOLPE CRITICO y queda con {} de vida. ****'.format(type(personaje2).__name__,
                                                                                                                            personaje2.nombre,
                                                                                                                            nuevoAtaque,
                                                                                                                            personaje2.vida))
                        contador +=1
                        totalTurnos -=1
                        print("-----TURNOS RESTANTES: {} -----".format(totalTurnos))
                        ataquesRealizados = 0
                    
                    elif tirada == 2:
                        ataquesRealizados = personaje1.atacarEspecial()
                        personaje2.defenderEspecial(ataquesRealizados)
                        print('{} {} no pudo bloquear {} impactos ESPECIALES y queda con {} de vida.'.format(type(personaje2).__name__,
                                                                                                    personaje2.nombre,
                                                                                                    ataquesRealizados,
                                                                                                    personaje2.vida))
                        
                        posibleCritico = personaje1.atacarEspecial()   # .atacar() devuelve un entero que representa la cantidad de golpes validos
                        if personaje1.ataque_especial < 3:
                            if posibleCritico == 2 :
                                nuevoAtaque = 1
                                personaje2.defenderEspecial(nuevoAtaque)
                                print('**** {} {} no pudo bloquear {} GOLPE CRITICO y queda con {} de vida. ****'.format(type(personaje2).__name__,
                                                                                                                            personaje2.nombre,
                                                                                                                            nuevoAtaque,
                                                                                                                            personaje2.vida))
                        elif personaje1.ataque_especial >= 3:
                            if posibleCritico == 3 :
                                nuevoAtaque = 1
                                personaje2.defenderEspecial(nuevoAtaque)
                                print('**** {} {} no pudo bloquear {} GOLPE CRITICO y queda con {} de vida. ****'.format(type(personaje2).__name__,
                                                                                                                            personaje2.nombre,
                                                                                                                            nuevoAtaque,
                                                                                                                            personaje2.vida))
                                
                                
                        contador +=1
                        totalTurnos -=1
                        print("-----TURNOS RESTANTES: {} -----".format(totalTurnos))
                        ataquesRealizados = 0
                        
            except AssertionError:
                if personaje1.estarVivo() == False and personaje2.estarVivo() == True:
                    print("""> GANADOR {} {}
                           >>> {} {} con {} de vida.
                           >>> {} {} con {} de vida.""".format(type(personaje2).__name__.upper(),
                                                                    personaje2.nombre,
                                                                    type(personaje2).__name__,
                                                                    personaje2.nombre,
                                                                    personaje2.vida,
                                                                    type(personaje1).__name__,
                                                                    personaje1.nombre,
                                                                    0))
                    print('--- TOTAL TURNOS JUGADOS: {} ---'.format(contador -1))
                    print('\n'*2)
                    print('*'*50)
                    print('\n'*5)
                    totalTurnos = 0
                elif personaje1.estarVivo() == True and personaje2.estarVivo() == False:
                    print("""> GANADOR {} {}
                           >>> {} {} con {} de vida.
                           >>> {} {} con {} de vida.""".format(type(personaje1).__name__.upper(),
                                                                  personaje1.nombre,
                                                                  type(personaje1).__name__,
                                                                  personaje1.nombre,
                                                                  personaje1.vida,
                                                                  type(personaje2).__name__,
                                                                  personaje2.nombre,
                                                                  0))
                    print('--- TOTAL TURNOS JUGADOS: {} ---'.format(contador -1))
                    print('\n'*2)
                    print('*'*50)
                    print('\n'*5)
                totalTurnos = 0
                break
        
        else:
            try:
                assert personaje1.estarVivo() == True and personaje2.estarVivo() == True
                print("""> EMPATE
                            >>> {} {} con {} de vida.
                            >>> {} {} con {} de vida.""".format(type(personaje1).__name__,
                                                                personaje1.nombre,
                                                                personaje1.vida,
                                                                type(personaje2).__name__,
                                                                personaje2.nombre,
                                                                personaje2.vida))
                print('--- TOTAL TURNOS JUGADOS: {} ---'.format(contador -1))
                print('\n'*2)
                print('*'*50)
                print('\n'*5)
                break
            except AssertionError:
                if personaje1.estarVivo() == False and personaje2.estarVivo() == True:
                    print("""> GANADOR {} {}
                           >>> {} {} con {} de vida.
                           >>> {} {} con {} de vida.""".format(type(personaje2).__name__.upper(),
                                                                    personaje2.nombre,
                                                                    type(personaje2).__name__,
                                                                    personaje2.nombre,
                                                                    personaje2.vida,
                                                                    type(personaje1).__name__,
                                                                    personaje1.nombre,
                                                                    0))
                    print('--- TOTAL TURNOS JUGADOS: {} ---'.format(contador -1))
                    print('\n'*2)
                    print('*'*50)
                    print('\n'*5)
                    totalTurnos = 0  
                elif personaje1.estarVivo() == True and personaje2.estarVivo() == False:
                    print("""> GANADOR {} {}
                           >>> {} {} con {} de vida.
                           >>> {} {} con {} de vida.""".format(type(personaje1).__name__.upper(),
                                                                  personaje1.nombre,
                                                                  type(personaje1).__name__,
                                                                  personaje1.nombre,
                                                                  personaje1.vida,
                                                                  type(personaje2).__name__,
                                                                  personaje2.nombre,
                                                                  0))
                    print('--- TOTAL TURNOS JUGADOS: {} ---'.format(contador -1))
                    print('\n'*2)
                    print('*'*50)
                    print('\n'*5)
                totalTurnos = 0
                break
            
            


if __name__ == '__main__':
    
    #A la hora de crear nuestros personajes, podemos hacer que uno sea mas atacante fisico (esto es, con un valor mas alto en 
    # ataque_fisico), y otro mayor ataque especial (valor mas alto en ataque_especial).

    momia = Momia(nombre = 'Nefertari',
                  vida = 13,
                  ataque_fisico = 2,
                  ataque_especial = 4,
                  defensa_fisica = 3,
                  defensa_especial = 3,
                  velocidad = 2)   
    barbaro = Barbaro(nombre = 'Conan',
                      vida = 13,
                      ataque_fisico = 5,
                      ataque_especial = 2,
                      defensa_fisica = 4,
                      defensa_especial = 3,
                      velocidad = 5)
    
    jugarPartida(barbaro,momia)

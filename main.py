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
                    print('# TURNO {} >> BARBARO vs MOMIA'.format(contador))
                    ataquesRealizados = personaje1.atacar()
                    personaje2.defender(ataquesRealizados)
                    print('La momia {} no pudo bloquear {} impactos y queda con {}'.format(personaje2.nombre,
                                                                                           ataquesRealizados,
                                                                                           personaje2.vida))
                    contador +=1
                    totalTurnos -=1
                    print("-----TURNOS RESTANTES: {} -----".format(totalTurnos))
                    ataquesRealizados = 0
                else:
                    print('# TURNO {} >> MOMIA vs BARBARO'.format(contador))
                    ataquesRealizados = personaje2.atacar()
                    personaje1.defender(ataquesRealizados)
                    print('El barbaro {} no pudo bloquear {} impactos y queda con {}'.format(personaje1.nombre,
                                                                                             ataquesRealizados,
                                                                                             personaje1.vida))
                    contador +=1
                    totalTurnos -=1
                    print("-----TURNOS RESTANTES: {} -----".format(totalTurnos))
                    ataquesRealizados = 0
            except AssertionError:
                if personaje1.estarVivo() == False and personaje2.estarVivo() == True:
                    print("""> GANADOR MOMIA {}
                           >>> Momia {} con {} de vida.
                           >>> Barbaro {} con {} de vida.""".format(personaje2.nombre,
                                                                    personaje2.nombre,
                                                                    personaje2.vida,
                                                                    personaje1.nombre,
                                                                    0))
                    print('--- TOTAL TURNOS JUGADOS: {} ---'.format(contador -1))
                    print('\n'*2)
                    print('*'*50)
                    print('\n'*5)
                    totalTurnos = 0  
                elif personaje1.estarVivo() == True and personaje2.estarVivo() == False:
                    print("""> GANADOR BARBARO {}
                           >>> Barbaro {} con {} de vida.
                           >>> Momia {} con {} de vida.""".format(personaje1.nombre,
                                                                  personaje1.nombre,
                                                                  personaje1.vida,
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
                    print('# TURNO {} >> MOMIA vs BARBARO'.format(contador))
                    ataquesRealizados = personaje2.atacar()
                    personaje1.defender(ataquesRealizados)
                    print('El barbaro {} no pudo bloquear {} impactos y queda con {}'.format(personaje1.nombre,
                                                                                             ataquesRealizados,
                                                                                             personaje1.vida))
                    contador +=1
                    totalTurnos -=1
                    print("-----TURNOS RESTANTES: {} -----".format(totalTurnos))
                    ataquesRealizados = 0
                else:
                    print('# TURNO {} >> BARBARO vs MOMIA'.format(contador))
                    ataquesRealizados = personaje1.atacar()
                    personaje2.defender(ataquesRealizados)
                    print('La momia {} no pudo bloquear {} impactos y queda con {}'.format(personaje2.nombre,
                                                                                           ataquesRealizados,
                                                                                           personaje2.vida))
                    contador +=1
                    totalTurnos -=1
                    print("-----TURNOS RESTANTES: {} -----".format(totalTurnos))
                    ataquesRealizados = 0
            except AssertionError:
                if personaje1.estarVivo() == False and personaje2.estarVivo() == True:
                    print("""> GANADOR MOMIA {}
                           >>> Momia {} con {} de vida.
                           >>> Barbaro {} con {} de vida.""".format(personaje2.nombre,
                                                                    personaje2.nombre,
                                                                    personaje2.vida,
                                                                    personaje1.nombre,
                                                                    0))
                    print('--- TOTAL TURNOS JUGADOS: {} ---'.format(contador -1))
                    print('\n'*2)
                    print('*'*50)
                    print('\n'*5)
                    totalTurnos = 0
                elif personaje1.estarVivo() == True and personaje2.estarVivo() == False:
                    print("""> GANADOR BARBARO {}
                           >>> Barbaro {} con {} de vida.
                           >>> Momia {} con {} de vida.""".format(personaje1.nombre,
                                                                  personaje1.nombre,
                                                                  personaje1.vida,
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
                print("""> EMPATE {}
                            >>> Barbaro {} con {} de vida.
                            >>> Momia {} con {} de vida.""".format(personaje1.nombre,
                                                                    personaje1.nombre,
                                                                    personaje1.vida,
                                                                    personaje2.nombre,
                                                                    personaje2.vida))
                print('--- TOTAL TURNOS JUGADOS: {} ---'.format(contador -1))
                print('\n'*2)
                print('*'*50)
                print('\n'*5)
                break
            except AssertionError:
                if personaje1.estarVivo() == False and personaje2.estarVivo() == True:
                    print("""> GANADOR MOMIA {}
                           >>> Momia {} con {} de vida.
                           >>> Barbaro {} con {} de vida.""".format(personaje2.nombre,
                                                                    personaje2.nombre,
                                                                    personaje2.vida,
                                                                    personaje1.nombre,
                                                                    0))
                    print('--- TOTAL TURNOS JUGADOS: {} ---'.format(contador -1))
                    print('\n'*2)
                    print('*'*50)
                    print('\n'*5)
                    totalTurnos = 0  
                elif personaje1.estarVivo() == True and personaje2.estarVivo() == False:
                    print("""> GANADOR BARBARO {}
                           >>> Barbaro {} con {} de vida.
                           >>> Momia {} con {} de vida.""".format(personaje1.nombre,
                                                                  personaje1.nombre,
                                                                  personaje1.vida,
                                                                  personaje2.nombre,
                                                                  0))
                    print('--- TOTAL TURNOS JUGADOS: {} ---'.format(contador -1))
                    print('\n'*2)
                    print('*'*50)
                    print('\n'*5)
                totalTurnos = 0
                break
            
            


if __name__ == '__main__':

    momia = Momia('Nefertari',8,2,3,2)
    barbaro = Barbaro('Conan',7,3,3,5)

    jugarPartida(barbaro,momia)
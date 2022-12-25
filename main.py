from models import Momia, Barbaro


def jugarPartida(personaje1,personaje2):  #personaje1 = Barbaro, personaje2 = Momia
    totalTurnos = int(input("Seleccione el numero de turnos que desea jugar:"))
    
    print('\n'*5)
    print('*'*50)
    print('\n'*2)
    print("El numero total de turnos establecido es de {} turnos.".format(totalTurnos))
    
    
    contador = 1
    while True:
        if totalTurnos > 0:
            try:
                assert personaje1.estarVivo() == True and personaje2.estarVivo() == True
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
                
            
            
            
            try:
                assert personaje1.estarVivo() == True and personaje2.estarVivo() == True
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

    momia = Momia('Nefertari',8,2,3)
    barbaro = Barbaro('Conan',7,3,3)

    jugarPartida(barbaro,momia)
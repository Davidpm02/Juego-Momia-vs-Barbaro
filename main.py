import random
import time

from models import Momia, Barbaro

def comprobarVelocidad(personaje1,personaje2):
    if personaje1.velocidad > personaje2.velocidad:
        print('*',' '*12,'El personaje {} es mas rapido que el personaje {}!'.format(personaje1.nombre,
                                                                                     personaje2.nombre),' '*36,'*')
        print('*',' '*12,'El personaje {} comienza el ataque antes.'.format(personaje1.nombre),' '*52,'*')
        
    elif personaje1.velocidad < personaje2.velocidad:
        print('*',' '*12,'El personaje {} es mas rapido que el personaje {}!'.format(personaje2.nombre,
                                                                                     personaje1.nombre),' '*36,'*')
        print('*',' '*12,'El personaje {} comienza el ataque antes.'.format(personaje2.nombre),' '*48,'*')
        
    elif personaje1.velocidad == personaje2.velocidad:
        
        numerosJ1 = [1,3,5,7,9]
        numerosJ2 = [2,4,6,8,10]
        
        
        numeroEscogido = random.randint(1,10)
        
        if numeroEscogido in numerosJ1:
            print('*',' '*3,'El personaje {} {} y el personaje {} {} tienen las mismas estadisticas de velocidad!'.format(type(personaje1).__name__.upper(),
                                                                                                                personaje1.nombre,
                                                                                                                type(personaje2).__name__.upper(),
                                                                                                                personaje2.nombre),' '*3,'*',end='\n')
            print('*',' '*3,'Se va a elegir aleatoriamente que personaje comienza antes...',' '*44,'*')
            
            personaje1.velocidad +=1                            # En el caso de que los dos personajes jugando tengan el mismo valor
            time.sleep(1)                                       # en el atributo velocidad, la funcion elegirá de manera aleatoria un numero y,
            print('*',' '*3,'.',' '*104,'*')                                        # en funcion del numero, se le sumana un punto de veolicadad al persona en cuestion.
            time.sleep(1)
            print('*',' '*3,'..',' '*103,'*')
            time.sleep(1)
            print('*',' '*3,'...',' '*102,'*')
            print('*',' '*3,'El personaje {} {} comienza el ataque antes!'.format(type(personaje1).__name__.upper(),
                                                                        personaje1.nombre),' '*53,'*')
            
            
        elif numeroEscogido in numerosJ2:
            print('*',' '*3,'El personaje {} {} y el personaje {} {} tienen las mismas estadisticas de velocidad!'.format(type(personaje1).__name__.upper(),
                                                                                                                personaje1.nombre,
                                                                                                                type(personaje2).__name__.upper(),
                                                                                                                personaje2.nombre),' '*3,'*',end='\n')
            print('*',' '*3,'Se va a elegir aleatoriamente que personaje comienza antes...',' '*44,'*')
               
            
            personaje2.velocidad +=1
            time.sleep(1)                                       # en el atributo velocidad, la funcion elegirá de manera aleatoria un numero y,
            print('*',' '*3,'.',' '*104,'*')                                        # en funcion del numero, se le sumana un punto de veolicadad al persona en cuestion.
            time.sleep(1)
            print('*',' '*3,'..',' '*103,'*')
            time.sleep(1)
            print('*',' '*3,'...',' '*102,'*')
            print('*',' '*3,'El personaje {} {} comienza el ataque antes!'.format(type(personaje2).__name__.upper(),
                                                                        personaje2.nombre),' '*51,'*')
            

            
            
        
    else:  
        print('''Ha ocurrido un error al comprobar la velocidad de los personajes.''')
        
        

def jugarPartida(personaje1,personaje2):  #personaje1 = Barbaro, personaje2 = Momia
    totalTurnos = int(input("Seleccione el numero de turnos que desea jugar:"))
    
    print('\n'*5)
    print('*'*114)
    print('*',' '*110,'*',end='\n')
    print('*',' '*110,'*',end='\n')
    print('*',' '*7,"El numero total de turnos establecido es de {} turnos.".format(totalTurnos),' '*47,'*')
    print('*',' '*110,'*',end='\n')
    print('*',' '*110,'*',end='\n')
    comprobarVelocidad(personaje1,personaje2)
    print('*',' '*110,'*',end='\n')
    print('*',' '*110,'*',end='\n')
    print('*'*114)
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
                        print("----- TURNOS RESTANTES: {} -----".format(totalTurnos))
                        print()
                        print()
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
                        print("----- TURNOS RESTANTES: {} -----".format(totalTurnos))
                        print()
                        print()
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
                        print("----- TURNOS RESTANTES: {} -----".format(totalTurnos))
                        print()
                        print()
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
                        print("----- TURNOS RESTANTES: {} -----".format(totalTurnos))
                        print()
                        print()
                        ataquesRealizados = 0
                    
            except AssertionError:
                if personaje1.estarVivo() == False and personaje2.estarVivo() == True:
                    print('*'*75)
                    print('*',' '*71,'*')
                    print('*',' '*71,'*')
                    print('*',' '*10,'> GANADOR {} {}'.format(type(personaje2).__name__.upper(),
                                                              personaje2.nombre),' '*34,'*')
                    print('*',' '*71,'*')
                    print('*',' '*25,'>>> {} {} con {} de vida.'.format(type(personaje2).__name__,
                                                             personaje2.nombre,
                                                             personaje2.vida),' '*9,'*')
                    print('*',' '*25,'>>> {} {} con {} de vida.'.format(type(personaje1).__name__,
                                                             personaje1.nombre,
                                                             0),' '*12,'*')
                    print('*',' '*71,'*')
                    print('*',' '*19,'--- TOTAL TURNOS JUGADOS: {} ---'.format(contador -1),' '*18,'*')
                    print('*',' '*71,'*')
                    print('*',' '*71,'*')
                    print('*'*75)
                    print('\n'*5)
                    totalTurnos = 0  
                elif personaje1.estarVivo() == True and personaje2.estarVivo() == False:
                    print('*'*75)
                    print('*',' '*71,'*')
                    print('*',' '*71,'*')
                    print('*',' '*10,'> GANADOR {} {}'.format(type(personaje1).__name__.upper(),
                                                              personaje1.nombre),' '*36,'*')
                    print('*',' '*71,'*')
                    print('*',' '*25,'>>> {} {} con {} de vida.'.format(type(personaje1).__name__,
                                                             personaje1.nombre,
                                                             personaje1.vida),' '*11,'*')
                    print('*',' '*25,'>>> {} {} con {} de vida.'.format(type(personaje2).__name__,
                                                             personaje2.nombre,
                                                             0),' '*10,'*')
                    print('*',' '*71,'*')
                    print('*',' '*19,'--- TOTAL TURNOS JUGADOS: {} ---'.format(contador -1),' '*18,'*')
                    print('*',' '*71,'*')
                    print('*',' '*71,'*')
                    print('*'*75)
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
                        print("----- TURNOS RESTANTES: {} -----".format(totalTurnos))
                        print()
                        print()
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
                        print("----- TURNOS RESTANTES: {} -----".format(totalTurnos))
                        print()
                        print()
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
                        print("----- TURNOS RESTANTES: {} -----".format(totalTurnos))
                        print()
                        print()
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
                        print("----- TURNOS RESTANTES: {} -----".format(totalTurnos))
                        print()
                        print()
                        ataquesRealizados = 0
                        
            except AssertionError:
                if personaje1.estarVivo() == False and personaje2.estarVivo() == True:
                    print('*'*75)
                    print('*',' '*71,'*')
                    print('*',' '*71,'*')
                    print('*',' '*10,'> GANADOR {} {}'.format(type(personaje2).__name__.upper(),
                                                              personaje2.nombre),' '*34,'*')
                    print('*',' '*71,'*')
                    print('*',' '*25,'>>> {} {} con {} de vida.'.format(type(personaje2).__name__,
                                                             personaje2.nombre,
                                                             personaje2.vida),' '*9,'*')
                    print('*',' '*25,'>>> {} {} con {} de vida.'.format(type(personaje1).__name__,
                                                             personaje1.nombre,
                                                             0),' '*12,'*')
                    print('*',' '*71,'*')
                    print('*',' '*19,'--- TOTAL TURNOS JUGADOS: {} ---'.format(contador -1),' '*18,'*')
                    print('*',' '*71,'*')
                    print('*',' '*71,'*')
                    print('*'*75)
                    print('\n'*5)
                    totalTurnos = 0
                elif personaje1.estarVivo() == True and personaje2.estarVivo() == False:
                    print('*'*75)
                    print('*',' '*71,'*')
                    print('*',' '*71,'*')
                    print('*',' '*10,'> GANADOR {} {}'.format(type(personaje1).__name__.upper(),
                                                              personaje1.nombre),' '*36,'*')
                    print('*',' '*71,'*')
                    print('*',' '*25,'>>> {} {} con {} de vida.'.format(type(personaje1).__name__,
                                                             personaje1.nombre,
                                                             personaje1.vida),' '*11,'*')
                    print('*',' '*25,'>>> {} {} con {} de vida.'.format(type(personaje2).__name__,
                                                             personaje2.nombre,
                                                             0),' '*10,'*')
                    print('*',' '*71,'*')
                    print('*',' '*19,'--- TOTAL TURNOS JUGADOS: {} ---'.format(contador -1),' '*18,'*')
                    print('*',' '*71,'*')
                    print('*',' '*71,'*')
                    print('*'*75)
                    print('\n'*5)
                totalTurnos = 0
                break
        
        else:
            try:
                assert personaje1.estarVivo() == True and personaje2.estarVivo() == True
                print('*'*75)
                print('*',' '*71,'*')
                print('*',' '*71,'*')
                print('*',' '*10,'> EMPATE',' '*51,'*')
                print('*',' '*71,'*')
                print('*',' '*25,'>>> {} {} con {} de vida. '.format(type(personaje1).__name__,
                                                                    personaje1.nombre,
                                                                    personaje1.vida),' '*11,'*')
                print('*',' '*25,'>>> {} {} con {} de vida. '.format(type(personaje2).__name__,
                                                                    personaje2.nombre,
                                                                    personaje2.vida),' '*8,'*')
                print('*',' '*71,'*')
                print('*',' '*19,'--- TOTAL TURNOS JUGADOS: {} ---'.format(contador -1),' '*18,'*')
                print('*',' '*71,'*')
                print('*',' '*71,'*')
                print('*'*75)
                print('\n'*5)
                break
            except AssertionError:
                if personaje1.estarVivo() == False and personaje2.estarVivo() == True:
                    print('*'*75)
                    print('*',' '*71,'*')
                    print('*',' '*71,'*')
                    print('*',' '*10,'> GANADOR {} {}'.format(type(personaje2).__name__.upper(),
                                                              personaje2.nombre),' '*34,'*')
                    print('*',' '*71,'*')
                    print('*',' '*25,'>>> {} {} con {} de vida.'.format(type(personaje2).__name__,
                                                             personaje2.nombre,
                                                             personaje2.vida),' '*9,'*')
                    print('*',' '*25,'>>> {} {} con {} de vida.'.format(type(personaje1).__name__,
                                                             personaje1.nombre,
                                                             0),' '*12,'*')
                    print('*',' '*71,'*')
                    print('*',' '*19,'--- TOTAL TURNOS JUGADOS: {} ---'.format(contador -1),' '*18,'*')
                    print('*',' '*71,'*')
                    print('*',' '*71,'*')
                    print('*'*75)
                    print('\n'*5)
                    totalTurnos = 0  
                elif personaje1.estarVivo() == True and personaje2.estarVivo() == False:
                    print('*'*75)
                    print('*',' '*71,'*')
                    print('*',' '*71,'*')
                    print('*',' '*10,'> GANADOR {} {}'.format(type(personaje1).__name__.upper(),
                                                              personaje1.nombre),' '*36,'*')
                    print('*',' '*71,'*')
                    print('*',' '*25,'>>> {} {} con {} de vida.'.format(type(personaje1).__name__,
                                                             personaje1.nombre,
                                                             personaje1.vida),' '*11,'*')
                    print('*',' '*25,'>>> {} {} con {} de vida.'.format(type(personaje2).__name__,
                                                             personaje2.nombre,
                                                             0),' '*10,'*')
                    print('*',' '*71,'*')
                    print('*',' '*19,'--- TOTAL TURNOS JUGADOS: {} ---'.format(contador -1),' '*18,'*')
                    print('*',' '*71,'*')
                    print('*',' '*71,'*')
                    print('*'*75)
                    print('\n'*5)
                totalTurnos = 0
                break
            
            


if __name__ == '__main__':
    
    #A la hora de crear nuestros personajes, podemos hacer que uno sea mas atacante fisico (esto es, con un valor mas alto en 
    # ataque_fisico), y otro mayor ataque especial (valor mas alto en ataque_especial).

    momia = Momia(nombre = 'Nefertari',
                  vida = 49,
                  ataque_fisico = 16,
                  ataque_especial = 12,
                  defensa_fisica = 11,   # Los valores de defensa de los personajes deben ser superiores a los valores de ataque
                  defensa_especial = 11, # para evitar posibles errores.
                  velocidad = 10)   
    barbaro = Barbaro(nombre = 'Conan',
                      vida = 52,
                      ataque_fisico = 17,
                      ataque_especial = 10,
                      defensa_fisica = 20,
                      defensa_especial = 18,
                      velocidad = 10)
    
    jugarPartida(barbaro,momia)

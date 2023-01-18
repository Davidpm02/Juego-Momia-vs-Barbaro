# Juego-Momia-vs-Barbaro

<br>
<h1> Introduccion </h1>

Juego basado en el clasico juego por turnos entre dos personajes.

Se utiliza en su totalidad el paradigma orientado a objetos de Python. El programa otorga el jugador la posibilidad de establecer
las estadisticas de los personajes, asi como su nombre.
Ademas, es posible establecer un numero de turnos fijado antes del comienzo de la batalla.
<br>
<br>
<br>
<br>

<h2> COMMIT #1 </h2>

  - Se ha dividido el codigo en dos archivos para mejorar la organizacion del mismo.
  
  - Se ha modificado la funcion principal para empezar la partida (se han incluido estructuras try: except: , asi como varios assert para tener
  mayor control del transcurso de la partida).
  - Se ha corregido un fallo que permitia que el un personaje con una vida < 0 pudiese seguir atacando.
  
  - Se un personaje recibe un daño superior a la vida restante que le queda, el mensaje de final de la partida mostrara a este personaje con un
  valor de vida de 0 (antes, si un personaje tenia 1 de vida restante y recibia 2 golpes, el mensaje final indicaba que el personaje quedaba con
  -1 de vida.)
<br>
<br>
<br>
<br>

<h2> COMMIT #2 </h2>


  - Se ha añadido el atributo 'velocidad' para los personajes. Este atributo sera crucial para decidir que personaje empieza antes el ataque
  durante la batalla. 
  
  Se ha mejorado la funcion principal para que tome en cuenta la novedad (ahora se verificara que personaje es mas rapido, y este empezara a 
  atacar antes durante la batalla).
  
  - Se ha creado una nueva funcion 'comprobarVelocidad()' que envia un mensaje por pantalla avisandonos de que personaje es mas rapido que
  el otro. 
  
  Esta funcion es llamada desde la funcion principal, por lo que el aviso aparecera siempre al principio de la terminal al comenzar una batalla.
<br>
<br>
<br>
<br>

<h2> COMMIT #3 </h2>


  - Se ha añadido una nueva funcionalidad, los **golpes criticos**.
  
  Los golpes criticos funcionan asestando un golpe adicional al final del turno de ataque de un personaje.
  
  Teniendo en cuenta que los ataques a un personaje 'b' se realizan mediante una tirada de dado en base al atributo ataque del personaje 'a', el funcionamiento de los golpes criticos se puede explicar de la siguiente manera:
 - El personaje 'a' realiza tantas tiradas de dado como indique su atributo ataque, y solo seran validas aquellas tiradas que cumplan ciertas condiciones.
 - El personaje 'a' ataca al personaje 'b' en base al resultado anterior.
 - Se ejecuta una nueva tirada de dado adicional (tambien en base al atributo ataque del personaje 'a'), para decidir si asestar un golpe critico.
 - Para que se valide la tirada adicional y se ejecute el golpe critico, el personaje DEBE haber realizado un total de 3 tiradas efectivas:
  
   - Si se cumple, se ejecutara (solo) un golpe critico (se avisara por pantalla), conservando el mismo efecto que un golpe normal.
   - En caso de no cumplirse la condicion, el programa continuara su curso, y el personaje 'a' no asestara ningun golpe critico en ese turno.
<br>
<br>
<br>
<br>  

<h2> COMMIT #4 </h2>
Se ha actualizado el archivo main.py modificando los mensajes que aparecian por pantalla anunciando el trancurso de la misma.
Se ha realizado los siguientes cambios:

  - Se ha modificado la forma de mostrar el nombre del tipo de personaje que escojemos (no su nombre (e.g: 'Conan'), si no su especie (e.g: 'Barbaro')).
<br>
<br>
<br>
<br> 

<h2> COMMIT #5 </h2>
Se ha solucionado un error que impedia que personajes con un valor de ataque < 3 no pudiesen ejecutar golpes criticos (debido a la naturaleza propia de como estos estaban definidos.)


<br>
<br>
<br>
<br>

<h2> COMMIT #6 </h2>
Se han añadido los atributos 'ataque_especial' y 'defensa_especial' a los personajes. Todavia falta implementar la funcion de ataque y defensa especial.

<br>
<br>
<br>
<br>

<h2> COMMIT #7 </h2>
Se han modificado los nombres de algunos atributos de la clase Personaje.

Se han modificado los detalles de los comentarios de las clases en el archivo models.py.

Se ha corregido el funcionamiento de la partida en el archivo main.py, acorde al nuevo nombre del atributo ataque (ataque_fisico)
<br>
<br>
<br>
<br>

<h2> COMMIT #8 </h2>
Se han introducido mecanicas de ataque Fisico y ataque Especial, pudiendo ahora los personajes ejecutar un ataque cada tipo por turno de manera aleatoria.

Este cambio esta implementado como una manera de crear a un personaje que tenga mayor valor de un ataque es especifico (podemos tener un personaje que posea un valor de ataque fisico mas elevado que su ataque especial, y viceversa.)

Por otra parte, este cambio aporta algo de novedad, pues dependiendo de que tipo de atacante sea el personaje del turno de juego, este puede ser visto como mejor personaje sin necesidad de tener mejores estadisticas.

<br>
<br>
<br>
<br>

<h2>Futuros Commits</h2> 
  
  Si dos personajes poseen las mismas estadisticas en el atributo velocidad, el programa deberia elegir de manera aleatoria que personaje empieza
  antes.
  
  Se podria implementar un **modo de JvsJ**
  
   - Cada jugador deberia poder crearse un personaje in-game.
    
   - Las estadisticas de los personajes, deberian repartirse de manera aleatoria, pero en consecuencia con el tipo de atacante ( si es especial, el valor de ataque Fisico deberia ser menor, etc...).
    
   - A la hora de atacar, el jugador deberia poder elegir si efectuar un ataque fisico o uno especial.
  
  Se deberia poder ofrecer al jugador la **posibilidad de escojer que tipo de personaje queria jugar** (models.py solo da opcion a Barbaro y Momia.)
  
   - Se deberian crear unos cuantos personajes por defecto, y que el jugador pudiese elegir uno de ellos al momento de crear su personaje.

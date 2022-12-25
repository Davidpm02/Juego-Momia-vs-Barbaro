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

<h2>Futuros Commits</h2>

Posteriormente, se anadiran golpes criticos, que actuaran en funcion de una probabilidad y con unos efectos todavia por definir.

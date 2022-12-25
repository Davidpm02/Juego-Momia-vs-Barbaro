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


<h2>Futuros Commits</h2>

Posteriormente, se anadiran estadisticas como la velocidad que, en funcion de su valor, hara que un personaje ataque antes que otro de manera automatica.

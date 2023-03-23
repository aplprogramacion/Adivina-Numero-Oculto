# Adivina-Numero-Oculto
Debemos de preguntar al usuario un número entre 1 y 50.

Si añaden un número fuera de ese rango, vamos a indicar con un error que anime a elegir un número dentro del rango adecuado..

Si no acertamos el número oculto, preguntaremos al usuario si queremos seguir jugando, introduciendo un nuevo número o queremos dejar de jugar.

Finalmente, cuando el usuario acierta correctamente el número oculto, mostramos un mensaje de enhorabuena y mostramos el número de intentos que hemos utilizado para llegar a esta situación.

utilizamos la función randint del módulo random para generar el número oculto aleatorio entre 1 y 50. Luego, utilizamos un bucle while para solicitar al usuario que elija un número y compararlo con el número oculto. Si el número elegido no está dentro del rango válido, mostramos un mensaje de error y volvemos a solicitar al usuario que elija un número.

Si el usuario adivina el número oculto, mostramos un mensaje de felicitación y el número de intentos que se han necesitado para adivinarlo. Si el usuario no adivina el número oculto, preguntamos si desea seguir jugando y, si no, mostramos el número oculto y un mensaje de despedida.

![This is an image](https://github.com/aplprogramacion/Adivina-Numero-Oculto/blob/master/Captura%20de%20pantalla%20(49).png)

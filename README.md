Primer Parcial de Programación - UTN-Avellaneda
Descripción del problema
En este parcial, se te pide desarrollar un código que trabaje con el Dream Team de baloncesto de 1992, un equipo icónico compuesto por jugadores destacados de la NBA. El objetivo del código es realizar diversas operaciones y análisis de datos sobre los jugadores y sus estadísticas.
El Dream Team de 1992 está representado en una lista de diccionarios, donde cada diccionario contiene la información de un jugador. Cada jugador tiene los siguientes campos:
"nombre": el nombre completo del jugador.
"posicion": la posición en la que juega (base, escolta, alero, ala-pívot o pívot).
"estadisticas": un diccionario que contiene diversas estadísticas del jugador, como puntos totales, rebotes totales, asistencias totales, etc.
![258891731_858144791541121_374467890545703283_n](https://github.com/damiancubilla27/pp_lab1_cubilla_damian/assets/68015497/1c546d55-ca53-44a8-9038-e7d89a0fddeb)
1. Escribe un programa en Python que cargue la información de los jugadores del Dream Team desde un archivo JSON y realice las siguientes tareas, teniendo en cuenta que cada una de ellas deberá de ser realizada por una función diferenteMostrar la lista de todos los jugadores del Dream Team. Con el formato:
Nombre Jugador - Posición. Ejemplo:
Michael Jordan - Escolta
2. Permitir al usuario seleccionar un jugador por su índice y mostrar sus estadísticas completas, incluyendo temporadas jugadas, puntos totales, promedio de puntos por partido, rebotes totales, promedio de rebotes por partido, asistencias totales, promedio de asistencias por partido, robos totales, bloqueos totales, porcentaje de tiros de campo, porcentaje de tiros libres y porcentaje de tiros triples.
3. Después de mostrar las estadísticas de un jugador seleccionado por el usuario, permite al usuario guardar las estadísticas de ese jugador en un archivo CSV. El archivo CSV debe contener los siguientes campos: nombre, posición, temporadas, puntos totales, promedio de puntos por partido, rebotes totales, promedio de rebotes por partido, asistencias totales, promedio de asistencias por partido, robos totales, bloqueos totales, porcentaje de tiros de campo, porcentaje de tiros libres y porcentaje de tiros triples.
4. Permitir al usuario buscar un jugador por su nombre y mostrar sus logros, como campeonatos de la NBA, participaciones en el All-Star y pertenencia al Salón de la Fama del Baloncesto, etc.
5. Calcular y mostrar el promedio de puntos por partido de todo el equipo del Dream Team, ordenado por nombre de manera ascendente. 
6. Permitir al usuario ingresar el nombre de un jugador y mostrar si ese jugador es miembro del Salón de la Fama del Baloncesto.
7. Calcular y mostrar el jugador con la mayor cantidad de rebotes totales.
8. Calcular y mostrar el jugador con el mayor porcentaje de tiros de campo.
9. Calcular y mostrar el jugador con la mayor cantidad de asistencias totales.
10. Permitir al usuario ingresar un valor y mostrar los jugadores que han promediado más puntos por partido que ese valor.
11. Permitir al usuario ingresar un valor y mostrar los jugadores que han promediado más rebotes por partido que ese valor.
12. Permitir al usuario ingresar un valor y mostrar los jugadores que han promediado más asistencias por partido que ese valor.
13. Calcular y mostrar el jugador con la mayor cantidad de robos totales.
14. Calcular y mostrar el jugador con la mayor cantidad de bloqueos totales.
15. Permitir al usuario ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros libres superior a ese valor.
16. Calcular y mostrar el promedio de puntos por partido del equipo excluyendo al jugador con la menor cantidad de puntos por partido.
17. Calcular y mostrar el jugador con la mayor cantidad de logros obtenidos
18. Permitir al usuario ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros triples superior a ese valor.
19. Calcular y mostrar el jugador con la mayor cantidad de temporadas jugadas
20. Permitir al usuario ingresar un valor y mostrar los jugadores , ordenados por posición en la cancha, que hayan tenido un porcentaje de tiros de campo superior a ese valor.
21. Calcular de cada jugador cuál es su posición en cada uno de los siguientes ranking:
Puntos 
Rebotes 
Asistencias 
Robos
22. Determinar la cantidad de jugadores que hay por cada posición.
Ejemplo:
Base: 2
Alero: 3
23. Mostrar la lista de jugadores ordenadas por la cantidad de All-Star de forma descendente. La salida por pantalla debe tener un formato similar a este:
Michael Jordan (14 veces All Star)
Magic Johnson (12 veces All-Star)
24. Determinar qué jugador tiene las mejores estadísticas en cada valor. La salida por pantalla debe tener un formato similar a este:
Mayor cantidad de temporadas: Karl Malone (19)
Mayor cantidad de puntos totales: Karl Malon (36928)
25. Determinar qué jugador tiene las mejores estadísticas de todos.


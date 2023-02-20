Hundir_la_flota
Adaptación  del juego de mesa hundir la flota a pyhton

Proyecto
Descripción:

El juego consiste en traer toda la información del juego clásico de hundir la flota y aplicarla en Python para generar una experiencia similar.

En esta versión, el usuario deberá ingresar coordenadas de la "A" a la "J" correspondientes a las filas y del 1 al 10 que corresponden a las columnas. El objetivo es encontrar todas las coordenadas donde están ubicados los barcos del oponente. Una vez se hayan impactado todas las naves en uno de los tableros de los jugadores, el juego llegará a su fin.

Mapa del Código:

Crear Tablero:

Como primera parte del código, se genera un tablero haciendo uso de la biblioteca NumPy, la cual retornará un tablero de 10 x 10 casillas. Este se aplica 4 veces para generar 4 tableros, 2 para cada jugador: 1 para ubicar los barcos y otro para identificar donde se ha disparado.

Ubicar los barcos:

Se define la función "colocar_barcos", la cual recibe los parámetros: cantidad, longitud_barco y tablero. Mediante el uso de un bucle "while", se abre la posibilidad de posicionarlo de forma vertical u horizontal. Desde la biblioteca NumPy y Random, se utilizan las funciones para crear arrays   y "random int" para que el ordenador pueda posicionar sus naves. Antes de ubicar las naves, se verifica que en esa posición no esté ocupada por otro barco mediante el uso de condicionales "if".

Con el uso de bucles "for", se ubican los barcos con diferentes letras para poder diferenciarlos.

Función disparó:

En un bucle "while", con el uso de condicionales, se verificará la ubicación escogida por el usuario. Si la ubicación coincide con una de las ubicaciones de los barcos del oponente, la ubicación se cambiará por una "X" indicando el golpe.

En caso de que la coordenada no coincida con una de las ubicaciones de los barcos, cambiará el turno.

En el caso de la máquina, se hace uso de las librerias  NumPy y  Random  para generar una posición aleatoria donde el ordenador disparará a las posibles ubicaciones donde el jugador haya posicionado sus naves.

En el momento en que los condicionales no se cumplan porque no hay presencia de barcos, en este caso identificados con las letras "A", "B", "C" y "S", dará paso al "break" del bucle "while".

Autores:

Alvaro Jaen

Jose Zambrano


Librerías:

Random 

Numpy 


Recursos utilizados:
https://numpy.org/doc/stable/reference/generated/numpy.array.html.

https://parzibyte.me/blog/2021/12/21/batalla-naval-python-programacion-juego/


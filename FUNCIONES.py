import random
import numpy as np

#CREAR TABLERO
def crear_tablero():
    tablero= np.full((10,10)," ",dtype=str)
    return tablero

#COLOCAR BARCOS

def colocar_barcos(cantidad, longitud_barco, tablero):
    nuevo_barco=[]
    barcos_colocados = 0
    while True:
    # elegir una dirección (horizontal o vertical)
        horizontal_true = random.choice([True, False])
        if horizontal_true:
        # si es horizontal, elegir una fila aleatoria
            fila = random.randint(0, 9)
        # meterlo de tal forma que hay suficiente espacio en esa columna para el barco
            columna_inicial = random.randint(0, 10 - longitud_barco)
            columna_final = columna_inicial + longitud_barco
            if all(tablero[fila][i] == " " for i in range(columna_inicial, columna_final)): 
                nuevo_barco += [(fila, i) for i in range(columna_inicial, columna_final)]
                barcos_colocados += 1
        else:
        # si es vertical, elegir una columna aleatoria
            columna = random.randint(0, 9)
        # comprobar que hay suficiente espacio en esa fila para el barco
            fila_inicial = random.randint(0, 10 - longitud_barco)
            fila_final = fila_inicial + longitud_barco
            if all(tablero[i][columna] == " " for i in range(fila_inicial, fila_final)):
                nuevo_barco += [(i, columna) for i in range(fila_inicial, fila_final)]
                barcos_colocados += 1
        
        if barcos_colocados == cantidad:
            break
    return nuevo_barco

def disparo_jugador1(tablero2):
    #Disparo del jugador al bot(jugador2)
    while True:
        #convertir el input en filas/columnas   
        disparo = input("JUGADOR 1 - Introduce la coordenada EN MAYUSCULAS a disparar AL JUGADOR2 (por ejemplo, 4C): ")
        fila, col = disparo[0], int(disparo[1:])

        if fila == "A":
            i = 0
        elif fila == "B":
            i = 1
        elif fila == "C":
            i = 2
        elif fila == "D":
            i = 3
        elif fila == "E":
            i = 4
        elif fila == "F":
            i = 5
        elif fila == "G":
            i = 6
        elif fila == "H":
            i = 7
        elif fila == "I":
            i = 8
        elif fila == "J":
            i = 9
        else:
            print("Coordenada inválida. Inténtalo de nuevo.")
            continue

        #comprobar que las coordenadas es barco/agua y poner X
        if tablero2[i, col-1] in  ["A", "B", "C", "S"]:
            tablero2[i, col-1]= "X"
            tablero1_vacio[i, col-1]= "X"
            print("\033[1;33m"+"¡Impacto del jugador 1 al bot!")
                
            if np.sum(tablero2 == "X") == 20:
                print("¡Felicidades, has ganado!")
                
        else:
            tablero2[i, col-1] = " "
            tablero1_vacio[i, col-1]= "F"
            print("\033[1;33m"+"¡Agua del jugador 1 al bot!")
            print(tablero1)
            print("----------------------------------------------------------------------")
            print(tablero1_vacio)
            break   
    return tablero1_vacio

def disparo_jugador2(tablero1):
    #disparo del bot al jugador1(nosotros)
    while True:
         #buscar de forma aleatoria las coordenadas de la maquina  
        i= random.randint(0, 9)
        col = random.randint(0, 9)

        if tablero1[i, col-1] in  ["A", "B", "C", "S"]:
            tablero1[i, col-1]= "X"
            tablero2_vacio[i, col-1]= "X"
            print("\033[4;35m"+"¡Impacto del bot al jugador 1!")
            if np.sum(tablero1 == "X") == 20:
                print("¡Felicidades, has ganado!")
                
        else:
            tablero1[i, col-1] = " "
            tablero2_vacio[i, col-1]= "F"
            tablero1[i, col-1]= "F"
            print("\033[4;35m"+"¡Agua del bot al jugador 1!")
            break
        return tablero2_vacio
    
def starjuego():
    #bucle de turnos hasta que uno gane
    while True:
        disparo_jugador1(tablero2)
        if np.sum(tablero2 == "X") == 20:
                print("\033[1;32m"+"¡Felicidades, has ganado!")
                break
        else:
                disparo_jugador2(tablero1)
                if np.sum(tablero1 == "X") == 20:
                        print("\033[1;32m"+"¡Eres cojo mental, has perdido!")
                        break

def instrucciones():
    print("\033[1;32m"+"INSTRUCCIONES")
    print("\033[1;32m"+"EL OBJETIVO DE ESTE JUEGO ES DERRIBAR TODAS LAS NAVES DEL CONTRINCANTE")
    print(""""\033[1;32m"+CADA JUGADOR CONSTA DE: 
          4 barcos de espacio 1 
          3 barcos de espacio 2
          2 barcos de espacio 3
          1 barco de espacio 4""")
    print("\033[1;32m"+"¡QUE LA FUERZA TE ACOMPAÑE!")
    print()

def menu():
   print() 
   print("\033[1;31m"+"Escoja 1 para jugar")
   print("\033[1;31m"+"Escoja 2 para salir del juego")
   print()

def main():
    global tablero1, tablero1_vacio, tablero2, tablero2_vacio
    menu()

    while True:
        
        juego=int(input("Introduzca una opción del menú"))

        if juego==1:
            instrucciones()
            tablero1=crear_tablero()
            tablero1_vacio=crear_tablero()
            for x, y in colocar_barcos(cantidad=1, longitud_barco=4, tablero=tablero1):
                tablero1[x][y] = "S"
            for x, y in colocar_barcos(cantidad=2, longitud_barco=3, tablero=tablero1):
                tablero1[x][y] = "C"
            for x, y in colocar_barcos(cantidad=3, longitud_barco=2, tablero=tablero1):
                tablero1[x][y] = "B"
            for x, y in colocar_barcos(cantidad=4, longitud_barco=1, tablero=tablero1):
                tablero1[x][y] = "A"
            print(tablero1)
            print(tablero1_vacio)

            tablero2=crear_tablero()
            tablero2_vacio=crear_tablero()
            for x, y in colocar_barcos(cantidad=1, longitud_barco=4, tablero=tablero2):
                tablero2[x][y] = "S"
            for x, y in colocar_barcos(cantidad=2, longitud_barco=3, tablero=tablero2):
                tablero2[x][y] = "C"
            for x, y in colocar_barcos(cantidad=3, longitud_barco=2, tablero=tablero2):
                tablero2[x][y] = "B"
            for x, y in colocar_barcos(cantidad=4, longitud_barco=1, tablero=tablero2):
                tablero2[x][y] = "A"
            
            starjuego()
            #hay que hacer que tras disparar cambie al otro jugador
        elif juego==2:
            print("Hasta pronto, soldado")
            break
        else:
            "Introduce una opcion valida, solo hay dos opciones, no seas torpe"

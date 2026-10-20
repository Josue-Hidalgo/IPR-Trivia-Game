""" Bibliotecas """
from pathlib import Path
from random import randint, choice, shuffle

""" Rutas de archivos """

RUTA_BASE = Path(__file__).resolve().parent
Archivo_Preguntas = RUTA_BASE / 'preguntas_respuestas.txt'
Archivo_Puntajes = RUTA_BASE / 'puntajes.txt'

""" Variables Globales """

Continuar_Jugando = True

Nombres_Jugadores = []

M_Jugadores = []
Matriz_Preguntas_Respuesta = []


""" Funciones """
def Imprimir_Bienvenida():
    """
    
        Descripción: 
        
        Función que imprime un mensaje de bienvenida al juego de Trivia.

        Entradas: 
        - Ninguna

        Salidas:
        - Mensaje de bienvenida.

    """

    print("\n\n¡Bienvenido al Juego de Trivia: La Gran Batalla de Conocimientos!\n\n")
    print("¡Empecemos!\n\n")


def Imprimir_Pantalla_Blanco():

    """
    
        Descripción:

        Función que imprime una pantalla en blanco.

        Entradas:
        - Ninguna

        Salidas:
        - Pantalla en blanco.

    """

    print("\n" * 30)


def Imprimir_Menu_Opciones():
    """
    
        Descripción:

        Función que imprime un menú con las opciones de jugar o salir del juego.

        Entradas:
        - Ninguna

        Salidas:
        - Menú con las opciones de jugar, ver instrucciones, ver puntajes o salir del juego.

    """

    print("Menú de opciones:\n\n")
    print("A. Jugar")
    print("B. Instrucciones")
    print("C. Salir\n\n")
    

def Obtener_Opcion_Menu():

    """
    
        Descripción:

        Función que obtiene la opción seleccionada por el usuario.

        Entradas:
        - Opción seleccionada por el usuario: string  ["A","B","C"].

        Salidas:
        - Opción seleccionada por el usuario.

    """

    Opciones_Validas = ["A","B","C"]

    Opcion = input("Ingrese la opción deseada: ").strip()

    while not Opcion.upper() in Opciones_Validas:
        print("Por favor, ingrese un número entero entre las siguientes [A,B,C].")
        Opcion = input("Ingrese la opción deseada: ").strip()

    return Opcion

def Obtener_Preguntas_Respuestas():

    '''
    Funcion que lee un archivo de texto y separa las preguntas ingresandolas a una matriz.

    Entradas: Ninguna.

    Salida: Una matriz con las preguntas y respuestas de la trivia.

    Restricciones: Ninguna.
    '''

    M_Preguntas = []

    with open(Archivo_Preguntas, 'r', encoding='utf-8') as archivo:
        
        Cuestionario = archivo.readlines()
        lista = []
        for linea in Cuestionario:
            lista = linea.strip().split("##")
            
            for e in lista:
                e.replace("\\n","")

            M_Preguntas.append(lista)

    return M_Preguntas

def Obtener_Jugadores():

    '''

    Descripción:

    Funcion que recibe la cantidad de jugadores y sus nombres a un diccionario global.

    Entradas y Restriciones:
    
    -El numero de participantes: tiene que ser un numero entre el 1 al 5
    -El nombre de los participantes: Los nombres de los participantes no puede estar vacia y no puede haber nombres repetidos

    Salidas: Jugadores en un diccionario global

    '''

    Continuando = True

    Imprimir_Pantalla_Blanco()

    while Continuando:

        try:

            Participantes = []

            Nombres = []

            print("\nCantidad de Jugadores\n")

            Numero_Participantes = int(input("Inserte la cantidad de participantes minimo 1 y maximo 5: "))
            
            while Numero_Participantes < 1 or Numero_Participantes > 5:
                print("El numero de participantes ingresados es incorrecto, vuelve a intentarlo.\n")
                Numero_Participantes = int(input("Inserte la cantidad de participantes (Número entre 1-5): "))

            for numero in range(Numero_Participantes):
                
                nombre = input(f"Ingrese el {numero + 1}.º jugador: ").strip().upper()

                while nombre in Nombres or nombre == "" or not nombre.isalpha():
                    print("\n ERROR: El nombre ya esta en uso o no es válido, este tiene que tener solo letras.\n")
                    nombre = input(f"Ingrese el {numero+1}.º jugador: ").strip().upper()
                
                Nombres.append(nombre)
            shuffle(Nombres)
            for usuario in Nombres:
                Participantes.append([0 , usuario])
            
            Continuando = False

        except Exception as error:

            if ValueError:
                print("Asegurese de ingresar solo numeros.\n")
            else:
                print (f"Error:{error}")

    return Participantes


def Obtener_Numero_Preguntas():

    """
    
        Descripción:

        Función que obtiene el número de preguntas que se le harán a cada jugador.

        Entradas:
        - Número de preguntas.

        Salidas:
        - Número de preguntas.

        Restricciones:
        - Número de preguntas debe de ser el numero 5, 10 o 15


    """
    while True:

        try:

            Preguntas = [5,10,15]

            print("\nCantidad de Preguntas\n")

            print("Inserte el número de preguntas por persona:")
            print("A. 5 Preguntas")
            print("B. 10 Preguntas")
            print("C. 15 Preguntas\n")

            Opcion = input("Opción: ").strip()
            
            if Opcion.upper() not in ["A","B","C"]:
                raise ValueError("Debe ingresar una opción [A,B,C]")

            Indice = ["A","B","C"].index(Opcion.upper())

            return Preguntas[Indice]
        
        except Exception as error:
            print (f"Error:{error}")


def Marcador():
    
    """
    
    Descripción:
    Función que imprime los resultados que tienen los participantes hasta el 
    momento en la ronda.
        
    Entradas: 
    - M_Jugadores: Matriz

    Salidas: 
    - Imprime Puntajes
    
    """

    Imprimir_Pantalla_Blanco()

    global M_Jugadores

    M_Jugadores.sort(reverse=True)

    i = 1

    for Puntaje, Jugador in M_Jugadores:
        print(f"{i}° Lugar: {Jugador} con {Puntaje} puntos.")
        i += 1

    input("\n\n Presiona cualquier tecla para continuar \n\n")


def Imprimir_Mensaje_Acierto():

    """

    Descripción:
    Procedimiento que imprime mensaje de acierto

    Entradas y restricciones: Ninguna

    Salida: ninguna

    """

    Imprimir_Pantalla_Blanco()

    mensajes_de_victoria = ["Felicidades, Acertaste", "Increíble intelecto", "Asombrosa idea", "No hay nadie como tú", "La victoria esta en tus manos"]
    random = randint(0, len(mensajes_de_victoria) - 1)
    print("\n¡¡CORRECTO!!\n")
    print("\n",mensajes_de_victoria[random],"\n")  

    input("\n\n Presiona cualquier tecla para continuar \n\n")

def Imprimir_Mensaje_Fallo():

    """
        Descripción:
        - Procedimiento que imprime mensaje de fallo

        Entradas y restricciones: Ninguna

        Salida: ninguna
    
    """

    Imprimir_Pantalla_Blanco()

    mensajes_de_fallo = ["Que lastima, casi lo consigues", "Tal vez pensar más antes de resolver", "A la siguiente lo podrás lograr", "Mejor suerte para la próxima", "Game Over"]
    random = randint(0, len(mensajes_de_fallo) - 1)

    print("\n¡¡INCORRECTO!!\n")
    print(mensajes_de_fallo[random])    
    
    input("\n\n Presiona cualquier tecla para continuar \n\n")

def Imprimir_Numero_Ronda(Ronda):
    """
    
    Descripción:
    Procedimiento que imprime la ronda en la que está.

    Entradas y restricciones: Ninguna

    Salida: ninguna
    
    """

    print(f"\n\nRonda #{Ronda}\n\n")


def Imprimir_Turno(Nombre):
    """
    Descripción:
    Procedimiento que imprime Mensaje de turno en el que está

    Entradas y restricciones: Ninguna

    Salida: ninguna
    
    """

    print(f"Va el TURNO de: {Nombre}\n\n")

def Imprimir_Progreso(Nombre, Puntaje, Ronda, Total_Preguntas):
    """
    Descripción:
    Procedimiento que imprime la pregunta en la que se está, junto con el
    puntaje que lleva el jugador en ese momento.

    Entradas:
    - Nombre: string
    - Puntaje: entero
    - Ronda: entero
    - Total_Preguntas: entero

    Salida: ninguna

    """

    print(f"Pregunta {Ronda} de {Total_Preguntas}  |  {Nombre}: {Puntaje} puntos\n")

def Obtener_Puntaje_Jugador(Jugador):
    """
    Descripción:
    Función que busca el puntaje actual del jugador en la matriz M_Jugadores.

    Entradas:
    - Jugador: string

    Salidas:
    - Puntaje del jugador (0 si no se encuentra)

    """

    for Puntaje, Nombre in M_Jugadores:
        if Nombre == Jugador:
            return Puntaje

    return 0

def Pregunta_Random():

    """

    Función que obtiene Matriz de preguntas y selecciona alguna random. 

    Entradas: 
    - M_Preguntas: Matriz

    Salidas:
    - Pregunta random
        
    """
    global Matriz_Preguntas_Respuesta

    if len(Matriz_Preguntas_Respuesta) == 0:
        Matriz_Preguntas_Respuesta = Obtener_Preguntas_Respuestas()

    Random = randint(0, len(Matriz_Preguntas_Respuesta) - 1)

    Pregunta = Matriz_Preguntas_Respuesta.pop(Random)
    
    return Pregunta

def Acumule_Puntos(Jugador, Puntos):
    """
    
    Descripción:
    Función que obtiene la lista de listas de  Puntuaciones,Jugadores y 
    devuelve la matriz actualizada sumandole a la puntuación del jugador
    que respondió correctamente la pregunta.

    Entradas: 
    - M_Jugadores: matriz 
    - Jugador: string

    Salida:
    - M_Jugadores actualizada como global

    """

    global M_Jugadores

    for i in range(len(M_Jugadores)):
        if M_Jugadores[i][1] == Jugador:
            M_Jugadores[i][0] = M_Jugadores[i][0] + Puntos

    return


def Evalua_Ganador():
    """
    
    Función que menciona el jugador que ganó. No solo debe ser el de mayor
    puntaje sino que no haya ningun otro con esa puntuación sino es empate.

    Entradas: Ninguna

    Salidas: Ninguna
    
    """

    global M_Jugadores, Nombres_Jugadores

    Puntaje_Maximo = M_Jugadores[0][0]

    Jugadores_Puntaje_Max = [e for e in M_Jugadores if e[0] == Puntaje_Maximo]

    Nombres_Jugadores = [Jugador for _ , Jugador in M_Jugadores]

    return Jugadores_Puntaje_Max
    

def Imprimir_Mensaje_Ganador(Ganador):
    """
    
    Función que imprime un mensaje de victoria. 

    Entradas: 
    - Ganador: lista 

    Salidas: 
    - Ninguna
    
    """
    
    Imprimir_Pantalla_Blanco()

    print("¡Felicidades Ganaste, ERES UN GENIO!")
    print(f"¡EL GANADOR ES {Ganador[1]} con un puntaje de {Ganador[0]} puntos!")

    input("\n\n Presiona cualquier tecla para continuar \n\n")

    Marcador()

    input("\n\n Presiona cualquier tecla para continuar \n\n")

def Hubo_Empate(Empatados):
    """
    
    Función que llamamos para desempatar el juego.

    Entradas: 
    - M_Jugadores: Matriz

    Salidas: 
    - Desempate

    """

    global M_Jugadores
    
    M_Jugadores = Empatados

    Imprimir_Pantalla_Blanco()

    print("¡Ha habido un EMPATE!")
    print("\n\nEs por ello que para desempatar se hará lo siguiente: ")
    print("\n1-Se tomarán los empatados y seguirán contestando, una por una, preguntas.")
    print("\n2-Quien falle la pregunta no tendrá segunta oportunidad.")
    print("\n3-Ganará quien no falle.")

    input("\n\n Presiona cualquier tecla para continuar \n\n")

    Empezar_Juego(1)

def Imprimir_Pregunta(Pregunta, L_Respuesta):
    """
    
    Función que imprime las Preguntas

    Entradas: 
    - Pregunta: Lista

    Salida: 
    - Ninguna

    """

    print(Pregunta[0])

    for i in range(1, len(Pregunta) - 1):
        print(L_Respuesta[i - 1], ". ", Pregunta[i])


def Empezar_Juego(N_Preguntas):
    """
    Descripción: 
    Subrutina que se encarga de realizar las preguntas a los jugadores y de acertarlas darle un punto al jugador
    
    Entradas:
    - preguntas: lista con las preguntas y las posibles respuestas ordenadas de manera aleatoria
    - participantes: diccionario/documento txt con los jugadores y sus puntajes actuales (Roy:modificar pq ahora los jugadores son matriz) 
    - respuestas: diccionario con las respuestas de las preguntas.

    Salida:
    - Ninguna

    """

    global Nombres_Jugadores

    L_Respuesta = ["A","B","C","D"]

    Imprimir_Pantalla_Blanco()

    for ronda in range(1, N_Preguntas + 1): 
        
        Marcador()

        Imprimir_Numero_Ronda(ronda)
        
        for Turno_Jugador in Nombres_Jugadores:
            
            Imprimir_Turno(Turno_Jugador)

            Imprimir_Progreso(Turno_Jugador, Obtener_Puntaje_Jugador(Turno_Jugador), ronda, N_Preguntas)

            Pregunta_Actual = Pregunta_Random()
            
            Imprimir_Pregunta(Pregunta_Actual, L_Respuesta)
            
            Respuesta = input("Ingrese su respuesta: ").strip().upper()

            while Respuesta not in L_Respuesta:
                Respuesta = input("Ingrese una respuesta válida (A,B,C,D): ").strip().upper()

            Indice = L_Respuesta.index(Respuesta)
            
            Respuesta_Correcta = (Pregunta_Actual[Indice + 1] == Pregunta_Actual[5])

            if Respuesta_Correcta:
                Imprimir_Mensaje_Acierto()
                Acumule_Puntos(Turno_Jugador, 100)
            else:
                Imprimir_Mensaje_Fallo() 

    Maximos_Puntajes = Evalua_Ganador()

    if len(Maximos_Puntajes) == 1:
        Imprimir_Mensaje_Ganador(Maximos_Puntajes[0]) 
    else: 
        Hubo_Empate(Maximos_Puntajes)

    return


def Guardar_Puntajes(Jugadores):

    """
    
        Descripción:

        Función que agrega al archivo puntajes.txt el puntaje final de cada
        jugador de la partida recién terminada, con el formato "Puntaje,Nombre".

        Entradas:
        - Jugadores: matriz con los puntajes y nombres de los jugadores.

        Salidas:
        - Líneas agregadas al archivo puntajes.txt.

    """

    Contenido_Previo = ""

    if Archivo_Puntajes.exists():
        Contenido_Previo = Archivo_Puntajes.read_text(encoding='utf-8')

    with open(Archivo_Puntajes, 'a', encoding='utf-8') as archivo:

        if Contenido_Previo and not Contenido_Previo.endswith("\n"):
            archivo.write("\n")

        for Puntaje, Jugador in Jugadores:
            archivo.write(f"{Puntaje},{Jugador}\n")

    print(f"\nLos puntajes de esta partida se guardaron en {Archivo_Puntajes.name}\n")


def Jugar_Trivia(): 

    """
    
        Descripción:

        Función que obtiene todos los datos necesarios para empezar el juego de Trivia.

        Entradas:
        - Jugadores.
        - Diccionario con las preguntas y respuestas.
        - Número de preguntas.

        Salidas:
        - Juego de Trivia.
        
    """

    global M_Jugadores, Nombres_Jugadores, Matriz_Preguntas_Respuesta
    
    Matriz_Preguntas_Respuesta = Obtener_Preguntas_Respuestas()
    N_Preguntas = Obtener_Numero_Preguntas()

    M_Jugadores = Obtener_Jugadores()

    Nombres_Jugadores = [Jugador for _ , Jugador in M_Jugadores]

    Empezar_Juego(N_Preguntas)

    Guardar_Puntajes(M_Jugadores)

def Imprimir_Como_Jugar():

    """
    
        Descripción:

        Función que imprime un mensaje con las instrucciones de cómo jugar.

        Entradas:
        - Ninguna

        Salidas:
        - Instrucciones de cómo jugar.

    """
    print("¿En qué consiste?\n\n")
    print("Consiste en una serie de preguntas y respuestas sobre diversos temas de arte. Los jugadores compiten")
    print("para ver quién puede responder correctamente a la mayor cantidad de preguntas.\n\n")

    print("Instrucciones de cómo jugar:\n\n")
    print("1. Primero, deberás ingresar el número de jugadores que participarán en el juego.")
    print("2. Luego, deberás ingresar el número de preguntas que se le harán a cada jugador.")
    print("3. A continuación, deberás ingresar el nombre de cada jugador.")
    print("""4. Luego de ingresar el nombre de cada jugador, se le harán las preguntas a cada 
          uno por turnos.""")
    print("5. Al finalizar, se mostrará el puntaje de cada jugador y el ganador del juego.\n\n")

    input("\n\n Presiona cualquier tecla para continuar \n\n")


def Salir():

    """
    
        Descripción:

        Función que cambia el valor de la variable "Continuar_Jugando" a False.
    
        Entradas:
        - Ninguna

        Salidas:
        - Cambio de la variable "Continuar_Jugando" a False.

    """

    global Continuar_Jugando

    Continuar_Jugando = False


def Ejecutar_Opcion(Opcion):

    """
    
        Descripción:

        Función que ejecuta la opción seleccionada por el usuario.

        Entradas:
        - Opción seleccionada por el usuario, es número entero entre  ["A","B","C"]

        Salidas:
        - Ejecución de la opción seleccionada por el usuario.

    """

    Imprimir_Pantalla_Blanco()

    if Opcion.upper() == "A":
        Jugar_Trivia()
    elif Opcion.upper() == "B":
        Imprimir_Como_Jugar()
    else:
        Salir()


""" Función Principal """
def main():

    """
    
        Descripción: 
        
        Función principal del programa. Este llamará las funciones necesarias 
        para el correcto funcionamiento del proyecto.

        Entradas: 
        - Ninguna

        Salidas:
        - Juego de Trivia.

    """

    try:

        Imprimir_Bienvenida()

        input("\n\n Presiona cualquier tecla para continuar \n\n")

        global Continuar_Jugando

        Continuar_Jugando = True

        while Continuar_Jugando:

            Imprimir_Pantalla_Blanco()

            Imprimir_Menu_Opciones()

            Opcion = Obtener_Opcion_Menu()

            Ejecutar_Opcion(Opcion)

    except Exception as e:
        print(f"Ha ocurrido un error: {e}")

    finally:
        print("Gracias por jugar!")
        input("\n\n Presiona cualquier tecla para continuar \n\n")


""" Ejecución del Programa """
if __name__ == "__main__":
    main()

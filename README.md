# Proyecto 1: Trivia — "Preguntados"

Juego de trivia multijugador para consola, escrito en Python. Cada jugador responde, por turnos, preguntas de arte, literatura, música y refranes; quien acumule más puntos al final de la partida gana.

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Interfaz](https://img.shields.io/badge/Interfaz-Consola-4B8BBE)
![Dependencias](https://img.shields.io/badge/Dependencias-ninguna-brightgreen)

## Tabla de contenido

- [Características](#características)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Cómo ejecutar](#cómo-ejecutar)
- [Cómo jugar](#cómo-jugar)
- [Puntaje y desempate](#puntaje-y-desempate)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Formato de `preguntas_respuestas.txt`](#formato-de-preguntas_respuestastxt)
- [Archivo de puntajes](#archivo-de-puntajes)
- [Integrantes](#integrantes)
- [Contacto](#contacto)

## Características

- **De 1 a 5 jugadores** en la misma computadora, con los nombres en orden aleatorio en cada partida.
- **Banco de 200 preguntas** con 4 opciones cada una; la respuesta correcta puede estar en cualquier posición y las preguntas no se repiten dentro de una partida.
- **Partidas cortas o largas:** 5, 10 o 15 preguntas por jugador.
- **Marcador en vivo** entre rondas, con el progreso y los puntos del jugador en cada turno.
- **Desempate automático** si dos o más jugadores terminan empatados en el primer lugar.
- **Historial de puntajes** guardado en `puntajes.txt`.
- **Sin dependencias externas:** solo la biblioteca estándar de Python.

## Requisitos

- Python 3.10 o superior (el proyecto fue desarrollado y probado en Python 3.12).
- Una terminal que soporte entrada y salida de texto estándar.

No hace falta instalar paquetes ni crear un entorno virtual.

## Instalación

1. Descargá o cloná el proyecto:

   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd Proyecto_1_Trivia
   ```

2. Verificá que Python esté disponible:

   ```bash
   python --version
   ```

   > En algunos sistemas el intérprete se llama `python3` en lugar de `python`.
   > En Windows, si `python` abre la Microsoft Store, usá `py` o el lanzador oficial de Python.

## Cómo ejecutar

Desde la carpeta del proyecto:

```bash
python main.py
```

También podés abrir `main.py` desde un IDE (VS Code, PyCharm, Thonny) y ejecutarlo con el botón de *Run*.

El juego y sus dos archivos de datos (`preguntas_respuestas.txt` y `puntajes.txt`) se buscan en la carpeta del script, así que se puede ejecutar desde cualquier directorio de trabajo. Si `preguntas_respuestas.txt` no está junto a `main.py`, el juego mostrará un error al intentar cargar las preguntas.

## Cómo jugar

1. Al iniciar, presioná **Enter** para pasar la pantalla de bienvenida.
2. En el menú, elegí:
   - **A. Jugar** — comienza una partida.
   - **B. Instrucciones** — muestra las reglas dentro del juego.
   - **C. Salir** — cierra el programa.
3. Al elegir *Jugar*, indicá la **cantidad de jugadores** (entre 1 y 5).
4. Elegí la **cantidad de preguntas por jugador**: **A** (5), **B** (10) o **C** (15).
5. Escribí el **nombre de cada jugador**. Solo se aceptan letras y no puede haber nombres repetidos.
6. En cada turno respondé con **A**, **B**, **C** o **D** (se aceptan minúsculas y espacios de más).
7. Presioná **Enter** para avanzar entre pantallas y ver el marcador.

Al finalizar se muestra el ganador, el marcador final y se agregan los puntajes de la partida a `puntajes.txt`.

## Puntaje y desempate

- Cada respuesta correcta otorga **100 puntos**.
- Una respuesta incorrecta no suma ni resta.
- Gana quien tenga el mayor puntaje al terminar todas las rondas.
- Si dos o más jugadores empatan en el primer lugar, se juega un **desempate a muerte súbita**: los empatados responden una pregunta cada uno y quien falle queda eliminado. Gana quien no falle.

## Estructura del proyecto

```
Proyecto_1_Trivia/
├── main.py                   # Lógica e interfaz del juego (menú, turnos, puntajes)
├── preguntas_respuestas.txt  # Banco de preguntas y respuestas
├── puntajes.txt              # Historial de puntajes de partidas anteriores
├── README.md                 # Este documento
└── .gitattributes            # Normalización de finales de línea
```

Funciones principales de `main.py`:

| Función | Responsabilidad |
| --- | --- |
| `main()` | Punto de entrada: bienvenida y bucle del menú. |
| `Jugar_Trivia()` | Reúne los datos de la partida y la inicia. |
| `Empezar_Juego(N)` | Ejecuta las rondas y turnos, y define al ganador. |
| `Obtener_Preguntas_Respuestas()` | Lee y parsea el banco de preguntas. |
| `Pregunta_Random()` | Extrae una pregunta al azar sin repetirla en la partida. |
| `Marcador()` | Muestra la tabla de posiciones ordenada. |
| `Guardar_Puntajes()` | Agrega el resultado final de la partida al historial. |

## Formato de `preguntas_respuestas.txt`

Cada línea es una pregunta, con los campos separados por `##`:

```
pregunta##opción A##opción B##opción C##opción D##respuesta correcta
```

Ejemplo real:

```
¿Quién pintó 'Mujer mirando por la ventana'?##Salvador Dalí##Pablo Picasso##Claude Monet##Vincent van Gogh##Salvador Dalí
```

El sexto campo debe coincidir **exactamente** con una de las cuatro opciones. Para agregar preguntas, sumá una línea nueva con los seis campos; no hay que modificar el código.

## Archivo de puntajes

Después de cada partida, `Guardar_Puntajes()` agrega una línea por jugador al final de `puntajes.txt`, con el formato `puntaje,nombre`:

```
1000,PEPITO
200,FULANO
700,MARIA
```

El archivo se abre en modo *append*, por lo que el historial se acumula entre partidas. Borralo (o vacialo) si querés empezar de cero.

## Integrantes

- Josué Hidalgo
- Luis Jiménez
- Roy Jiménez

## Contacto

- j.hidalgo.5@estudiantec.cr
- l.jimenez.2@estudiantec.cr
- r.jimenez.2@estudiantec.cr

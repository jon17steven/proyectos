def crear_tablero(filas, columnas):
    tablero = [None]*filas
    for f in range(filas):
        tablero[f] = ['.']*columnas
    return tablero

def mostrar_tablero(tablero):
    for num in range(len(tablero[0])):
        print(num, end= '  ')
    for fila in tablero:
        print("")
        for casilla in fila:
            print(casilla, end="  ")

def introducir_ficha(tablero, columna, color):
    if columna >= len(tablero[0]) or columna < 0:
        print("ERROR")
        return
    elif tablero[0][columna] != '.':
        print("ERROR la columna esta llena")
        return
    else:
        for fila in range (len(tablero)-1, -1, -1):
            if tablero[fila][columna] == '.':
                tablero[fila][columna] = color
                return tablero

def revisar_filas(tablero, color):
    num_filas = len(tablero)
    num_columnas = len(tablero[0])
    for r in range(num_filas):
        for c in range(num_columnas - 3):
            if tablero[r][c] == color and tablero[r][c+1] == color and tablero[r][c+2] == color and tablero[r][c+3] == color:
                return True

def revisar_columnas(tablero, color):
    num_filas = len(tablero)
    num_columnas = len(tablero[0])
    for c in range(num_columnas):
        for r in range(num_filas - 3):  # Cambiado el rango para evitar salirse de los límites
            if tablero[r][c] == color and tablero[r+1][c] == color and tablero[r+2][c] == color and tablero[r+3][c] == color:
                return True
    return False  # Agregado para manejar el caso de que no se encuentre ninguna columna de 4


def revisar_diagonal_derecha(tablero, color):
    num_filas = len(tablero)
    num_columnas = len(tablero[0])
    for c in range(num_columnas - 3):
        for r in range(num_filas - 3):  # Cambiado el rango para evitar salirse de los límites
            if tablero[r][c] == color and tablero[r+1][c+1] == color and tablero[r+2][c+2] == color and tablero[r+3][c+3] == color:
                return True
    return False  # Agregado para manejar el caso de que no se encuentre ninguna diagonal derecha de 4


def revisar_diagonal_izquierda(tablero, color):
    num_filas = len(tablero)
    num_columnas = len(tablero[0])
    for c in range(num_columnas - 3):
        for r in range(3, num_filas):  # Cambiado el rango para evitar salirse de los límites
            if tablero[r][c] == color and tablero[r-1][c+1] == color and tablero[r-2][c+2] == color and tablero[r-3][c+3] == color:
                return True
    return False  # Agregado para manejar el caso de que no se encuentre ninguna diagonal izquierda de 4


def comprobar_ganador(tablero, color):
    if (revisar_filas(tablero, color) or
            revisar_columnas(tablero, color) or
            revisar_diagonal_derecha(tablero, color) or
            revisar_diagonal_izquierda(tablero, color)):
        print(f"\nHa ganado {color}. ¡Felicidades!")
        return True
    return False


def tablero_lleno(tablero):
    for fila in tablero:
        if '.' in fila:
            return False
    return True


def jugar():
    filas = 6
    columnas = 7
    tablero = crear_tablero(filas, columnas)
    jugador_actual = 'X'
    ganador = False

    while not ganador and not tablero_lleno(tablero):
        mostrar_tablero(tablero)
        print(f"\nTurno del jugador {jugador_actual}")
        columna = int(input("Introduce una columna (0-6): "))
        if introducir_ficha(tablero, columna, jugador_actual):
            if comprobar_ganador(tablero, jugador_actual):
                ganador = True
            else:
                jugador_actual = 'O' if jugador_actual == 'X' else 'X'
        else:
            print("Intenta de nuevo.")

    if not ganador:
        print("¡Es un empate!")

    mostrar_tablero(tablero)


jugar(0, 'x')



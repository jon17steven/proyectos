class CuatroRaya:
    def __init__(self, filas, columnas):

        """ Propósito: Inicializa el juego con el número de filas y columnas especificado.
            Parámetros: filas y columnas para definir el tamaño del tablero.
            Acciones:Guarda el número de filas y columnas en variables de instancia.
            Crea un tablero llamando a crear_tablero."""

        self._filas = filas
        self._columnas = columnas
        self._tablero = self.crear_tablero()



    def crear_tablero(self):

        """Propósito: Crea y devuelve un tablero vacío.
        Acciones:Utiliza una lista de listas para representar
        el tablero, con cada casilla inicialmente marcada con un punto ('.')."""

        tablero = [['.'] * self._columnas for _ in range(self._filas)]
        return tablero

    def mostrar_tablero(self):

        """Propósito: Imprime el tablero en la consola para que los jugadores puedan ver el estado actual del juego.
           Acciones:Imprime los números de las columnas en la primera fila.
           Imprime cada fila del tablero."""

        for num in range(self._columnas):
            print(num, end='  ')
        print("")
        for fila in self._tablero:
            for casilla in fila:
                print(casilla, end="  ")
            print("")

    def introducir_ficha(self, columna, ficha):

        """Propósito: Introduce una ficha en la columna especificada.
           Parámetros: columna (el índice de la columna) y ficha (el símbolo del jugador, por ejemplo, 'X' o 'O').
           Acciones:Comprueba si la columna es válida.
           Comprueba si la columna está llena.
           Encuentra la fila disponible más baja en la columna y coloca la ficha ahí."""

        if columna >= self._columnas or columna < 0:
            print("ERROR: Columna inválida")
            return False
        elif self._tablero[0][columna] != '.':
            print("ERROR: La columna está llena")
            return False
        else:
            for fila in range(self._filas - 1, -1, -1):

                """self._filas - 1: Este es el índice de la última fila del tablero. En un tablero de 6 filas, los índices van de 0 a 5, por lo que self._filas - 1 sería 5.
                   -1: Este es el valor final del rango (no inclusivo). Significa que el bucle se detendrá antes de alcanzar -1, es decir, cuando llegue a 0.
                   -1: Este es el paso del rango. Un paso negativo de -1 indica que queremos que el bucle vaya hacia atrás, es decir, de la última fila a la primera fila."""

                if self._tablero[fila][columna] == '.':
                    self._tablero[fila][columna] = ficha
                    return True
        return False

    def revisar_filas(self, color):

        """Propósito: Comprueba si hay cuatro fichas del mismo color en una fila.
           Parámetros: color (el símbolo del jugador).
           Acciones:Itera sobre cada fila y columna, y comprueba si hay cuatro fichas consecutivas del mismo color.
           Utiliza range(self._filas - 1, -1, -1) para iterar desde la última fila (índice self._filas - 1) hasta la primera fila (índice 0), en orden inverso."""

        for r in range(self._filas):
            for c in range(self._columnas - 3):
                if all(self._tablero[r][c + i] == color for i in range(4)):
                    return True
        return False

    def revisar_columnas(self, color):

        """Propósito: Comprueba si hay cuatro fichas del mismo color en una columna.
           Parámetros: color (el símbolo del jugador).
           Acciones:Itera sobre cada columna y fila, y comprueba si hay cuatro fichas consecutivas del mismo color."""

        for c in range(self._columnas):
            for r in range(self._filas - 3):
                if all(self._tablero[r + i][c] == color for i in range(4)):
                    return True
        return False

    def revisar_diagonal_derecha(self, color):

        """Propósito: Comprueba si hay cuatro fichas del mismo color en una diagonal hacia la derecha.
           Parámetros: color (el símbolo del jugador).
           Acciones:Itera sobre posibles posiciones iniciales de diagonales y comprueba si hay cuatro fichas consecutivas del mismo color."""

        for c in range(self._columnas - 3):
            for r in range(self._filas - 3):
                if all(self._tablero[r + i][c + i] == color for i in range(4)):
                    return True
        return False

    def revisar_diagonal_izquierda(self, color):

        """Propósito: Comprueba si hay cuatro fichas del mismo color en una diagonal hacia la izquierda.
           Parámetros: color (el símbolo del jugador).
           Acciones:Itera sobre posibles posiciones iniciales de diagonales y comprueba si hay cuatro fichas consecutivas del mismo color."""

        for c in range(self._columnas - 3):
            for r in range(3, self._filas):
                if all(self._tablero[r - i][c + i] == color for i in range(4)):
                    return True
        return False

    def comprobar_ganador(self, color):

        """Propósito: Comprueba si un jugador ha ganado el juego.
           Parámetros: color (el símbolo del jugador).
           Acciones:Llama a los métodos que comprueban filas, columnas y diagonales.
           Si alguno de ellos encuentra una línea de cuatro fichas del mismo color, declara al jugador como ganador."""

        if (self.revisar_filas(color) or
                self.revisar_columnas(color) or
                self.revisar_diagonal_derecha(color) or
                self.revisar_diagonal_izquierda(color)):
            print(f"\nHa ganado {color}. ¡Felicidades!")
            return True
        return False

    def tablero_lleno(self):

        """Propósito: Comprueba si el tablero está lleno.
        Acciones:Itera sobre el tablero y comprueba si hay alguna casilla vacía ('.')."""

        for fila in self._tablero:
            if '.' in fila:
                return False
        return True

    def jugar(self):

        """Propósito: Controla el flujo del juego.
           Acciones:Alterna los turnos entre dos jugadores ('X' y 'O').
           Muestra el tablero y solicita al jugador actual que introduzca una ficha en una columna.
           Comprueba si el jugador ha ganado o si el tablero está lleno. Si el tablero está lleno y no hay ganador, se declara un empate."""

        jugador_actual = 'X'
        ganador = False

        while not ganador and not self.tablero_lleno():
            self.mostrar_tablero()
            print(f"\nTurno del jugador {jugador_actual}")
            columna = int(input("Introduce una ficha (0-6): "))
            if self.introducir_ficha(columna, jugador_actual):
                if self.comprobar_ganador(jugador_actual):
                    ganador = True
                else:
                    jugador_actual = 'O' if jugador_actual == 'X' else 'X'
            else:
                print("Intenta de nuevo.")

        if not ganador:
            print("¡Es un empate!")

        self.mostrar_tablero()


# Crear una instancia del juego y empezar a jugar
juego = CuatroRaya(6, 7)
juego.jugar()

"""Propósito: Crea una instancia del juego y lo inicia.
   Acciones:Se crea un objeto CuatroRaya con 6 filas y 7 columnas.
   Se llama al método jugar para iniciar el juego."""
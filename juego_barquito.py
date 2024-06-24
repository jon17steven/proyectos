import string

class HundirLosNavios:
    def __init__(self, filas, columnas):
        self._filas = filas
        self._columnas = columnas
        self._tablero = self.crear_tablero()
        self._tablero_visible = self.crear_tablero()
        self._letras_filas = string.ascii_uppercase[:filas]

    def crear_tablero(self):
        return [['.'] * self._columnas for _ in range(self._filas)]

    def mostrar_tablero(self, tablero):
        print("   ", end='')
        for num in range(self._columnas):
            print(num, end='  ')
        print()
        for i, fila in enumerate(tablero):
            print(self._letras_filas[i], end='  ')
            for casilla in fila:
                print(casilla, end="  ")
            print()

    def colocar_barco(self, fila, columna, tamano, orientacion):
        if orientacion == 'H':
            if columna + tamano > self._columnas:
                print("ERROR: Barco fuera de los límites horizontales")
                return False
            for i in range(tamano):
                if self._tablero[fila][columna + i] != '.':
                    print("ERROR: Espacio ya ocupado")
                    return False
            for i in range(tamano):
                self._tablero[fila][columna + i] = 'B'
        elif orientacion == 'V':
            if fila + tamano > self._filas:
                print("ERROR: Barco fuera de los límites verticales")
                return False
            for i in range(tamano):
                if self._tablero[fila + i][columna] != '.':
                    print("ERROR: Espacio ya ocupado")
                    return False
            for i in range(tamano):
                self._tablero[fila + i][columna] = 'B'
        else:
            print("ERROR: Orientación inválida")
            return False
        return True

    def disparar(self, fila, columna):
        if self._tablero[fila][columna] == 'B':
            self._tablero_visible[fila][columna] = 'X'
            self._tablero[fila][columna] = '.'
            print("¡Tocado!")
        else:
            self._tablero_visible[fila][columna] = 'O'
            print("Agua")

    def comprobar_ganador(self):
        for fila in self._tablero:
            if 'B' in fila:
                return False
        return True

    def jugar(self):
        print("Jugador 1, coloca tus barcos.")
        self.mostrar_tablero(self._tablero)
        barcos = [(2, 'Barco de 2 espacios'), (3, 'Primer barco de 3 espacios'), (3, 'Segundo barco de 3 espacios')]
        for tamano, nombre in barcos:
            colocado = False
            while not colocado:
                fila = input(f"Introduce la fila para el {nombre}: ").upper()
                columna = input(f"Introduce la columna para el {nombre}: ").upper()
                orientacion = input(f"Introduce la orientación (H/V) para el {nombre}: ").upper()
                if fila.isalpha() and len(fila) == 1:
                    if fila in self._letras_filas:
                        fila = self._letras_filas.index(fila)
                    else:
                        print("ERROR: Fila no válida")
                        continue
                else:
                    fila = int(fila)

                if columna.isalpha() and len(columna) == 1:
                    columna = self._letras_filas.index(columna)
                else:
                    columna = int(columna)

                colocado = self.colocar_barco(fila, columna, tamano, orientacion)
                self.mostrar_tablero(self._tablero)

        print("\nJugador 2, intenta destruir los barcos en 20 intentos.")
        intentos = 20
        while intentos > 0:
            print(f"\nIntentos restantes: {intentos}")
            self.mostrar_tablero(self._tablero_visible)
            fila = input("Introduce la fila para disparar: ").upper()
            columna = input("Introduce la columna para disparar: ").upper()

            if columna.isalpha() and len(columna) == 1:
                columna = self._letras_filas.index(columna)
            else:
                columna = int(columna)

            if fila.isalpha() and len(fila) == 1:
                if fila in self._letras_filas:
                    fila = self._letras_filas.index(fila)
                else:
                    print("ERROR: Fila no válida")
                    continue
            else:
                fila = int(fila)

            self.disparar(fila, columna)
            if self._tablero_visible[fila][columna] == 'X':
                continue

            intentos -= 1
            if self.comprobar_ganador():
                print("¡Felicidades Jugador 2, has ganado!")
                return

        print("¡Felicidades Jugador 1, has ganado!")


juego = HundirLosNavios(7, 8)
juego.jugar()

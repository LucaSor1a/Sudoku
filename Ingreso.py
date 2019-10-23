from Sudoku import Sudoku
from API import API


class UserInput():

    def __init__(self):
        self.sizev = 0

    def numberInput(self, number):
        # Controla que el valor ingresado sea uno permitido, dentro del rango
        if (number > 0 and number <= self.sizev):
            return True
        else:
            return False

    def position(self, row, column):
        # Controla que la coordenada ingresada sea una permitida
        if (row > 0 and row <= self.sizev and column > 0 and
                column <= self.sizev):
            return True
        else:
            return False

    def dimention(self):
        # Controla que el usuario ingrese una dimension valida
        if (self.sizev != 4 and self.sizev != 9):
            return False
        else:
            return True

    def size(self):
        # Pide el tamano del tablero del sudoku y controla que este permitido
        try:
            self.sizev = int(input("Ingrese la dimension " +
                                   "del sudoku (4 o 9): "))
            if (not self.dimention()):
                raise ValueError
        except ValueError:
            print("Ingresaste un valor no permitido, intentalo de nuevo")
            raise ValueError

    def getValues(self):
        # Toma valores para las coordenadas y para el valor de la casilla
        number = 0
        row = 0
        column = 0
        while not self.numberInput(number) or not self.position(row, column):
            try:
                row = int(input("\nFila: "))
                column = int(input("Columna: "))
                number = int(input("Valor de la casilla: "))
                if not (self.numberInput(number) and
                        self.position(row, column)):
                    raise ValueError
            except ValueError:
                print("Ingresaste un valor no permitido, intentalo de nuevo")
                raise ValueError
        uinput = [row - 1, column - 1, number]
        return uinput

    def run(self):
        # Instancia del juego
        while not self.dimention():
            self.size()
        api = API(self.sizev)
        sudoku = Sudoku(api.Table(), self.sizev)
        while not sudoku.is_over():
            print(sudoku.showTable())
            check, error_message = sudoku.playing(self.getValues())
            if not check:
                print(error_message)
        print("\n\nFelicitaciones!!!!")
        print("Terminaste el juego de Sudoku\n\n")
        print(sudoku.showTable())
        return sudoku.showTable()


if __name__ == "__main__":
    UserInput().run()

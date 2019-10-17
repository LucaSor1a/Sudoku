from Sudoku import Sudoku
from API import API


class UserInput():

    # Controla que el valor ingresado sea uno permitido, dentro del rango
    def numberInput(self, number, sizev):
        if (number > 0 and number <= sizev):
            return True
        else:
            return False

    # Controla que la coordenada ingresada sea una permitida
    def position(self, row, column, sizev):
        if (row > 0 and row <= sizev and column > 0 and column <= sizev):
            return True
        else:
            return False

    # Controla que el usuario ingrese una dimension valida
    def dimention(self, sizev):
        if (sizev != 4 and sizev != 9):
            return False
        else:
            return True

    # Pide el tamano del tablero del sudoku y controla que este permitido
    def size(self):
        try:
            sizev = int(input("Ingrese la dimension del sudoku (4 o 9): "))
            if (self.dimention(sizev)):
                return sizev
            raise ValueError
        except ValueError:
            print("Ingresaste un valor no permitido, intentalo de nuevo")

    # Toma valores validos para las coordenadas y para el valor de la casilla
    def getValues(self, sizev):
        number = 0
        row = 0
        column = 0
        while not self.numberInput(number, sizev) or not self.position(row,
                                                                       column,
                                                                       sizev):
            try:
                row = int(input("\nFila: "))
                column = int(input("Columna: "))
                number = int(input("Valor de la casilla: "))
            except ValueError:
                print("Ingresaste un valor no permitido, intentalo de nuevo")
            if (self.numberInput(number, sizev) and self.position(row,
                                                                  column,
                                                                  sizev)):
                uinput = [row - 1, column - 1, number]
                return uinput
            raise ValueError

    # Instancia del juego
    def run(self):
        ui = UserInput()
        sizev = 0
        while not self.dimention(sizev):
            sizev = ui.size()
        api = API(sizev)
        table = api.Table()
        sudoku = Sudoku(table, sizev)
        ori_pos = sudoku.position_originals()
        while not sudoku.is_over():
            print(sudoku.showTable())
            check, error_message = sudoku.playing(
                ui.getValues(sizev),
                ori_pos,
            )
            if not check:
                print(error_message)
        print("\n\nFelicitaciones!!!!")
        print("Terminaste el juego de Sudoku\n\n")
        print(sudoku.showTable())


if __name__ == "__main__":
    UserInput().run()

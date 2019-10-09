from Sudoku import Sudoku
from API import API
import sys
import math


class NotANumberException(Exception):
    pass


class UserInput():

    def numberInput(self, number, sizev):
        if (number > 0 and number <= sizev):
            return True
        else:
            return False

    def position(self, row, column, sizev):
        if (row > 0 and row <= sizev and column > 0 and column <= sizev):
            return True
        else:
            return False

    def showTable(self, table, sizev):
        sys.stdout.write("     ")
        for x in range(sizev):
            sys.stdout.write(str(x + 1) + "  ")
            if (x == (math.sqrt(sizev)-1) or (x == (math.sqrt(sizev)*2-1))):
                sys.stdout.write(" ")
        print("")
        for i in range(sizev):
            if i % math.sqrt(sizev) == 0:
                sys.stdout.write("   ")
                sys.stdout.write("----"*(sizev-1))
                print("")
            sys.stdout.write(str(i + 1) + "  ")
            for j in range(sizev):
                if j % math.sqrt(sizev) == 0:
                    sys.stdout.write("|")
                sys.stdout.write(table[i][j].replace("", " "))
            print("")

    def dimention(self, sizev):
        if (sizev != 4 and sizev != 9):
            return False
        else:
            return True

    def size(self):
        sizev = 0
        while not self.dimention(sizev):
            try:
                sizev = int(input("Ingrese la dimension del sudoku (4 o 9): "))
                if (self.dimention(sizev)):
                    return sizev
                print("Ingresaste un valor no permitido, intentalo de nuevo")
            except ValueError:
                print("Ingresaste un valor no permitido, intentalo de nuevo")

    def getValues(self, table, sizev):
        self.showTable(table, sizev)
        number = 0
        row = 0
        column = 0
        while not self.numberInput(number, sizev) or not self.position(row,
                                                                       column,
                                                                       sizev):
            try:
                row = int(input("\n\nFila: "))
                column = int(input("Columna: "))
                number = int(input("Valor de la casilla: "))
            except ValueError:
                pass
            if (self.numberInput(number, sizev) and self.position(row,
                                                                  column,
                                                                  sizev)):
                uinput = [row - 1, column - 1, number]
                return uinput
            print("Ingresaste un valor no permitido, intentalo de nuevo")

    def run(self):
        ui = UserInput()
        sizev = ui.size()
        api = API(sizev)
        table = api.Table()
        sudoku = Sudoku(table, sizev)
        ori_pos = sudoku.position_originals()
        while not sudoku.is_over():
            sudoku.playing(ui.getValues(table, sizev), ori_pos)
        print("\n\nFelicitaciones!!!!")
        print("Terminaste el juego de Sudoku\n\n")
        ui.showTable(table, sizev)


if __name__ == "__main__":
    UserInput().run()

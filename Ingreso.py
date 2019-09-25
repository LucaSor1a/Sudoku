from Sudoku import Sudoku

class UserInput():

    def getValues(self):
        while True:
            row = int(input("Fila: "))
            column = int(input("Columna: "))
            number = int(input("Valor de la casilla: "))
            if (numberInput(number) and position(row, column)):
                uinput = [row, column - 1, number - 1]
                return uinput
            if (Sudoku.is_over):
                break

    def numberInput(self, number):
        if (number > 0 and number < 10):
            return True
        else:
            return False

    def position(self, row, column):
        if (row > 0 and row < 10 and column > 0 and column < 10):
            return True
        else:
            return False
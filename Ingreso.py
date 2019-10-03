from Sudoku import Sudoku
from API import API
import sys

class UserInput():

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
    
    def showTable(self, table):
        for i in range(9):
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    sys.stdout.write("|")    
                sys.stdout.write(table[i][j].replace("", " "))
            print("")
            if (i - 2) % 3 == 0 and i != 8: 
                print("----------------------------")

    def getValues(self, table):
        self.showTable(table)
        number = 0
        row = 0
        column = 0
        while not self.numberInput(number) or not self.position(row, column):
            row = int(input("\n\nFila: "))
            column = int(input("Columna: "))
            number = int(input("Valor de la casilla: "))
            if (self.numberInput(number) and self.position(row, column)):
                uinput = [row - 1, column - 1, number]
                return uinput
            print("Ingresaste un valor no permitido, intentalo de nuevo")


ui = UserInput()
api = API()
table = api.Table()
sudoku = Sudoku(table)
ori_pos = sudoku.position_originals()
while not sudoku.is_over():
    sudoku.playing(ui.getValues(table), ori_pos)
print("\n\nFelicitaciones!!!!")
print("Terminaste el juego de Sudoku\n\n")
ui.showTable(table)
from Sudoku import Sudoku
import sys

class UserInput():

    def table(self):
        #table = ["53xx7xxxx", "6xx195xxx", "x98xxxx6x", "8xxx6xxx3", "4xx8x3xx1", "7xxx2xxx6", "x6xxxx28x", "xxx419xx5", "xxxx8xx79"]
        table = ["534678912", "672195348", "198342567", "859761423", "426853791", "713924856", "961537284", "287419635", "345x86179"]
        return table

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
table = ui.table()
sudoku = Sudoku(table)
ori_pos = sudoku.position_originals(table)
while not sudoku.is_over(table):
    sudoku.playing(ui.getValues(table), ori_pos, table)
print("\n\nFelicitaciones!!!!")
print("Terminaste el juego de Sudoku\n\n")
ui.showTable(table)
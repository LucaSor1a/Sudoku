# overwrite, is_over, write, check,
from Ingreso import UserInput

class Sudoku():
    
    def __init__(self, uinput):
        self.row = uinput[0]
        self.column = uinput[1]
        self.value = uinput[2]
        self.table = ["53xx7xxxx", "6xx195xxx", "x98xxxx6x", "8xxx6xxx3", "4xx8x3xx1", "7xxx2xxx6", "x6xxxx28x", "xxx419xx5", "xxxx8xx79"]

    def position_originals(self, table):
        ori_pos = []
        for i in range(9):
            for j in range(9):
                if self.table[i][j] != "x":
                    ori_pos.append(str(i)+str(j))
    
    def check_reps_row(self, table, row, value):
        if (value not in table[row]):
            return True
        else:
            return False
    
    def check_reps_column(self, table, column, value):
        c = 0
        for i in range(9):
            if (table[i][column] != value):
                c += 1
        if (c == 9):
            return True
        else:
            return False
    def check_reps_block(self, table, row, column, value):
        pass

    def check(self):
        c = 0
        if check_reps_row(table, row, value) == False:
            print ("El valor ya existe en la Fila")
        else:
            c += 1
        if check_reps_column(table, column, value) == False:
            print ("El valor ya existe en la Columna")
        else:
            c += 1
        if check_reps_block(table, row, column, value) == False:
            print ("El valor ya existe en el Bloque")
        else:
            c += 1
        if c == 3:
            return True
        else:
            return False



uinput = UserInput.getValues()
sudoku = Sudoku(uinput)

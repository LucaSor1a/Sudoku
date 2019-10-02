class Sudoku():
    
    def __init__(self, table):
        table = ["53xx7xxxx", "6xx195xxx", "x98xxxx6x", "8xxx6xxx3", "4xx8x3xx1", "7xxx2xxx6", "x6xxxx28x", "xxx419xx5", "xxxx8xx79"]

    def position_originals(self, table):
        ori_pos = []
        for i in range(9):
            for j in range(9):
                if table[i][j] != "x":
                    ori_pos.append(str(i)+str(j))
        return ori_pos
    
    def check_reps_row(self, table, row, value):
        if (str(value) not in table[row]):
            return True
        else:
            return False
    
    def check_reps_col(self, table, column, value):
        for i in range(9):
            if (table[i][column] == str(value)):
                return False
            else:
                return True

    def check_reps_block(self, table, row, column, value):
        if (row < 3):
            row = 0
        elif (row >= 3 and row < 6):
            row = 3
        else:
            row = 6
        if (column < 3):
            column = 0
        elif (column >= 3 and column < 6):
            column = 3
        else:
            column = 6
        for i in range(3):
            for j in range(3):
                if (table[row + i][column + j] == str(value)):
                    return False
        return True

    def check(self, table, row, column, value):
        c = 0
        if self.check_reps_row(table, row, value) == False:
            print ("El valor ya existe en la Fila")
        else:
            c += 1
        if self.check_reps_col(table, column, value) == False:
            print ("El valor ya existe en la Columna")
        else:
            c += 1
        if self.check_reps_block(table, row, column, value) == False:
            print ("El valor ya existe en el Bloque")
        else:
            c += 1
        if c == 3:
            return True
        else:
            return False

    def overwrite(self, table, row, column, ori_pos):
        if ((str(row)+str(column)) in ori_pos):
            return False
        else:
            return True

    def write(self, table, row, column, value, ori_pos):
        if (self.overwrite(table, row, column, ori_pos) == False):
            print ("Perdon, no se puede escribir en esa posicion")
        else:
            table[row] = table[row][:column] + str(value) + table[row][column+1:]
        return table
    
    def is_over(self, table):
        for i in range(9):
            if ("x" in table[i]):
                return False
        return True

    def playing(self, uinput, ori_pos, table):
        row = uinput[0]
        column = uinput[1]
        value = uinput[2]
        if self.check(table, row, column, value) == True:
            self.write(table, row, column, value, ori_pos)
        self.is_over(table)

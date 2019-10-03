class Sudoku():
    
    def __init__(self, table):
        self.table = table

    def position_originals(self):
        ori_pos = []
        for i in range(9):
            for j in range(9):
                if self.table[i][j] != "x":
                    ori_pos.append(str(i)+str(j))
        return ori_pos
    
    def check_reps_row(self, row, value):
        if (str(value) not in self.table[row]):
            return True
        else:
            return False
    
    def check_reps_col(self, column, value):
        for i in range(9):
            if (self.table[i][column] == str(value)):
                return False
            else:
                return True

    def check_reps_block(self, row, column, value):
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
                if (self.table[row + i][column + j] == str(value)):
                    return False
        return True

    def check(self, row, column, value):
        c = 0
        if self.check_reps_row(row, value) == False:
            print ("El valor ya existe en la Fila")
        else:
            c += 1
        if self.check_reps_col(column, value) == False:
            print ("El valor ya existe en la Columna")
        else:
            c += 1
        if self.check_reps_block(row, column, value) == False:
            print ("El valor ya existe en el Bloque")
        else:
            c += 1
        if c == 3:
            return True
        else:
            return False

    def overwrite(self, row, column, ori_pos):
        if ((str(row)+str(column)) in ori_pos):
            return False
        else:
            return True

    def write(self, row, column, value, ori_pos):
        if (self.overwrite(row, column, ori_pos) == False):
            print ("Perdon, no se puede escribir en esa posicion")
        else:
            self.table[row] = self.table[row][:column] + str(value) + self.table[row][column+1:]
        return self.table
    
    def is_over(self):
        for i in range(9):
            if ("x" in self.table[i]):
                return False
        return True

    def playing(self, uinput, ori_pos):
        row = uinput[0]
        column = uinput[1]
        value = uinput[2]
        if self.check(row, column, value) == True:
            self.write(row, column, value, ori_pos)
        self.is_over()

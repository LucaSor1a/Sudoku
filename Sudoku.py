import math


class Sudoku():

    def __init__(self, table, size):
        self.table = table
        self.size = size

    def position_originals(self):
        ori_pos = []
        for i in range(self.size):
            for j in range(self.size):
                if self.table[i][j] != "x":
                    ori_pos.append(str(i)+str(j))
        return ori_pos

    def check_reps_row(self, row, value):
        if (str(value) not in self.table[row]):
            return True
        else:
            return False

    def check_reps_col(self, column, value):
        for i in range(self.size):
            if (self.table[i][column] == str(value)):
                return False
            else:
                return True

    def check_reps_block(self, row, column, value):
        if (row < math.sqrt(self.size)):
            row = 0
        elif (row >= math.sqrt(self.size) and row < math.sqrt(self.size) * 2):
            row = math.sqrt(self.size)
        else:
            row = math.sqrt(self.size) * 2

        if (column < math.sqrt(self.size)):
            column = 0
        elif (column >= math.sqrt(self.size) and
              column < math.sqrt(self.size) * 2):
            column = math.sqrt(self.size)
        else:
            column = math.sqrt(self.size) * 2
        for i in range(int(math.sqrt(self.size))):
            for j in range(int(math.sqrt(self.size))):
                if (self.table[int(row + i)][int(column + j)] == str(value)):
                    return False
        return True

    def check(self, row, column, value):
        c = 0
        if self.check_reps_row(row, value) is False:
            print("El valor ya existe en la Fila")
        else:
            c += 1
        if self.check_reps_col(column, value) is False:
            print("El valor ya existe en la Columna")
        else:
            c += 1
        if self.check_reps_block(row, column, value) is False:
            print("El valor ya existe en el Bloque")
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
        if (self.overwrite(row, column, ori_pos) is False):
            print("Perdon, no se puede escribir en esa posicion")
        else:
            first = self.table[row][:column]
            second = self.table[row][column+1:]
            self.table[row] = first + str(value) + second
        return self.table

    def is_over(self):
        for i in range(self.size):
            if ("x" in self.table[i]):
                return False
        return True

    def playing(self, uinput, ori_pos):
        row = uinput[0]
        column = uinput[1]
        value = uinput[2]
        if self.check(row, column, value) is True:
            self.write(row, column, value, ori_pos)

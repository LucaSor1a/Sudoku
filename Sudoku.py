import math


class Sudoku():

    def __init__(self, table, size):
        self.table = table
        self.size = size

    # Forma un vector de coordenadas con la posicion de los valores originales
    def position_originals(self):
        ori_pos = []
        for i in range(self.size):
            for j in range(self.size):
                if (self.table[i][j] != "x"):
                    ori_pos.append(str(i)+str(j))
        return ori_pos

    # Se fija que el valor que se quiere escribir no este en la fila
    def check_reps_row(self, row, value):
        if (str(value) not in self.table[row]):
            return True
        else:
            print("El valor ya existe en la Fila")
            return False

    # Se fija que el valor que se quiere escribir no este en la columna
    def check_reps_col(self, column, value):
        for i in range(self.size):
            if (self.table[i][column] == str(value)):
                print("El valor ya existe en la Columna")
                return False
            else:
                return True

    # Se fija que el valor que se quiere escribir no este en el bloque
    def check_reps_block(self, row, column, value):
        row = int(row / math.sqrt(self.size)) * math.sqrt(self.size)
        column = int(column / math.sqrt(self.size)) * math.sqrt(self.size)
        for i in range(int(math.sqrt(self.size))):
            for j in range(int(math.sqrt(self.size))):
                if (self.table[int(row + i)][int(column + j)] == str(value)):
                    print("El valor ya existe en el Bloque")
                    return False
        return True

    # Se fija que el valor que se quiere escribir no se encuentre ya escrito
    def check(self, row, column, value):
        cr = self.check_reps_row(row, value)
        cc = self.check_reps_col(column, value)
        cb = self.check_reps_block(row, column, value)
        if (cr and cc and cb):
            return True
        else:
            return False

    # Dice si donde se quiere escribir es o no un valor original de la tabla
    def overwrite(self, row, column, ori_pos):
        if ((str(row)+str(column)) in ori_pos):
            return False
        else:
            return True

    # Se encarga de escribir la tabla si es que se puede
    def write(self, row, column, value, ori_pos):
        if (self.overwrite(row, column, ori_pos) is False):
            print("Perdon, no se puede escribir en esa posicion")
        else:
            first = self.table[row][:column]
            second = self.table[row][column+1:]
            self.table[row] = first + str(value) + second
        return self.table

    # Se fija si la tabla esta completa
    def is_over(self):
        for i in range(self.size):
            if ("x" in self.table[i]):
                return False
        return True

    # La ejecucion del juego
    def playing(self, uinput, ori_pos):
        row = uinput[0]
        column = uinput[1]
        value = uinput[2]
        if (self.check(row, column, value) is True):
            self.write(row, column, value, ori_pos)

import math


class Sudoku():

    def __init__(self, table, size):
        self.table = table
        self.size = size

    # Forma un vector de coordenadas con la posicion de los valores originales
    def position_originals(self):
        ori_pos = []  # El vector
        for i in range(self.size):
            for j in range(self.size):
                if (self.table[i][j] != "x"):
                    # Si tiene un numero agrega la coordenada al vector
                    ori_pos.append(str(i)+str(j))
        return ori_pos

    # Se fija que el valor que se quiere escribir no este en la fila
    def check_reps_row(self, row, value):
        if (str(value) not in self.table[row]):
            return True, ""
        else:
            return False, "El valor ya existe en la Fila"

    # Se fija que el valor que se quiere escribir no este en la columna
    def check_reps_col(self, column, value):
        for i in range(self.size):
            if (self.table[i][column] == str(value)):
                return False, "El valor ya existe en la Columna"
        return True, ""

    # Propiedad que devuelve la raiz del tamano de la tabla
    @property
    def sqrt(self):
        return int(math.sqrt(self.size))

    # Calcula el origen del bolque, para su chequeo
    def calc_row_col(self, x):
        return (x // self.sqrt) * self.sqrt

    # Se fija que el valor que se quiere escribir no este en el bloque
    def check_reps_block(self, row, column, value):
        # Toma el valor de inicio del bloque
        row = self.calc_row_col(row)
        column = self.calc_row_col(column)
        for i in range(self.sqrt):
            for j in range(self.sqrt):
                if (self.table[int(row + i)][int(column + j)] == str(value)):
                    return False, "El valor ya existe en el Bloque"
        return True, ""

    # Dice si donde se quiere escribir es o no un valor original de la tabla
    def overwrite(self, row, column, ori_pos):
        if ((str(row)+str(column)) in ori_pos):
            return False, "Perdon, no se puede escribir en esa posicion"
        else:
            return True, ""

    # Se fija que el valor que se quiere escribir no se encuentre ya escrito
    def check(self, row, column, value, ori_pos):
        error_message = ["", "", "", ""]
        cr, error_message[0] = self.check_reps_row(row, value)
        cc, error_message[1] = self.check_reps_col(column, value)
        cb, error_message[2] = self.check_reps_block(row, column, value)
        co, error_message[3] = self.overwrite(row, column, ori_pos)
        if (cr and cc and cb and co):
            return True, ""
        else:
            for x in range(4):
                if error_message[3-x] != "":
                    return False, error_message[3-x]

    # Se encarga de escribir la tabla si es que se puede
    def write(self, row, column, value):
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
        check, error_message = self.check(row, column, value, ori_pos)
        if check:
            self.write(row, column, value)
            return True, ""
        else:
            return False, error_message

    # Muestra la tabla al jugador
    def showTable(self):
        TableInString = "\n     "
        for x in range(self.size):
            TableInString += (str(x + 1) + "  ")
            if (x == (self.sqrt-1) or (x == (self.sqrt*2-1))):
                TableInString += (" ")
        TableInString += "\n"
        for i in range(self.size):
            if (i % self.sqrt == 0):
                TableInString += ("   " + "----"*(self.size-1) + "\n")
            TableInString += (str(i + 1) + "  ")
            for j in range(self.size):
                if (j % self.sqrt == 0):
                    TableInString += ("|")
                TableInString += str(self.table[i][j].replace("", " "))
            TableInString += "\n"
        return TableInString

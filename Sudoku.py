import math


class Sudoku():

    def __init__(self, table, size):
        self.table = table
        self.size = size
        # Forma un vector de coordenadas con la posicion de
        # los valores originales
        self.ori_pos = []  # El vector
        for i in range(self.size):
            for j in range(self.size):
                if (self.table[i][j] != "x"):
                    # Si tiene un numero agrega la coordenada al vector
                    self.ori_pos.append(str(i)+str(j))

    def check_reps_row(self, row, value):
        # Se fija que el valor que se quiere escribir no este en la fila
        if (str(value) not in self.table[row]):
            return True, ""
        else:
            return False, "El valor ya existe en la Fila"

    def check_reps_col(self, column, value):
        # Se fija que el valor que se quiere escribir no este en la columna
        for i in range(self.size):
            if (self.table[i][column] == str(value)):
                return False, "El valor ya existe en la Columna"
        return True, ""

    @property
    def sqrt(self):
        # Propiedad que devuelve la raiz del tamano de la tabla
        return int(math.sqrt(self.size))

    def calc_row_col(self, x):
        # Calcula el origen del bolque, para su chequeo
        return (x // self.sqrt) * self.sqrt

    def check_reps_block(self, row, column, value):
        # Se fija que el valor que se quiere escribir no este en el bloque
        # Primero, toma el valor de inicio del bloque
        row = self.calc_row_col(row)
        column = self.calc_row_col(column)
        for i in range(self.sqrt):
            for j in range(self.sqrt):
                if (self.table[int(row + i)][int(column + j)] == str(value)):
                    return False, "El valor ya existe en el Bloque"
        return True, ""

    def overwrite(self, row, column):
        # Dice si hay un valor original en la pocicion que se quiere escribir
        if ((str(row)+str(column)) in self.ori_pos):
            return False, "Perdon, no se puede escribir en esa posicion"
        else:
            return True, ""

    def check(self, row, column, value):
        # Se fija si se puede escribir el valor deseado
        error_message = ["", "", "", ""]
        cr, error_message[0] = self.check_reps_row(row, value)
        cc, error_message[1] = self.check_reps_col(column, value)
        cb, error_message[2] = self.check_reps_block(row, column, value)
        co, error_message[3] = self.overwrite(row, column)
        if (cr and cc and cb and co):
            return True, ""
        else:
            for x in range(4):
                if error_message[3-x] != "":
                    return False, error_message[3-x]

    def write(self, row, column, value):
        # Se encarga de escribir la tabla si es que se puede
        first = self.table[row][:column]
        second = self.table[row][column+1:]
        self.table[row] = first + str(value) + second
        return self.table

    def is_over(self):
        # Se fija si la tabla esta completa
        for i in range(self.size):
            if ("x" in self.table[i]):
                return False
        return True

    def playing(self, uinput):
        # La ejecucion del juego
        row = uinput[0]
        column = uinput[1]
        value = uinput[2]
        check, error_message = self.check(row, column, value)
        if check:
            self.write(row, column, value)
            return True, ""
        else:
            return False, error_message

    def showTable(self):
        # Muestra la tabla al jugador
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

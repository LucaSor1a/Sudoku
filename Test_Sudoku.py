import unittest
from Sudoku import Sudoku
from parameterized import parameterized


class TestSudoku(unittest.TestCase):

    def setUp(self):
        self.table = ["53xx7xxxx", "6xx195xxx", "x98xxxx6x",
                      "8xxx6xxx3", "4xx8x3xx1", "7xxx2xxx6",
                      "x6xxxx28x", "xxx419xx5", "xxxx8xx79"]
        self.sudoku = Sudoku(self.table, 9)
        self.ori_pos = ["00", "01", "04", "10", "13", "14", "15", "21", "22",
                        "27", "30", "34", "38", "40", "43", "45", "48", "50",
                        "54", "58", "61", "66", "67", "73", "74", "75", "78",
                        "84", "87", "88"]

    @parameterized.expand([
        # Test de valores repetidos en la fila
        (0, 5),
        (1, 5),
        (2, 9),
        (3, 3),
        (4, 1),
        (5, 7),
        (6, 2),
        (7, 9),
        (8, 8),
    ])
    def test_row_repeated(self, row, value):
        self.assertEqual(self.sudoku.check_reps_row(row, value),
                         (False, "El valor ya existe en la Fila"))

    @parameterized.expand([
        # Test de valores NO repetidos en la fila
        (0, 2),
        (1, 3),
        (2, 5),
        (3, 5),
        (4, 7),
        (5, 3),
        (6, 9),
        (7, 6),
        (8, 1),
    ])
    def test_row_not_repeated(self, row, value):
        self.assertEqual(self.sudoku.check_reps_row(row, value),
                         (True, ""))

    @parameterized.expand([
        # Test de valores repetidos en la columna
        (0, 8),
        (1, 6),
        (2, 8),
        (3, 4),
        (4, 1),
        (5, 3),
        (6, 2),
        (7, 7),
        (8, 9),
    ])
    def test_column_repeated(self, column, value):
        self.assertEqual(self.sudoku.check_reps_col(column, value),
                         (False, "El valor ya existe en la Columna"))

    @parameterized.expand([
        # Test de valores NO repetidos en la columna
        (0, 2),
        (1, 1),
        (2, 7),
        (3, 3),
        (4, 4),
        (5, 7),
        (6, 1),
        (7, 5),
        (8, 2),
    ])
    def test_column_not_repeated(self, column, value):
        self.assertEqual(self.sudoku.check_reps_col(column, value),
                         (True, ""))

    @parameterized.expand([
        # Test de valores repetidos en el bloque
        (0, 0, 3),
        (2, 4, 7),
        (1, 6, 6),
        (4, 1, 4),
        (3, 5, 3),
        (3, 8, 6),
        (8, 0, 6),
        (6, 4, 9),
        (7, 7, 2)
    ])
    def test_block_repeated(self, row, column, value):
        self.assertEqual(self.sudoku.check_reps_block(row, column, value),
                         (False, "El valor ya existe en el Bloque"))

    @parameterized.expand([
        # Test de valores NO repetidos en el bloque
        (0, 0, 1),
        (2, 4, 2),
        (1, 6, 4),
        (4, 1, 5),
        (3, 5, 5),
        (3, 8, 5),
        (8, 0, 7),
        (6, 4, 3),
        (7, 7, 1)
    ])
    def test_block_not_repeated(self, row, column, value):
        self.assertEqual(self.sudoku.check_reps_block(row, column, value),
                         (True, ""))

    @parameterized.expand([
        # Test de valores que NO pueden ser cambiados
        (0, 0),
        (4, 0),
        (7, 3),
    ])
    def test_overwrite_originals(self, row, column):
        self.assertEqual(self.sudoku.overwrite(row, column),
                         (False,
                         "Perdon, no se puede escribir en esa posicion"))

    @parameterized.expand([
        # Test de valores que pueden ser cambiados
        (3, 7),
        (1, 6),
        (4, 7),
    ])
    def test_overwrite_originals_positive(self, row, column):
        self.assertEqual(self.sudoku.overwrite(row, column), (True, ""))

    @parameterized.expand([
        # Test de valores repetidos en el bloque
        (0, 2, 3),
        (2, 4, 7),
        (1, 6, 6),
        (4, 1, 4),
        (3, 5, 3),
        (3, 7, 6),
        (8, 0, 6),
        (6, 4, 9),
        (7, 7, 2)
    ])
    def test_check_repeated_Block(self, row, column, value):
        self.assertEqual(self.sudoku.check(row, column, value),
                         (False, "El valor ya existe en el Bloque"))

    @parameterized.expand([
        # Test de valores repetidos en la fila
        (0, 2, 7),
        (1, 7, 9),
        (2, 6, 9),
        (3, 6, 8),
        (4, 4, 4),
        (5, 1, 2),
        (6, 0, 2),
        (7, 0, 1),
        (8, 5, 7)
    ])
    def test_check_repeated_Row(self, row, column, value):
        self.assertEqual(self.sudoku.check(row, column, value),
                         (False, "El valor ya existe en la Fila"))

    @parameterized.expand([
        # Test de valores repetidos en la columna
        (6, 0, 4),
        (4, 1, 9),
        (7, 2, 8),
        (2, 3, 4),
        (2, 4, 8),
        (5, 5, 9),
        (2, 6, 2),
        (5, 7, 7),
        (0, 8, 9)
    ])
    def test_check_repeated_Column(self, row, column, value):
        self.assertEqual(self.sudoku.check(row, column, value),
                         (False, "El valor ya existe en la Columna"))

    @parameterized.expand([
        # Test de valores que NO pueden ser cambiados
        (0, 0, 3),
        (4, 0, 2),
        (7, 3, 1),
    ])
    def test_check_repeated_Overwrite(self, row, column, value):
        self.assertEqual(self.sudoku.check(row, column, value),
                         (False,
                          "Perdon, no se puede escribir en esa posicion"))

    @parameterized.expand([
        # Test de numeros validos
        (0, 2, 2),
        (4, 7, 2),
        (7, 6, 3),
    ])
    def test_check_not_repeated(self, row, column, value):
        self.assertEqual(self.sudoku.check(row, column, value), (True, ""))

    @parameterized.expand([
        # Test de juego terminado
        (["533175384", "612195537", "298376369",
          "882668363", "481863981", "717328356",
          "169836281", "916419925", "816288179"], 9),
        (["5331", "6121", "2983", "8826"], 4),
    ])
    def test_game_over(self, table, size):
        self.sudoku = Sudoku(table, size)
        self.assertTrue(self.sudoku.is_over())

    # Test de juego NO terminado
    def test_game_not_over(self):
        over = self.sudoku.is_over()
        self.assertFalse(over)

    @parameterized.expand([
        # Test de la tabla a imprimir
        (["xx3x", "x2x4",
          "xx23", "2x41"], 4,
         '\n     1  2   3  4   \n' +
         '   ------------\n' +
         '1  | x  x | 3  x \n' +
         '2  | x  2 | x  4 \n' +
         '   ------------\n' +
         '3  | x  x | 2  3 \n' +
         '4  | 2  x | 4  1 \n'),
        (["534x7xxxx", "6xx195xxx", "x98xxxx6x",
          "8xxx6xxx3", "4xx8x3xx1", "7xxx2xxx6",
          "x6xxxx28x", "xxx419xx5", "xxxx8xx79"], 9,
         '\n     1  2  3   4  5  6   7  8  9  \n' +
         '   --------------------------------\n' +
         '1  | 5  3  4 | x  7  x | x  x  x \n' +
         '2  | 6  x  x | 1  9  5 | x  x  x \n' +
         '3  | x  9  8 | x  x  x | x  6  x \n' +
         '   --------------------------------\n' +
         '4  | 8  x  x | x  6  x | x  x  3 \n' +
         '5  | 4  x  x | 8  x  3 | x  x  1 \n' +
         '6  | 7  x  x | x  2  x | x  x  6 \n' +
         '   --------------------------------\n' +
         '7  | x  6  x | x  x  x | 2  8  x \n' +
         '8  | x  x  x | 4  1  9 | x  x  5 \n' +
         '9  | x  x  x | x  8  x | x  7  9 \n')
    ])
    def test_print_table(self, table, size, stable):
        self.sudoku = Sudoku(table, size)
        self.assertEqual(self.sudoku.showTable(), stable)

    @parameterized.expand([
        # Test raiz del tamaño
        (["534x7xxxx", "6xx195xxx", "x98xxxx6x",
          "8xxx6xxx3", "4xx8x3xx1", "7xxx2xxx6",
          "x6xxxx28x", "xxx419xx5", "xxxx8xx79"], 9, 3),
        (["xx3x", "x2x4",
          "xx23", "2x41"], 4, 2)
    ])
    def test_sqrt(self, table, size, expected):
        self.sudoku = Sudoku(table, size)
        self.assertEqual(self.sudoku.sqrt, expected)

    @parameterized.expand([
        # Test del inicio del bloque
        (["534x7xxxx", "6xx195xxx", "x98xxxx6x",
          "8xxx6xxx3", "4xx8x3xx1", "7xxx2xxx6",
          "x6xxxx28x", "xxx419xx5", "xxxx8xx79"], 9, 2, 0),
        (["534x7xxxx", "6xx195xxx", "x98xxxx6x",
          "8xxx6xxx3", "4xx8x3xx1", "7xxx2xxx6",
          "x6xxxx28x", "xxx419xx5", "xxxx8xx79"], 9, 4, 3),
        (["534x7xxxx", "6xx195xxx", "x98xxxx6x",
          "8xxx6xxx3", "4xx8x3xx1", "7xxx2xxx6",
          "x6xxxx28x", "xxx419xx5", "xxxx8xx79"], 9, 7, 6),
        (["xx3x", "x2x4",
          "xx23", "2x41"], 4, 0, 0),
        (["xx3x", "x2x4",
          "xx23", "2x41"], 4, 2, 2)
    ])
    def test_calc_start_block(self, table, size, num, expected):
        self.sudoku = Sudoku(table, size)
        self.assertEqual(self.sudoku.calc_row_col(num), expected)

    # Test busqueda de los valores que no pueden ser cambiados
    def test_position_originals(self):
        self.table = ["53xx7xxxx", "6xx195xxx", "x98xxxx6x",
                      "8xxx6xxx3", "4xx8x3xx1", "7xxx2xxx6",
                      "x6xxxx28x", "xxx419xx5", "xxxx8xx79"]
        self.sudoku = Sudoku(self.table, 9)
        self.assertEqual(self.sudoku.ori_pos,
                         ["00", "01", "04", "10", "13", "14", "15", "21", "22",
                          "27", "30", "34", "38", "40", "43", "45", "48", "50",
                          "54", "58", "61", "66", "67", "73", "74", "75", "78",
                          "84", "87", "88"])

    # Test de la escritura de la tabla
    def test_written(self):
        self.sudoku.write(0, 2, 4)
        self.assertEqual(self.table, ["534x7xxxx", "6xx195xxx", "x98xxxx6x",
                                      "8xxx6xxx3", "4xx8x3xx1", "7xxx2xxx6",
                                      "x6xxxx28x", "xxx419xx5", "xxxx8xx79"])

    # Test de intento de escritura exitoso
    def test_playing_write(self):
        self.assertEqual(self.sudoku.playing([0, 2, 2]),
                         (True, ""))

    # Test de intento de escritura fallido
    def test_playing_did_nothing(self):
        self.assertEqual(self.sudoku.playing([0, 0, 2]),
                         (False,
                          "Perdon, no se puede escribir en esa posicion"))


if __name__ == "__main__":
    unittest.main()

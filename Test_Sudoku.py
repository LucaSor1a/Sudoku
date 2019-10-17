import unittest
from Sudoku import Sudoku


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

    def test_row_repeated(self):
        self.assertEqual(self.sudoku.check_reps_row(0, 5),
                         (False, "El valor ya existe en la Fila"))

    def test_row_not_repeated(self):
        self.assertEqual(self.sudoku.check_reps_row(0, 1),
                         (True, ""))

    def test_column_repeated(self):
        self.assertEqual(self.sudoku.check_reps_col(0, 5),
                         (False, "El valor ya existe en la Columna"))

    def test_column_not_repeated(self):
        self.assertEqual(self.sudoku.check_reps_col(0, 1),
                         (True, ""))

    def test_block_repeated(self):
        self.assertEqual(self.sudoku.check_reps_block(1, 1, 5),
                         (False, "El valor ya existe en el Bloque"))

    def test_block_not_repeated(self):
        self.assertEqual(self.sudoku.check_reps_block(0, 2, 1,),
                         (True, ""))

    def test_overwrite_originals(self):
        self.assertEqual(self.sudoku.overwrite(0, 0),
                         (False,
                         "Perdon, no se puede escribir en esa posicion"))

    def test_overwrite_originals_positive(self):
        self.assertEqual(self.sudoku.overwrite(0, 2), (True, ""))

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

    def test_check_repeated_Block(self):
        self.assertEqual(self.sudoku.check(0, 2, 5),
                         (False, "El valor ya existe en el Bloque"))

    def test_check_repeated_Row(self):
        self.assertEqual(self.sudoku.check(0, 6, 7),
                         (False, "El valor ya existe en la Fila"))

    def test_check_repeated_Column(self):
        self.assertEqual(self.sudoku.check(6, 4, 6),
                         (False, "El valor ya existe en la Columna"))

    def test_check_repeated_Overwrite(self):
        self.assertEqual(self.sudoku.check(0, 0, 3),
                         (False,
                          "Perdon, no se puede escribir en esa posicion"))

    def test_check_not_repeated(self):
        self.assertEqual(self.sudoku.check(0, 2, 4), (True, ""))

    def test_written(self):
        self.sudoku.write(0, 2, 4)
        self.assertEqual(self.table, ["534x7xxxx", "6xx195xxx", "x98xxxx6x",
                                      "8xxx6xxx3", "4xx8x3xx1", "7xxx2xxx6",
                                      "x6xxxx28x", "xxx419xx5", "xxxx8xx79"])

    def test_game_not_over(self):
        over = self.sudoku.is_over()
        self.assertFalse(over)

    def test_game_over(self):
        table = ["533175384", "612195537", "298376369",
                 "882668363", "481863981", "717328356",
                 "169836281", "916419925", "816288179"]
        self.sudoku = Sudoku(table, 9)
        over = self.sudoku.is_over()
        self.assertTrue(over)

    def test_game_over_2(self):
        table = ["5331", "6121", "2983", "8826"]
        self.sudoku = Sudoku(table, 4)
        over = self.sudoku.is_over()
        self.assertTrue(over)

    def test_print_table_4(self):
        table = ["xx3x", "x2x4",
                 "xx23", "2x41"]
        self.sudoku = Sudoku(table, 4)
        self.assertEqual(self.sudoku.showTable(),
                         str('\n     1  2   3  4   \n' +
                             '   ------------\n' +
                             '1  | x  x | 3  x \n' +
                             '2  | x  2 | x  4 \n' +
                             '   ------------\n' +
                             '3  | x  x | 2  3 \n' +
                             '4  | 2  x | 4  1 \n'))

    def test_print_table_9(self):
        table = ["534x7xxxx", "6xx195xxx", "x98xxxx6x",
                 "8xxx6xxx3", "4xx8x3xx1", "7xxx2xxx6",
                 "x6xxxx28x", "xxx419xx5", "xxxx8xx79"]
        self.sudoku = Sudoku(table, 9)
        self.assertEqual(self.sudoku.showTable(),
                         str('\n     1  2  3   4  5  6   7  8  9  \n' +
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
                             '9  | x  x  x | x  8  x | x  7  9 \n'))

    def test_playing_write(self):
        self.assertEqual(self.sudoku.playing([0, 2, 2]),
                         (True, ""))

    def test_playing_did_nothing(self):
        self.assertEqual(self.sudoku.playing([0, 0, 2]),
                         (False,
                          "Perdon, no se puede escribir en esa posicion"))

    def test_sqrt_9(self):
        table = ["534x7xxxx", "6xx195xxx", "x98xxxx6x",
                 "8xxx6xxx3", "4xx8x3xx1", "7xxx2xxx6",
                 "x6xxxx28x", "xxx419xx5", "xxxx8xx79"]
        self.sudoku = Sudoku(table, 9)
        self.assertEqual(self.sudoku.sqrt, 3)

    def test_sqrt_4(self):
        table = ["xx3x", "x2x4",
                 "xx23", "2x41"]
        self.sudoku = Sudoku(table, 4)
        self.assertEqual(self.sudoku.sqrt, 2)

    """
    def calc_row_col(self, x):
        return (x // self.sqrt) * self.sqrt
    """
    def test_calc_start_block_1_9(self):
        table = ["534x7xxxx", "6xx195xxx", "x98xxxx6x",
                 "8xxx6xxx3", "4xx8x3xx1", "7xxx2xxx6",
                 "x6xxxx28x", "xxx419xx5", "xxxx8xx79"]
        self.sudoku = Sudoku(table, 9)
        self.assertEqual(self.sudoku.calc_row_col(2), 0)

    def test_calc_start_block_2_9(self):
        table = ["534x7xxxx", "6xx195xxx", "x98xxxx6x",
                 "8xxx6xxx3", "4xx8x3xx1", "7xxx2xxx6",
                 "x6xxxx28x", "xxx419xx5", "xxxx8xx79"]
        self.sudoku = Sudoku(table, 9)
        self.assertEqual(self.sudoku.calc_row_col(4), 3)

    def test_calc_start_block_3_9(self):
        table = ["534x7xxxx", "6xx195xxx", "x98xxxx6x",
                 "8xxx6xxx3", "4xx8x3xx1", "7xxx2xxx6",
                 "x6xxxx28x", "xxx419xx5", "xxxx8xx79"]
        self.sudoku = Sudoku(table, 9)
        self.assertEqual(self.sudoku.calc_row_col(7), 6)

    def test_calc_start_block_1_4(self):
        table = ["xx3x", "x2x4",
                 "xx23", "2x41"]
        self.sudoku = Sudoku(table, 4)
        self.assertEqual(self.sudoku.calc_row_col(0), 0)

    def test_calc_start_block_2_4(self):
        table = ["xx3x", "x2x4",
                 "xx23", "2x41"]
        self.sudoku = Sudoku(table, 4)
        self.assertEqual(self.sudoku.calc_row_col(2), 2)


if __name__ == "__main__":
    unittest.main()

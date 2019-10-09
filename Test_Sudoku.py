import unittest
from Sudoku import Sudoku


class TestSudoku(unittest.TestCase):

    def setUp(self):
        self.table = ["53xx7xxxx", "6xx195xxx", "x98xxxx6x", "8xxx6xxx3",
                      "4xx8x3xx1", "7xxx2xxx6", "x6xxxx28x", "xxx419xx5",
                      "xxxx8xx79"]
        self.sudoku = Sudoku(self.table, 9)

    def test_table_9_rows(self):
        self.assertEqual(len(self.sudoku.table), 9)

    def test_table_9_columns(self):
        for i in range(9):
            self.assertEqual(len(self.sudoku.table[i]), 9)

    def test_non_empty_creation(self):
        for i in range(9):
            self.assertNotEqual(self.sudoku.table, "xxxxxxxxx")

    def test_row_repeated(self):
        self.assertEqual(self.sudoku.check_reps_row(0, 5), False)

    def test_row_not_repeated(self):
        self.assertEqual(self.sudoku.check_reps_row(0, 1), True)

    def test_column_repeated(self):
        self.assertEqual(self.sudoku.check_reps_col(0, 5), False)

    def test_column_not_repeated(self):
        self.assertEqual(self.sudoku.check_reps_col(0, 1), True)

    def test_block_repeated(self):
        self.assertEqual(self.sudoku.check_reps_block(1, 1, 5), False)

    def test_block_not_repeated(self):
        self.assertEqual(self.sudoku.check_reps_block(0, 2, 1,), True)

    def test_overwrite_originals(self):
        self.assertEqual(self.sudoku.overwrite(0, 0,
                                               self.sudoku.position_originals()
                                               ), False)

    def test_overwrite_originals_positive(self):
        self.assertEqual(self.sudoku.overwrite(0, 2,
                                               self.sudoku.position_originals()
                                               ), True)

    def test_position_originals(self):
        self.assertEqual(self.sudoku.position_originals(),
                         ["00", "01", "04", "10", "13", "14", "15", "21", "22",
                          "27", "30", "34", "38", "40", "43", "45", "48", "50",
                          "54", "58", "61", "66", "67", "73", "74", "75", "78",
                          "84", "87", "88"])

    def test_check(self):
        self.assertEqual(self.sudoku.check(0, 2, 4), True)

    def test_check_repeated(self):
        self.assertEqual(self.sudoku.check(1, 1, 5), False)

    def test_written(self):
        self.sudoku.write(0, 2, 4, self.sudoku.position_originals())
        self.assertEqual(self.table, ["534x7xxxx", "6xx195xxx", "x98xxxx6x",
                                      "8xxx6xxx3", "4xx8x3xx1", "7xxx2xxx6",
                                      "x6xxxx28x", "xxx419xx5", "xxxx8xx79"])

    def test_game_not_over(self):
        over = self.sudoku.is_over()
        self.assertFalse(over)

    def test_game_over(self):
        table = ["533175384", "612195537", "298376369", "882668363",
                 "481863981", "717328356", "169836281", "916419925",
                 "816288179"]
        self.sudoku = Sudoku(table, 9)
        over = self.sudoku.is_over()
        self.assertTrue(over)

    def test_game_over_2(self):
        table = ["5331", "6121", "2983", "8826"]
        self.sudoku = Sudoku(table, 2)
        over = self.sudoku.is_over()
        self.assertTrue(over)


if __name__ == "__main__":
    unittest.main()

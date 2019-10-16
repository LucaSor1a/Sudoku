import unittest
from unittest.mock import patch, MagicMock
from Ingreso import UserInput


class TestIngreso(unittest.TestCase):

    def setUp(self):
        self.ui = UserInput()

    def test_number_bigger_9(self):
        self.assertEqual(self.ui.numberInput(10, 9), False)

    def test_number_smaller_1(self):
        self.assertEqual(self.ui.numberInput(0, 9), False)

    def test_number_in_range(self):
        self.assertEqual(self.ui.numberInput(5, 9), True)

    def test_number_bigger_4(self):
        self.assertEqual(self.ui.numberInput(5, 4), False)

    def test_number_smaller_1_2(self):
        self.assertEqual(self.ui.numberInput(0, 4), False)

    def test_number_in_range_2(self):
        self.assertEqual(self.ui.numberInput(3, 4), True)

    def test_position_9(self):
        self.assertEqual(self.ui.position(5, 6, 9), True)

    def test_position_4(self):
        self.assertEqual(self.ui.position(4, 2, 4), True)

    def test_bad_position_4(self):
        self.assertEqual(self.ui.position(5, 1, 4), False)

    def test_position_bad_row_bigger(self):
        self.assertEqual(self.ui.position(10, 6, 9), False)

    def test_position_bad_row_smaller(self):
        self.assertEqual(self.ui.position(0, 6, 9), False)

    def test_position_bad_column_bigger(self):
        self.assertEqual(self.ui.position(5, 11, 9), False)

    def test_position_bad_column_smaller(self):
        self.assertEqual(self.ui.position(5, 0, 9), False)

    def test_dimention_4(self):
        self.assertEqual(self.ui.dimention(4), True)

    def test_dimention_9(self):
        self.assertEqual(self.ui.dimention(4), True)

    def test_bad_dimention(self):
        self.assertEqual(self.ui.dimention(3), False)

    """
    def size(self):
        sizev = 0
        while not self.dimention(sizev):
            try:
                sizev = int(input("Ingrese la dimension del sudoku (4 o 9): "))
                if (self.dimention(sizev)):
                    return sizev
                print("Ingresaste un valor no permitido, intentalo de nuevo")
            except ValueError:
                print("Ingresaste un valor no permitido, intentalo de nuevo")
    """

    def test_algo_size(self):
        pass


if __name__ == '__main__':
    unittest.main()

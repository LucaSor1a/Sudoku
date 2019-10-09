import unittest
from Ingreso import UserInput


class TestLetterCounter(unittest.TestCase):

    def setUp(self):
        self.valor = UserInput()
        self.sizev = 9

    def test_number_bigger_9(self):
        self.assertEqual(self.valor.numberInput(10, 9), False)

    def test_number_smaller_1(self):
        self.assertEqual(self.valor.numberInput(0, 9), False)

    def test_number_in_range(self):
        self.assertEqual(self.valor.numberInput(5, 9), True)

    def test_position(self):
        self.assertEqual(self.valor.position(5, 6, 9), True)

    def test_position_wrong_row(self):
        self.assertEqual(self.valor.position(10, 6, 9), False)

    def test_position_wrong_row_smaller(self):
        self.assertEqual(self.valor.position(0, 6, 9), False)

    def test_position_wrong_column(self):
        self.assertEqual(self.valor.position(5, 11, 9), False)

    def test_position_wrong_column_samller(self):
        self.assertEqual(self.valor.position(5, 0, 9), False)


if __name__ == '__main__':
    unittest.main()

import unittest
from unittest.mock import patch, MagicMock
import unittest.mock
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

    def test_size_4(self):
        with patch("builtins.input", return_value=4):
            result = self.ui.size()
        self.assertEqual(result, 4)

    def test_size_9(self):
        with patch("builtins.input", return_value=9):
            result = self.ui.size()
            self.assertEqual(result, 9)

    def test_size_7(self):
        with self.assertRaises(ValueError) and patch("builtins.input",
                                                     return_value=7):
            self.ui.size()

    def test_size_a(self):
        with self.assertRaises(ValueError) and patch("builtins.input",
                                                     return_value="a"):
            self.ui.size()

    def test_getValues_9(self):
        mock = MagicMock()
        mock.side_effect = [1, 2, 3]
        with patch("builtins.input", new=mock):
            result = self.ui.getValues(9)
        self.assertEqual(result, [0, 1, 3])

    def test_getValues_a(self):
        mock = MagicMock()
        mock.side_effect = ["a", 2, 3]
        with self.assertRaises(ValueError) and patch("builtins.input",
                                                     new=mock):
            self.ui.size()

    def test_getValues_11(self):
        mock = MagicMock()
        mock.side_effect = [1, 2, 29]
        with self.assertRaises(ValueError) and patch("builtins.input",
                                                     new=mock):
            self.ui.size()


if __name__ == '__main__':
    unittest.main()

import unittest
from unittest.mock import patch, MagicMock
import unittest.mock
from Ingreso import UserInput
from API import API


class TestIngreso(unittest.TestCase):

    def setUp(self):
        self.ui = UserInput()

    def test_number_bigger_9(self):
        self.ui.sizev = 9
        self.assertEqual(self.ui.numberInput(10), False)

    def test_number_smaller_1(self):
        self.ui.sizev = 9
        self.assertEqual(self.ui.numberInput(0), False)

    def test_number_in_range(self):
        self.ui.sizev = 9
        self.assertEqual(self.ui.numberInput(5), True)

    def test_number_bigger_4(self):
        self.ui.sizev = 4
        self.assertEqual(self.ui.numberInput(5), False)

    def test_number_smaller_1_2(self):
        self.ui.sizev = 4
        self.assertEqual(self.ui.numberInput(0), False)

    def test_number_in_range_2(self):
        self.ui.sizev = 4
        self.assertEqual(self.ui.numberInput(3), True)

    def test_position_9(self):
        self.ui.sizev = 9
        self.assertEqual(self.ui.position(5, 6), True)

    def test_position_4(self):
        self.ui.sizev = 4
        self.assertEqual(self.ui.position(4, 2), True)

    def test_bad_position_4(self):
        self.ui.sizev = 4
        self.assertEqual(self.ui.position(5, 1), False)

    def test_position_bad_row_bigger(self):
        self.ui.sizev = 9
        self.assertEqual(self.ui.position(10, 6), False)

    def test_position_bad_row_smaller(self):
        self.ui.sizev = 9
        self.assertEqual(self.ui.position(0, 6), False)

    def test_position_bad_column_bigger(self):
        self.ui.sizev = 9
        self.assertEqual(self.ui.position(5, 11), False)

    def test_position_bad_column_smaller(self):
        self.ui.sizev = 9
        self.assertEqual(self.ui.position(5, 0), False)

    def test_dimention_4(self):
        self.ui.sizev = 4
        self.assertEqual(self.ui.dimention(), True)

    def test_dimention_9(self):
        self.ui.sizev = 9
        self.assertEqual(self.ui.dimention(), True)

    def test_bad_dimention(self):
        self.ui.sizev = 3
        self.assertEqual(self.ui.dimention(), False)

    def test_size_4(self):
        with patch("builtins.input", return_value=4):
            self.ui.size()
        self.assertEqual(self.ui.sizev, 4)

    def test_size_9(self):
        with patch("builtins.input", return_value=9):
            self.ui.size()
            self.assertEqual(self.ui.sizev, 9)

    def test_size_7(self):
        with patch("builtins.input", return_value=7):
            self.ui.size()
            patch("buitins.print", return_value="Ingresaste un valor no " +
                  "permitido, intentalo de nuevo")

    def test_size_a(self):
        with patch("builtins.input", return_value="a"):
            self.ui.size()
            patch("buitins.print", return_value="Ingresaste un valor no " +
                  "permitido, intentalo de nuevo")

    def test_getValues_9(self):
        self.ui.sizev = 9
        mock = MagicMock()
        mock.side_effect = [1, 2, 3]
        with patch("builtins.input", new=mock):
            result = self.ui.getValues()
        self.assertEqual(result, [0, 1, 3])

    def test_getValues_a(self):
        self.ui.sizev = 9
        mock = MagicMock()
        mock.side_effect = ["a", 1, 5]
        with patch("builtins.input", new=mock):
            self.ui.size()
            patch("buitins.print", return_value="Ingresaste un valor no " +
                  "permitido, intentalo de nuevo")

    def test_getValues_11(self):
        self.ui.sizev = 9
        mock = MagicMock()
        mock.side_effect = [5, 1, 11]
        with patch("builtins.input", new=mock):
            self.ui.size()
            patch("buitins.print", return_value="Ingresaste un valor no " +
                  "permitido, intentalo de nuevo")

    def test_run(self):
        mock = MagicMock()
        mock.side_effect = [4, 3, 2, 1, 1, 2, 1]
        with patch("builtins.input", new=mock):
            mock_response = MagicMock()
            mock_response.json = MagicMock(return_value={"response": True,
                                                         "size": "4", "squar" +
                                                         "es":
                                                         [{"x": 0, "y": 0,
                                                          "value": 4},
                                                          {"x": 0, "y": 1,
                                                           "value": 2},
                                                          {"x": 0, "y": 2,
                                                           "value": 3},
                                                          {"x": 0, "y": 3,
                                                           "value": 1},
                                                          {"x": 1, "y": 1,
                                                           "value": 3},
                                                          {"x": 1, "y": 2,
                                                           "value": 2},
                                                          {"x": 1, "y": 3,
                                                           "value": 4},
                                                          {"x": 2, "y": 0,
                                                           "value": 3},
                                                          {"x": 2, "y": 1,
                                                           "value": 1},
                                                          {"x": 2, "y": 2,
                                                           "value": 4},
                                                          {"x": 2, "y": 3,
                                                           "value": 2},
                                                          {"x": 3, "y": 0,
                                                           "value": 2},
                                                          {"x": 3, "y": 1,
                                                           "value": 4},
                                                          {"x": 3, "y": 2,
                                                           "value": 1},
                                                          {"x": 3, "y": 3,
                                                           "value": 3}]})
            with patch("API.requests.get", return_value=mock_response):
                API(4).Table()
                fin = self.ui.run()
        self.assertEqual(fin, '\n     1  2   3  4   \n' +
                              '   ------------\n' +
                              '1  | 4  1 | 3  2 \n' +
                              '2  | 2  3 | 1  4 \n' +
                              '   ------------\n' +
                              '3  | 3  2 | 4  1 \n' +
                              '4  | 1  4 | 2  3 \n')


if __name__ == '__main__':
    unittest.main()

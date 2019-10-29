import unittest
import io
from parameterized import parameterized
from unittest.mock import patch, MagicMock, call
from Ingreso import UserInput


class TestIngreso(unittest.TestCase):

    def setUp(self):
        self.ui = UserInput()

    @parameterized.expand([
        # Test en rango
        (9, 5),
        (4, 3)
    ])
    def test_number_ok(self, size, value):
        self.ui.sizev = size
        self.assertEqual(self.ui.numberInput(value), True)

    @parameterized.expand([
        # Test mas grande
        (9, 10),
        (4, 5),
        # Test mas pequeño
        (9, 0),
        (4, 0),
    ])
    def test_number_bad(self, size, value):
        self.ui.sizev = size
        self.assertEqual(self.ui.numberInput(value), False)

    @parameterized.expand([
        # Test posicion en rango
        (9, 2, 9),
        (4, 4, 2),
    ])
    def test_position_ok(self, size, row, column):
        self.ui.sizev = size
        self.assertEqual(self.ui.position(row, column), True)

    @parameterized.expand([
        # Test fila mas grande
        (9, 10, 6),
        (4, 5, 1),
        # Test fila mas pequeña
        (9, 0, 6),
        (4, -1, 1),
        # Test columna mas grande
        (9, 5, 11),
        (4, 3, 6),
        # Test columna mas pequeña
        (9, 5, 0),
        (4, 3, 0)
    ])
    def test_position_bad(self, size, row, column):
        self.ui.sizev = size
        self.assertEqual(self.ui.position(row, column), False)

    @parameterized.expand([
        (4, ),
        (9, )
    ])
    def test_dimention_ok(self, size):
        self.ui.sizev = size
        self.assertEqual(self.ui.dimention(), True)

    @parameterized.expand([
        (7, ),
        (3, )
    ])
    def test_dimention_bad(self, size):
        self.ui.sizev = size
        self.assertEqual(self.ui.dimention(), False)

    @parameterized.expand([
        # Test entradas validas
        (4, ),
        (9, )
    ])
    def test_size(self, number):
        with patch("builtins.input", return_value=number):
            self.ui.size()
        self.assertEqual(self.ui.sizev, number)

    @parameterized.expand([
        # Test entradas NO validas
        ([2, 4], 4),
        (["a", 4], 4)
    ])
    @patch('builtins.print')
    def test_size_not_valid(self, numbers, expected, mocked_print):
        mock = MagicMock()
        mock.side_effect = numbers
        with patch("builtins.input", new=mock):
            self.ui.size()
            assert mocked_print.mock_calls == [call('Ingresaste un valor no pe'
                                                    'rmitido, intentalo de nue'
                                                    'vo')]
        self.assertEqual(self.ui.sizev, expected)

    @parameterized.expand([
        # Test entradas validas
        (4, [2, 3, 2], [1, 2, 2]),
        (9, [1, 2, 3], [0, 1, 3])
    ])
    def test_getValues(self, size, numbers, expected):
        self.ui.sizev = size
        mock = MagicMock()
        mock.side_effect = numbers
        with patch("builtins.input", new=mock):
            result = self.ui.getValues()
        self.assertEqual(result, expected)

    @parameterized.expand([
        # Test entradas NO validas
        (9, ["a", 2, 3, 1], [1, 2, 1]),
        (9, [1, 11, 1, 1, 2, 3], [0, 1, 3])
    ])
    @patch('builtins.print')
    def test_getValues_not_valid(self, size, numbers, expected, mocked_print):
        self.ui.sizev = size
        mock = MagicMock()
        mock.side_effect = numbers
        with patch("builtins.input", new=mock):
            result = self.ui.getValues()
            assert mocked_print.mock_calls == [call('Ingresaste un valor no pe'
                                                    'rmitido, intentalo de nue'
                                                    'vo')]
        self.assertEqual(result, expected)

    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    def test_run(self, mocked_print):
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
                self.ui.run()
            self.assertEqual(mocked_print.getvalue(),
                             '\n     1  2   3  4   \n'
                             '   ------------\n'
                             '1  | 4  x | 3  2 \n'
                             '2  | 2  3 | 1  4 \n'
                             '   ------------\n'
                             '3  | 3  2 | 4  1 \n'
                             '4  | 1  4 | 2  3 \n'
                             '\nPerdon, no se puede escribir en esa posicion\n'
                             '\n     1  2   3  4   \n'
                             '   ------------\n'
                             '1  | 4  x | 3  2 \n'
                             '2  | 2  3 | 1  4 \n'
                             '   ------------\n'
                             '3  | 3  2 | 4  1 \n'
                             '4  | 1  4 | 2  3 \n'
                             '\n\n\nFelicitaciones!!!!\n'
                             'Terminaste el juego de Sudoku\n\n\n'
                             '\n     1  2   3  4   \n'
                             '   ------------\n'
                             '1  | 4  1 | 3  2 \n'
                             '2  | 2  3 | 1  4 \n'
                             '   ------------\n'
                             '3  | 3  2 | 4  1 \n'
                             '4  | 1  4 | 2  3 \n\n'
                             )


if __name__ == '__main__':
    unittest.main()

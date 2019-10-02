import unittest
from Ingreso import UserInput

valor = UserInput()

class TestLetterCounter(unittest.TestCase):
    
    def test_number_bigger_9(self):
        self.assertEqual(valor.numberInput(10), False)
    
    def test_number_smaller_1(self):
        self.assertEqual(valor.numberInput(0), False)
    
    def test_number_in_range(self):
        self.assertEqual(valor.numberInput(5), True)
    
    def test_position(self):
        self.assertEqual(valor.position(5,6), True)
    
    def test_position_wrong_row(self):
        self.assertEqual(valor.position(10,6), False)
    
    def test_position_wrong_row_smaller(self):
        self.assertEqual(valor.position(0,6), False)
    
    def test_position_wrong_column(self):
        self.assertEqual(valor.position(5,11), False)
    
    def test_position_wrong_column_samller(self):
        self.assertEqual(valor.position(5,0), False)

if __name__ == '__main__':
    unittest.main()
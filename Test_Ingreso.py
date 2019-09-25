import unittest
from Ingreso import UserInput

valor = UserInput()

class TestLetterCounter(unittest.TestCase):
    
    def test_numero_ingresado_mayor_9(self):
        self.assertEqual(valor.numberInput(10), False)
    
    def test_numero_ingresado_menor_1(self):
        self.assertEqual(valor.numberInput(0), False)
    
    def test_numero_ingresado_en_rango(self):
        self.assertEqual(valor.numberInput(5), True)
    
    def test_posicion(self):
        self.assertEqual(valor.position(5,6), True)
    
    def test_posicion_fila_mal(self):
        self.assertEqual(valor.position(10,6), False)
    
    def test_posicion_fila_mal_menor(self):
        self.assertEqual(valor.position(0,6), False)
    
    def test_posicion_columna_mal(self):
        self.assertEqual(valor.position(5,11), False)
    
    def test_posicion_columna_mal_menor(self):
        self.assertEqual(valor.position(5,0), False)

if __name__ == '__main__':
    unittest.main()
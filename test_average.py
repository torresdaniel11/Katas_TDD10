from unittest import TestCase
from average import Average

class TestAverage(TestCase):
    def test_arrayNumbers_elementos_vacio(self):
        self.assertEqual(Average().arrayNumbers(""), 0 , "Elementos cadena vacia")

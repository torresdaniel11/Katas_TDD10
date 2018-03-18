from unittest import TestCase
from average import Average

class TestAverage(TestCase):
    def test_arrayNumbers_elementos_vacio(self):
        self.assertEqual(Average().arrayNumbers(""), 0 , "Elementos cadena vacia")

    def test_arrayNumbers_elementos_1(self):
        self.assertEqual(Average().arrayNumbers("3"), 1 , "Elementos cadena 1")

    def test_arrayNumbers_elementos_2(self):
        self.assertEqual(Average().arrayNumbers("233, 232"), 2 , "Elementos cadena 2")

    def test_arrayNumbers_elementos_n(self):
        self.assertEqual(Average().arrayNumbers("233, 232,23,23,2,2,2,432, 466,6"), 10 , "Elementos cadena n")

from unittest import TestCase
from average import Average

class TestAverage(TestCase):
    def test_arrayNumbers_elementos_vacio(self):
        self.assertEqual(Average().arrayNumbers("")[0], 0, "Elementos cadena vacia")

    def test_arrayNumbers_elementos_1(self):
        self.assertEqual(Average().arrayNumbers("32")[0], 1, "Elementos cadena 1")

    def test_arrayNumbers_elementos_2(self):
        self.assertEqual(Average().arrayNumbers("233, 232")[0], 2, "Elementos cadena 2")

    def test_arrayNumbers_elementos_n(self):
        self.assertEqual(Average().arrayNumbers("233, 232,23,23,2,2,2,432, 466,6")[0], 10, "Elementos cadena n")

    def test_arrayNumbers_min_vacio(self):
        self.assertEqual(Average().arrayNumbers("")[1], None, "Minimo cadena vacia")

    def test_arrayNumbers_min_1(self):
        self.assertEqual(Average().arrayNumbers("32")[1], 32, "Minimo cadena 1")

    def test_arrayNumbers_min_2(self):
        self.assertEqual(Average().arrayNumbers("1, 434")[1], 1, "Minimo cadena 2")

    def test_arrayNumbers_min_n(self):
        self.assertEqual(Average().arrayNumbers("1, 434,32,32,32,32,3,4")[1], 1, "Minimo cadena n")

    def test_arrayNumbers_max_vacio(self):
        self.assertEqual(Average().arrayNumbers("")[2], None, "Maximo cadena vacia")

    def test_arrayNumbers_max_1(self):
        self.assertEqual(Average().arrayNumbers("3")[2], 3, "Maximo cadena 1")

    def test_arrayNumbers_max_2(self):
        self.assertEqual(Average().arrayNumbers("3, 323")[2], 323, "Maximo cadena 2")

    def test_arrayNumbers_max_n(self):
        self.assertEqual(Average().arrayNumbers("3, 323, 232,2 ,2,2,3 ,4")[2], 323, "Maximo cadena n")

    def test_arrayNumbers_average_vacio(self):
        self.assertEqual(Average().arrayNumbers("")[3], None, "Promedio cadena vacia")

    def test_arrayNumbers_average_1(self):
        self.assertEqual(Average().arrayNumbers("3")[3], 3, "Promedio cadena 1")

    def test_arrayNumbers_average_2(self):
        self.assertEqual(Average().arrayNumbers("3, 9")[3], 6, "Promedio cadena 2")

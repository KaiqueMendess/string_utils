import unittest
from string_utils import inverter_string, contar_vogais

class TestStringUtils(unittest.TestCase):

    def test_inverter_string(self):
        self.assertEqual(inverter_string("hello"), "olleh")
        self.assertEqual(inverter_string("Python"), "nohtyP")

    def test_contar_vogais(self):
        self.assertEqual(contar_vogais("hello"), 2)
        self.assertEqual(contar_vogais("Python"), 1)
        self.assertEqual(contar_vogais(""), 0)

if __name__ == '__main__':
    unittest.main()
import unittest
from bosses import Vito_ganyada

class VitoGanyadaTesting(unittest.TestCase):
    
    def test_decrement(self):
        vito = Vito_ganyada()
        vito.decrement(100)
        result = vito.score
        self.assertEqual(result, 400)

    def test_increment(self):
        vito = Vito_ganyada()
        vito.increment(100)
        result = vito.score
        self.assertEqual(result, 600)


if __name__ == '__main__':
    unittest.main()
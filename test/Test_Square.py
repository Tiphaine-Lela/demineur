import unittest
import source
from source.Square import Square

# pour le faire tourner, utiliser : python -m unittest test.Test_Square
# pour executer tous les fichiers de test, utiliser :
# python -m unittest discover
# ou
# python -m unittest


class TestSquare(unittest.TestCase):

    square = Square()

    def test_set_position(self):
        self.square.set_position(1, 1)
        tuple_to_test = (1, 1)
        self.assertEqual(self.square.get_position(), tuple_to_test, "Should be (1, 1)")

    def test_set_mine(self):
        self.assertEqual(self.square.get_mine(), False, "Should be False")
        self.square.set_mine(True)
        self.assertEqual(self.square.get_mine(), True, "Should be True")

    def test_dig(self):
        self.assertEqual(self.square.get_unveiled(), False)
        self.square.dig_square()
        self.assertEqual(self.square.get_unveiled(), True)

    def test_display(self):
        s1 = Square()
        self.assertEqual(s1.display(), ".", "Problems with hidden square")
        s1.set_mine(True)
        s1.dig_square()
        self.assertEqual(s1.display(), "*", "Problems with explosion")
        s1.set_mine(False)
        s1.increase_mines_neighbors()
        s1.increase_mines_neighbors()
        self.assertEqual(s1.display(), "2", "Problems with unveiledn square, no mines")


if __name__ == '__main__':
    unittest.main()

import unittest
from source.Board import Board

# pour le faire tourner utiliser : python -m unittest test.Test_Board


class MyTestCase(unittest.TestCase):

    board = Board(3, 3, 9)

    def test_get_neighbors(self):
        poss_1 = [(0, 1), (1, 1), (1, 0)]
        self.assertEqual(set(self.board.get_neighbors((0, 0))), set(poss_1))
        poss_2 = [(0, 0), (0, 1), (1, 1), (2, 1), (2, 0)]
        self.assertEqual(set(self.board.get_neighbors((1, 0))), set(poss_2))
        poss_3 = [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 1), (2, 0), (1, 0)]
        self.assertEqual(set(self.board.get_neighbors((1, 1))), set(poss_3))

    def test_pos_mines(self):
        mines = self.board.pos_mines()
        self.assertEqual(len(mines), self.board.nb_mines, "the number of created mines isn't the asked number")
        set_mines = set(mines)
        self.assertEqual(len(mines), len(set_mines), "At least one mine is duplicated")

    # pas terrible, le test...
    def test_build_board(self):
        # compter si le nombre de mines est le bon
        real_nb_mines = 0
        for i in range(self.board.dim_x):
            for j in range(self.board.dim_y):
                if self.board.board[i][j].get_mine:
                    real_nb_mines += 1
        self.assertEqual(real_nb_mines, self.board.nb_mines, "the number of created mines isn't the asked number")

    def test_dig(self):
        b1 = Board(3, 3, 0)
        b1.board[0][0].set_mine(True)
        self.assertFalse(b1.dig(0, 1))
        self.assertEqual(b1.dug_squares, 1, "the number of dug squares hasn't incremented")
        self.assertFalse(b1.dig(0, 1))
        self.assertTrue(b1.dig(0, 0), "The mine isn't exploding")
        # pas fait le test sur la derniere mine qui finit le jeu


if __name__ == '__main__':
    unittest.main()

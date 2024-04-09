import unittest
from unittest.mock import patch
from tic_tac_bug_toe_solution import is_win,main, board

class MyTestCase(unittest.TestCase):
    def test_board_creation(self):
        """Test if the board is initialized correctly."""
        expected_board = [[' ', ' ', ' '],
                          [' ', ' ', ' '],
                          [' ', ' ', ' ']]
        self.assertEqual(board, expected_board)

    def test_player_has_won(self):
        """Test if a player has won, when win condition is met"""
        board = [['X', 'O', 'X'],
                 ['O', 'O', 'X'],
                 ['X', 'O', 'O']]
        self.assertTrue(is_win(board,'O'))

    def test_no_win(self):
        board = [['X', 'O', 'X'],
                 ['X', 'O', 'O'],
                 ['O', 'X', 'O']]
        self.assertFalse(is_win(board,'X'))
        self.assertFalse(is_win(board,'O'))

if __name__ == '__main__':
    unittest.main()
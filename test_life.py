import unittest
import life
import random
from itertools import chain


class TestLife(unittest.TestCase):
    def setUp(self):
        self.board = life.create_dead_board(3, 3)

    def initialise_neighbours(self, board, neighbours):
        locations = random.sample(list(chain(range(4), range(5, 9))), neighbours)
        for pos in locations:
            board[pos//3][pos % 3] = 1
        return board

    def test_create_dead_board(self):
        result = life.create_dead_board(3, 3)
        expected = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.assertEqual(result, expected)

    def test_8_dead_neighbours(self):
        """
        // depopulation, 8 dead neighbours
        xxx      xxx
        xxx   -> xxx
        xxx      xxx
        """
        print('========= Test 8 dead neighbours ==========')
        self.board = self.initialise_neighbours(self.board, 0)
        next_board = life.calculate_next_board_state(self.board)
        self.assertEqual(0, next_board[1][1],
                         "Cell should stay dead when it has 8 dead neighbours\n{} => {}"
                         .format(self.board, next_board))

        self.board[1][1] = 1
        next_board = life.calculate_next_board_state(self.board)
        self.assertEqual(0, next_board[1][1],
                         "Cell should die when it has 8 dead neighbours\n {} => {}"
                         .format(self.board, next_board))

    def test_7_dead_neighbours(self):
        """
        // depopulation, 7 dead neighbours
        oxx      oxx
        xxx   -> xxx
        xxx      xxx
        """
        print('========= Test 7 dead neighbours ==========')
        self.board = self.initialise_neighbours(self.board, 1)
        next_board = life.calculate_next_board_state(self.board)
        self.assertEqual(0, next_board[1][1],
                         "Cell should stay dead when it has 7 dead neighbours\n{} => {}"
                         .format(self.board, next_board))

        self.board[1][1] = 1
        next_board = life.calculate_next_board_state(self.board)
        self.assertEqual(0, next_board[1][1],
                         "Cell should die when it has 7 dead neighbours\n {} => {}"
                         .format(self.board, next_board))

    def test_6_dead_neighbours(self):
        """
        // Just right, 6 dead neighbours
        oxx      oxx
        oox   -> oox
        xxx      xxx
        """
        print('========= Test 6 dead neighbours ==========')
        self.board = self.initialise_neighbours(self.board, 2)
        next_board = life.calculate_next_board_state(self.board)
        self.assertEqual(0, next_board[1][1],
                         "Cell should stay dead when it has 6 dead neighbours\n{} => {}"
                         .format(self.board, next_board))

        self.board[1][1] = 1
        next_board = life.calculate_next_board_state(self.board)
        self.assertEqual(1, next_board[1][1],
                         "Cell should stay alive when it has 6 dead neighbours\n {} => {}"
                         .format(self.board, next_board))

    def test_5_dead_neighbours(self):
        """
        // Reproduction, 5 dead neighbours
        oxx      oxx
        oxx   -> oox
        oxx      oxx
        """
        print('========= Test 5 dead neighbours ==========')
        self.board = self.initialise_neighbours(self.board, 3)
        next_board = life.calculate_next_board_state(self.board)
        self.assertEqual(1, next_board[1][1],
                         "Cell reproduces and becomes alive when it has 5 dead neighbours\n{} => {}"
                         .format(self.board, next_board))
        self.board[1][1] = 1
        next_board = life.calculate_next_board_state(self.board)
        self.assertEqual(1, next_board[1][1],
                         "Cell stays alive when it has 5 dead neighbours\n {} => {}"
                         .format(self.board, next_board))

    def test_4_dead_neighbours(self):
        """
        // overpopulation, 4 dead neighbours
        ooo      ooo
        xox   -> xxx
        oxx      oxx
        """
        print('========= Test 4 dead neighbours ==========')
        self.board = self.initialise_neighbours(self.board, 4)
        next_board = life.calculate_next_board_state(self.board)
        self.assertEqual(0, next_board[1][1],
                         "Cell should stay dead when it has 4 dead neighbours\n{} => {}"
                         .format(self.board, next_board))

        self.board[1][1] = 1
        next_board = life.calculate_next_board_state(self.board)
        self.assertEqual(0, next_board[1][1],
                         "Cell should die when it has 4 dead neighbours\n {} => {}"
                         .format(self.board, next_board))

    def test_3_dead_neighbours(self):
        """
        // overpopulation, 3 dead neighbours
        ooo      ooo
        xoo   -> xxo
        oxx      oxx
        """
        print('========= Test 3 dead neighbours ==========')
        self.board = self.initialise_neighbours(self.board, 5)
        next_board = life.calculate_next_board_state(self.board)
        self.assertEqual(0, next_board[1][1],
                         "Cell should stay dead when it has 3 dead neighbours\n{} => {}"
                         .format(self.board, next_board))

        self.board[1][1] = 1
        next_board = life.calculate_next_board_state(self.board)
        self.assertEqual(0, next_board[1][1],
                         "Cell should die when it has 3 dead neighbours\n {} => {}"
                         .format(self.board, next_board))

    def test_2_dead_neighbours(self):
        """
        // overpopulation, 2 dead neighbours
        ooo      ooo
        xoo   -> xxo
        oxo      oxo
        """
        print('========= Test 2 dead neighbours ==========')
        self.board = self.initialise_neighbours(self.board, 6)
        next_board = life.calculate_next_board_state(self.board)
        self.assertEqual(0, next_board[1][1],
                         "Cell should stay dead when it has 2 dead neighbours\n{} => {}"
                         .format(self.board, next_board))

        self.board[1][1] = 1
        next_board = life.calculate_next_board_state(self.board)
        self.assertEqual(0, next_board[1][1],
                         "Cell should die when it has 2 dead neighbours\n {} => {}"
                         .format(self.board, next_board))

    def test_1_dead_neighbours(self):
        """
        // overpopulation, 1 dead neighbours
        ooo      ooo
        ooo   -> oxo
        oxo      oxo
        """
        print('========= Test 1 dead neighbours ==========')
        self.board = self.initialise_neighbours(self.board, 7)
        next_board = life.calculate_next_board_state(self.board)
        self.assertEqual(0, next_board[1][1],
                         "Cell should stay dead when it has 1 dead neighbours\n{} => {}"
                         .format(self.board, next_board))

        self.board[1][1] = 1
        next_board = life.calculate_next_board_state(self.board)
        self.assertEqual(0, next_board[1][1],
                         "Cell should die when it has 1 dead neighbours\n {} => {}"
                         .format(self.board, next_board))

    def test_0_dead_neighbours(self):
        """
        // overpopulation, 0 dead neighbours
        ooo      ooo
        ooo   -> oxo
        ooo      ooo
        """
        print('========= Test 0 dead neighbours ==========')
        self.board = self.initialise_neighbours(self.board, 8)
        next_board = life.calculate_next_board_state(self.board)
        self.assertEqual(0, next_board[1][1],
                         "Cell should stay dead when it has 0 dead neighbours\n{} => {}"
                         .format(self.board, next_board))

        self.board[1][1] = 1
        next_board = life.calculate_next_board_state(self.board)
        self.assertEqual(0, next_board[1][1],
                         "Cell should die when it has 0 dead neighbours\n {} => {}"
                         .format(self.board, next_board))


import unittest
from board import Board
from player import Player
from state import State
from Ai import AI
class Tests(unittest.TestCase):
    def setUp(self):
        self.player = Player("X")
        self.move=(1,1)
        self.anotherMove = (1,1)
        self.board = Board()
        self.board.initializeBoard(5)
        self.state = State()
        self.state.board = self.board 
        unittest.TestCase.setUp(self)

    def tearDown(self):
        del self.board
        del self.player
        del self.move
        del self.state
        unittest.TestCase.tearDown(self)
    #board
    def test_makeMove_OK(self):
        self.board.makeMove(self.move, self.player)
        self.assertEqual(self.board.get_position(self.move), self.player.piece)

    def test_isValidMove_validMove_True(self):
        self.assertTrue(self.board.isValidMove( self.move))

    def test_isValidMove_takenSpot_False(self):
        self.board.makeMove(self.move, self.player)
        self.assertFalse(self.board.isValidMove(self.move))

    def test_isValidMove_outsideBoard_False(self):
        self.assertFalse(self.board.isValidMove((-1,100)))
    
    #state
    def test_createNewState_validMove_True(self):
        newState = self.state.createNewState((2,2),self.player)
        self.state.board.makeMove((2,2),self.player)
        self.assertEqual(self.state.board, newState.board)


        



if __name__ == '__main__':
    unittest.main()

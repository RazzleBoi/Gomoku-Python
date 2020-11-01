import random

class Board(object):
    def __init__(self):
        '''
        board is a dictionary which represnts the current state of the board
        dimension is the size of the board
        '''
        self.board = {}
        self.dimension = None

    def get_position(self,coordinates):
        return self.board[coordinates]


    def initializeBoard(self, dimension):
        '''
        sets the size and fills the board 
        diictionary with "."
        '''
        self.dimension = dimension
        for row in range(dimension):
            for column in range(dimension):
                self.board[(row, column)] = '.'

    def __str__(self):
        '''
        printable state of the board
        '''
        printableBoard=""
        for row in range(self.dimension):
            for column in range(self.dimension):
                if (row, column) in self.board:
                    printableBoard+=self.board[(row, column)]+" "
                else:
                    board+="  "
            printableBoard+="\n"
        return printableBoard

    def makeMove(self, move, player):
        '''
        make the move
        '''
        if self.isValidMove(move):
            self.board[(move[0], move[1])] = player.piece
            return move
        else:
            return (-1, -1)

    def isValidMove(self, move):
        '''
        boolean function that checks if the move is on the
        board and that the spot is not already taken
        '''
        if move[0] >= 0 and move[0] < self.dimension  and move[1] >= 0 and move[1] < self.dimension:
            if self.board[(move[0], move[1])] == '.':
                return True
            else:
                return False
        return False



    def getValidMoves(self):
        '''
        gets the empty spots of the board
        and returns them as a list
        '''
        valid = []
        for row in range(self.dimension):
            for column in range(self.dimension):
                move = (row, column)
                if self.isValidMove(move):
                    valid.append(move)
        return valid

    def getCloseMoves(self):
        transitionMoves = []
        for row in range(self.dimension):
            for column in range(self.dimension):
                move = (row, column)
                if self.isValidMove((row, column)) == False:
                    move=(row-1,column)
                    if move not in transitionMoves and self.isValidMove(move):
                        transitionMoves.append(move)
                    move=(row-1,column-1)
                    if move not in transitionMoves and self.isValidMove(move):
                        transitionMoves.append(move)
                    move=(row-1,column+1)
                    if move not in transitionMoves and self.isValidMove(move):
                        transitionMoves.append(move)

                    move=(row,column-1)
                    if move not in transitionMoves and self.isValidMove(move):
                        transitionMoves.append(move)
                    move=(row,column+1)
                    if move not in transitionMoves and self.isValidMove(move):
                        transitionMoves.append(move)
                    move=(row+1,column-1)
                    if move not in transitionMoves and self.isValidMove(move):
                        transitionMoves.append(move)
                    move=(row+1,column)
                    if move not in transitionMoves and self.isValidMove(move):
                        transitionMoves.append(move)
                    move=(row+1,column+1)
                    if move not in transitionMoves and self.isValidMove(move):
                        transitionMoves.append(move)

        return transitionMoves

    def __eq__(self, other):
        if self.dimension != other.dimension:
            return False
        for row in range(self.dimension):
            for column in range(self.dimension):
                if self.board[(row,column)] != other.board[(row,column)]:
                    return False
        return True
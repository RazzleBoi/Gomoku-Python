import copy
from board import Board


class State(object):
    def __init__(self):
        self.move = (0, 0)
        self.board = Board()
        self.parent = None

    def createNewState(self, move, player):
        '''
        creates a new state by doing the given move
        in the state object
        '''
        new = State()
        new.board = copy.deepcopy(self.board)
        new.move = new.board.makeMove(move, player)

        if new.move == (-1, -1):
            return None
        return new

    def getValidTransitions(self, player):
        '''
        gets all the states possibly derrived from the current(self) state
        and all possible moves
        '''
        validMoves = self.board.getCloseMoves()
        transitionBoardStates = []
        for move in validMoves:
            new_state = self.createNewState(move, player)
            transitionBoardStates.append((move, new_state))

        return transitionBoardStates

    def isWinner(self, player, chain,lastMove):
        '''
        checks if the last player ho moved won
        a.k.a. made a chain of length 'chain'
        '''
        count = 0
        # North
        for row in reversed(range(self.move[0])):
            if self.board.board[(row, self.move[1])] == player.piece:
                count += 1
            else:
                break

        # South
        for row in range(self.move[0], self.board.dimension):
            if self.board.board[(row, self.move[1])] == player.piece:
                count += 1
            else:
                break

        if count == chain:
            return True

        count = 0
        # East
        for column in range(self.move[1], self.board.dimension):
            if self.board.board[(self.move[0], column)] == player.piece:
                count += 1
            else:
                break

        # West
        for column in reversed(range(self.move[1])):
            if self.board.board[(self.move[0], column)] == player.piece:
                count += 1
            else:
                break

        if count == chain:
            return True

        count = 0
        # North West
        for row, column in zip(reversed(range(self.move[0])),
                            reversed(range(self.move[1]))):
            if self.board.board[(row, column)] == player.piece:
                count += 1
            else:
                break

        # South East
        for row, column in zip(range(self.move[0], self.board.dimension),
                            range(self.move[1], self.board.dimension)):
            if self.board.board[(row, column)] == player.piece:
                count += 1
            else:
                break

        if count == chain:
            return True

        count = 0
        # North East
        for row, column in zip(reversed(range(self.move[0])),
                            range(self.move[1] + 1, self.board.dimension)):
            if self.board.board[(row, column)] == player.piece:
                count += 1
            else:
                break

        # South West
        for row, column in zip(range(self.move[0], self.board.dimension),
                            reversed(range(self.move[1] + 1))):
            if self.board.board[(row, column)] == player.piece:
                count += 1
            else:
                break

        if count == chain:
            return True

        return False

    def heuristic(self, chain, player, opponent):
        '''
        checks the current state of the board
        and computes a value which represents
        the favorability of the player 'player'
        '''
        current_chain_count = self.countChains(player)
        oponent_chain_count =self.countChains(opponent)

        if current_chain_count >= 10000:
            return 100000

        elif oponent_chain_count >= 10000:
            return -100000
        
        else:
            return current_chain_count-oponent_chain_count

    def counter(self, player, row, column, dir_x, dir_y):
        '''
        counts the number of player pieces that
        are consecutive in a certain direction
        '''
        count = 0
        while row >= 0 and row < self.board.dimension and column >= 0 and column < self.board.dimension:
            if self.board.board[(row, column)] == player.piece:
                count += 1
                row += dir_x
                column += dir_y
            else:
                break

        return count

    def countChains(self, player):
        '''
        gets the state of  chains
        made by th current player 
        chainScore = 0
        '''
        chainScore = 0
        #horizontal
        for row in range(self.board.dimension - 1):
            currentChain=0
            for column in range(self.board.dimension - 1):
                if self.board.board[(row,column)] == player.piece:
                    currentChain+=1
                elif currentChain >1:
                    chainScore += 10**(currentChain-1)
                    currentChain = 0
                else:
                    currentChain = 0
            if currentChain >1:
                chainScore += 10**(currentChain-1)
                currentChain = 0
        #vertical
        for column in range(self.board.dimension - 1):
            currentChain=0
            for row in range(self.board.dimension - 1):
                if self.board.board[(row,column)] == player.piece:
                    currentChain+=1
                elif currentChain >1:
                    chainScore += 10**(currentChain-1)
                    currentChain = 0
                else:
                    currentChain = 0
            if currentChain >1:
                chainScore += 10**(currentChain-1)
                currentChain = 0
        #main diagonal
        currentChain1=0
        currentChain2=0
        row = 0
        copyRow = row
        for column in range(self.board.dimension-1):
            if self.board.board[(column,column)] == player.piece:
                currentChain1+=1
            elif currentChain1 >1:
                chainScore += 10**(currentChain1-1)
               # print(chainScore)
                currentChain1 = 0
            else:
                currentChain1 = 0

        if currentChain1 >1:
            chainScore += 10**(currentChain1-1)
            currentChain1 = 0
        currentChain1=0
        for row in range(1,self.board.dimension - 1):
            currentChain1=0
            currentChain2=0
            copyRow = row
            for column in range(self.board.dimension - copyRow-1):
                if self.board.board[(row,column)] == player.piece:
                    currentChain1+=1
                elif currentChain1 >1:
                    chainScore += 10**(currentChain1-1)
                    currentChain1 = 0
                else:
                    currentChain1 = 0
                if self.board.board[(column,row)] == player.piece:
                    currentChain2+=1
                elif currentChain2 >1:
                    chainScore += 10**(currentChain2-1)
                    currentChain2 = 0
                else:
                    currentChain2 = 0
                row+=1
            if currentChain1 >1:
                chainScore += 10**(currentChain1-1)
                currentChain1 = 0
            if currentChain2 >1:
                chainScore += 10**(currentChain2-1)
                currentChain2 = 0
            row = copyRow

        #secondary diagonal
        currentChain1=0
        currentChain2=0
        row = 0
        copyRow = row
        for column in range(self.board.dimension-1,0,-1):
            if self.board.board[(row,column)] == player.piece:
                currentChain1+=1
            elif currentChain1 >1:
                chainScore += 10**(currentChain1-1)
                currentChain1 = 0
            else:
                currentChain1 = 0
            row+=1
        if currentChain1 >1:
            chainScore += 10**(currentChain1-1)
            currentChain1 = 0

        currentChain1=0
        currentChain2=0
        for row in range(self.board.dimension - 1):
            currentChain1=0
            currentChain2=0
            copyRow = row
            for column in range(self.board.dimension-1,copyRow,-1):
                if self.board.board[(row,column)] == player.piece:
                    currentChain1+=1
                elif currentChain1 >1:
                    chainScore += 10**(currentChain1-1)
                    currentChain1 = 0
                else:
                    currentChain1 = 0
                if self.board.board[(14-column,14-row)] == player.piece:
                    currentChain2+=1
                elif currentChain2 >1:
                    chainScore += 10**(currentChain2-1)
                    currentChain2 = 0
                else:
                    currentChain2 = 0
                row+=1
            if currentChain1 >1:
                chainScore += 10**(currentChain1-1)
                currentChain1 = 0
            if currentChain2 >1:
                chainScore += 10**(currentChain2-1)
                currentChain2 = 0
            row = copyRow

        return chainScore

 
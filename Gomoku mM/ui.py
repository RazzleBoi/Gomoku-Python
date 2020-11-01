from errors import *
from state import *
from player import *
from Ai import AI


class Console(object):
    def __init__(self, dimension=0, chain=0):
        self.state = State()
        self.dimension = dimension
        self.chain = chain
        self.initial = None
        self.current = None
        self.oponent = None
        self.player_x = Player('X')
        self.player_o = Player('O')
        self.max_depth = 3
        self.Aiplayer = AI(self.state,self.chain)


    def displayMenu(self):
        print("------------------------------------------")
        print("             Welcome to Gomoku            ")
        print("------------------------------------------")
        print("Modes:                                    ")
        print(" 1. Human vs. Human                       ")
        print(" 2. Human vs. AI                          ")
        print("------------------------------------------")


    def start(self,mode):
        self.state.board.initializeBoard(self.dimension)
        if mode == 1:
            self.manualGame()
        elif mode == 2:
            self.AiGame()

    def swapTurn(self, player):
        if player == self.player_x:
            self.current = self.player_o
            self.oponent = self.player_x
            return self.player_o
        else:
            self.current = self.player_x
            self.oponent = self.player_o
            return self.player_x

    def swapInitial(self, player):
        if player == self.player_x:
            return self.player_o
        else:
            return self.player_x

    def getMove(self, player):
        print("Player %s's Turn" % player.piece)
        inputString=input("Move :")
        inputString=inputString.split()
        if len(inputString) !=2:
            raise UiError("There must be exactly 2 values!")
        elif not inputString[0].isdecimal() or not inputString[1].isdecimal():
            raise UiError("The 2 values ,ust be integers!")
        return [int(inputString[0]),int(inputString[1])]



    def manualGame(self):
        print("Start:                                    ")
        print(" 1. Human (X)                             ")
        print(" 2. Human (O)                             ")
        while True:
            
            inputString = input("Choose Starting Player: ")
            if inputString == "1":
                self.current = self.player_x
                self.oponent = self.player_o
                break
            elif inputString == "2":
                self.current = self.player_o
                self.oponent = self.player_x
                break
            else:
                print("Please introduce 1 or 2!")


        print("------------------------------------------")
        print("               Start Board                ")
        print("------------------------------------------")

        while self.isOver() is not True:
            print(self.state.board)
            print("------------------------------------------")
            while True:
                try:
                    move = self.getMove(self.current)
                    if self.state.board.isValidMove(move) == False:
                        print("Invalid move!")
                    else:
                        break
                except UiError as ue:
                    print(ue)
 
            self.state = self.state.createNewState(move, self.current)
            if self.state.isWinner(self.current, self.chain, move) is True:
                self.printWinMessage()
                return 0
            self.current = self.swapTurn(self.current)

        self.printGameEnded()
        print(self.state.board)
        print("------------------------------------------")
        print("                 Tie                      ")
        print("------------------------------------------")

    
    def printWinMessage(self):
        print("------------------------------------------")
        print(self.state.board)
        print("------------------------------------------")
        print("            Player %s Wins                " % self.current.piece)
        print("------------------------------------------")

    def printGameEnded(self):
        print("------------------------------------------")
        print("              Game Ended                  ")
        print("------------------------------------------")

    def isOver(self):
        return not self.state.board.getValidMoves()
    
###########################################################################################################################################
###########################################################################################################################################


    def AiGame(self):
        print("Start:                                    ")
        print(" 1. Human (X)                             ")
        print(" 2. Aiplayer (O)                          ")
        self.current = self.player_x
        self.oponent = self.player_o
        while self.isOver() is not True:
            print(self.state.board)
            print("------------------------------------------")
            if self.current.piece == "X":
                while True:
                    try:
                        move = self.getMove(self.current)
                        if self.state.board.isValidMove(move) == False:
                            print("Invalid move!")
                        else:
                            break
                    except UiError as ue:
                        print(ue)
            else:
                self.Aiplayer = AI(self.state,self.chain)
                move = self.Aiplayer.alphaBetaSearch(self.current,3)
                move = move[1]
            self.state = self.state.createNewState(move, self.current)
            if self.state.isWinner(self.current, self.chain, move) is True:
                self.printWinMessage()
                return 0
            self.current = self.swapTurn(self.current)

        self.printGameEnded()
        print(self.state.board)
        print("------------------------------------------")
        print("                 Tie                      ")
        print("------------------------------------------")


    def run(self):
        while True:
            inputString = input("Press 1 to switch interface:")
            if inputString == "1":
                break
            self.dimension = 15
            self.chain = 5
            self.state.board.initializeBoard(self.dimension)
            self.Aiplayer = AI(self.state,self.chain)
            while True:
                self.displayMenu()
                inputString = input("Choose :")
                if inputString == "1":
                    self.manualGame()
                elif inputString == "2":
                    self.AiGame()
                elif inputString == "3":
                    break
                else:
                    print("Invalid command!")


from player import Player
class AI(object):

    def __init__(self,state,chain):
        self.state = state
        self.chain = chain
        self.player_x = Player('X')
        self.player_o = Player('O')
        self.minimax_moves = []

    def swap(self, player):
        '''
        swaps the current and
        opponent players values
        '''
        if player == self.player_x:
            return self.player_o
        else:
            return self.player_x


    def alphaBetaSearch(self, player, depth):
        '''
        minMax algorithm with alpha beta proning strategy
        '''

        alpha = float('-inf')
        beta = float('inf')

        utility = self.maxValue(self.state, player,
                                alpha, beta, depth-1,None)
        print(utility[1])
        return utility

    def maxValue(self, state, player, alpha, beta, depth,lastMove):
        '''
        returns the best available move and its heuristic for the
        'current' player at a given state
        '''
        if depth == 0 or self.state.isWinner(player,self.chain,lastMove) or self.state.isWinner(self.swap(player),self.chain,lastMove):
            return [state.heuristic(self.chain, self.player_o, self.player_x),None]
        else:
            validTransitionBoards = state.getValidTransitions(player)
            utility = [float('-inf'),None]
            for move, state in validTransitionBoards:
                intermidiaryEuristicValue = self.minValue(state, self.swap(player), alpha, beta, depth-1,move)
                if utility[0] < intermidiaryEuristicValue[0]:
                    utility[0] = intermidiaryEuristicValue[0]
                    utility[1] = move
                
                alpha = max(alpha, utility[0])
                if alpha >= beta:
                    break
            return utility

    def minValue(self, state, player, alpha, beta, depth,lastMove):
        '''
        returns the best available move and its heuristic for the
        'opponent' player at a given state
        '''
        if depth == 0 or self.state.isWinner(player,self.chain,lastMove) or self.state.isWinner(self.swap(player),self.chain,lastMove):
            return [state.heuristic(self.chain, self.player_o, self.player_x),None]
        else:
            validTransitionBoards = state.getValidTransitions(player)     
            utility = [float('inf'),None]
            for move, state in validTransitionBoards:
                intermidiaryEuristicValue = self.maxValue(state, self.swap(player), alpha, beta, depth-1,move)
                
                if utility[0] > intermidiaryEuristicValue[0]:
                    utility[0] = intermidiaryEuristicValue[0]
                    utility[1] = move
               
                beta = min(beta, utility[0])
                if beta <= alpha:
                    break
            return utility

    

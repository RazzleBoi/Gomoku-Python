from state import *


class Player(object):
    def __init__(self, piece):
        '''
        piece is X or O 
        '''
        self.piece = piece
           
    def __str__(self):
        return "Player " + self.piece

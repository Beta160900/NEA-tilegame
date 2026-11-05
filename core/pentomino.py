from core.board import board
class pentomino_game:
    def __init__(self):
        self.__board = board(6,10)
    def get_board(self):
        return self.__board    
class board:
    def __init__(self, rows, cols):
        self.__arr = [[0]*cols for _ in range(rows)]
    def change(self, row, col, value):
        self.__arr[row][col] = value


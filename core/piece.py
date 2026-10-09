#tile is a shape+position
class tile:
    def __init__(self, row, col, shape, cells):
        self.row = row
        self.col = col
        self.shape = tile.normalize(cells) 

    @classmethod
    def normalize(cls, cells):
        min_row = min(cell[0] for cell in cells)
        min_col = min(cell[1] for cell in cells)
        return [(cell[0] - min_row, cell[1] - min_col) for cell in cells]
    
    def move(self, new_row, new_col):
        self.row = new_row
        self.col = new_col

    #rotation matrix: [[0, -1], [1, 0]] (90 degrees clockwise)
    def rotate(self):
        self.shape = [(col, -row) for row, col in self.shape]
        self.shape = tile.normalize(self.shape)
        
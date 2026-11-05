class piece:
    def __init__(self, shape, color, piece_id):
        self.__id = piece_id
        self.__color = color
        self.__list = shape # y = [(0,0),(0,1),(0,2),(0,3),(1,1)]

    def get_id(self):
        return self.__id

    def get_color(self):
        return self.__color

    def rotate(self):
        rotated = []
        for block in self.__list:
            r = block[0]
            c = block[1]
            rotated.append((-c, r))
        self.__list = self.__normalise(rotated)
        #rotation matrix = [[0, -1], [1, 0]] # anticlock wise rotation
    
    def __normalise(lists):
        min_row = min(block[0] for block in lists)
        min_col = min(block[1] for block in lists)
        normalised = []
        for block in lists:
            r = block[0] - min_row
            c = block[1] - min_col
            normalised.append((r, c))
        return normalised
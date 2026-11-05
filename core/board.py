import pygame
CELL_COLORS = [
    (231, 76, 60),
    (52, 152, 219),
    (46, 204, 113),
    (241,196, 15),
    (155, 89, 182),
    (230, 126, 34),
]
GRID_COLOR = (50, 50, 50)
class board:
    def __init__(self, rows, cols, margin=40):
        self.__rows=rows
        self.__cols= cols
        self.__margin = margin
        self.__cell = 0
        self.__x = 0
        self.__y = 0
        self.__arr = [[0]*cols for _ in range(rows)]
        
    def __layout(self, screen):
        w, h = screen.get_size()
        self.__cell = min((w-2*self.__margin)//self.__cols,
                          (h-2*self.__margin)//self.__rows)
        self.__x = (w - self.__cell*self.__cols)//2
        self.__y = (h - self.__cell*self.__rows)//2

    def draw(self, screen):
        self.__layout(screen)
        for r in range(self.__rows):
            for c in range(self.__cols):
                rect = pygame.Rect(self.__x+c*self.__cell, self.__y+r*self.__cell, self.__cell, self.__cell)
                value = self.__arr[r][c]
                if value >0:
                    color = CELL_COLORS[(value-1) % len(CELL_COLORS)]
                    pygame.draw.rect(screen, color, rect)
                pygame.draw.rect(screen, GRID_COLOR, rect, 1)
    #turn a mouse position into (row,col), or None if it's outside the grid
    def cell_at(self,pos):
        if self.__cell == 0:
            return None
        col = (pos[0]-self.__x)//self.__cell
        row = (pos[1]-self.__y)//self.__cell
        if 0<= row<self.__rows and 0<=col <self.__cols:
            return row,col
        return None
    


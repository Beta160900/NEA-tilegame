import pygame
from core.pentomino import pentomino_game
class pentomino_scene:
    def __init__(self, manager):
        self.__name = "pentomino"
        self.__manager = manager
        self.__title_font = pygame.font.Font(None, 72)
        self.__font = pygame.font.Font(None, 32)
        self.__custom_btn = pygame.Rect(160, 320, 220, 70)
        self.__ready_btn = pygame.Rect(420, 320, 220, 70)
        self.__game = pentomino_game()
    
    def get_name(self):
        return self.__name

    def handle_events(self, event):
       pass 

    def draw(self, screen):
        #x
        self.__game.get_board().draw(screen)
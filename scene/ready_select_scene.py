import pygame
class ready_select_scene:
    def __init__(self, manager):
        self.__name = "ready"
        self.__manager = manager
        self.__choice = ["Domino", "Peotomino", "Ltromino"]
        self.__selected_choice = 0
        self.__title_font = pygame.font.Font(None, 72)
        self.__font = pygame.font.Font(None, 32)
        self.__custom_btn = pygame.Rect(160, 320, 220, 70)
        self.__ready_btn = pygame.Rect(420, 320, 220, 70)
    
    def get_name(self):
        return self.__name

    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.__selected_choice = (self.__selected_choice + 1) % len(self.__choice)
            elif event.key == pygame.K_LEFT:
                self.__selected_choice = (self.__selected_choice - 1) % len(self.__choice)
            elif event.key == pygame.K_RETURN:
                if self.__selected_choice == 0:
                    self.__manager.change_scene("domino")
                elif self.__selected_choice == 1:
                    self.__manager.change_scene("pentomino")
                elif self.__selected_choice == 2:
                    self.__manager.change_scene("ltromino")


    def draw(self, screen):
        #x
        title = self.__title_font.render("Tile Puzzle", True, "white")
        screen.blit(title, title.get_rect(center=(400, 200)))
        choice_text = self.__font.render(self.__choice[self.__selected_choice], True, "white")
        screen.blit(choice_text, choice_text.get_rect(center=(400, 300)))
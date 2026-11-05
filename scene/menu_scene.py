import pygame

class menu_scene:
    def __init__(self, manager):
        self.__name = "menu"
        self.__manager = manager
        self.__title_font = pygame.font.Font(None, 72)
        self.__font = pygame.font.Font(None, 32)
        self.__custom_btn = pygame.Rect(160, 320, 220, 70)
        self.__ready_btn = pygame.Rect(420, 320, 220, 70)
        
    def get_name(self):
        return self.__name
    
    def __draw_button(self, screen, rect, text):
        pygame.draw.rect(screen, "white", rect, 3, border_radius=8)
        label = self.__font.render(text, True, "white")
        screen.blit(label, label.get_rect(center=rect.center))
 
    def draw_buttons_ready(self, screen):
        self.__draw_button(screen, self.__ready_btn, "Ready mode")
 
    def draw_buttons_custom(self, screen):
        self.__draw_button(screen, self.__custom_btn, "custom mode")
 
    def text_ready(self, screen):
        title = self.__title_font.render("Tile Puzzle", True, "white")
        screen.blit(title, title.get_rect(center=(400, 200)))
 
    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.__custom_btn.collidepoint(event.pos):
                print("custom mode clicked")
                # later: self.__manager.change_scene("custom")
            elif self.__ready_btn.collidepoint(event.pos):
                print("ready mode clicked")
                self.__manager.change_scene("ready")
                # later: self.__manager.change_scene("ready")
 
    # replaces main_loop: main.py owns the loop, the scene just draws
    def draw(self, screen):
        self.text_ready(screen)
        self.draw_buttons_custom(screen)
        self.draw_buttons_ready(screen)
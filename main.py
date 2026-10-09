import pygame
import sys 
from scene.scene import scene_manager
from scene.menu_scene import menu_scene
# setting
WIDTH, HEIGHT = 800, 600
FPS = 60
BG_COLOR = (30, 30, 30)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tile Game Puzzle")
    clock = pygame.time.Clock()

    manager = scene_manager()
    manager.add_scene("menu", menu_scene())
    manager.change_scene("menu")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            manager.handle_events(event)

        screen.fill(BG_COLOR)
        manager.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
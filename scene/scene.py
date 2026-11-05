#scene manager
class scene_manager:
    def __init__(self):
        self.__scenes = []#add menu scene, game scene, etc here by default
        self.__map = {}#map scene name to scene object
        self.__current = None
    def add_scene(self, scene):
        self.__map[scene.get_name()] = len(self.__scenes)
        self.__scenes.append(scene)
    def change_scene(self, name):
        self.__current = self.__scenes[self.__map[name]]
    def handle_events(self, event):
        if self.__current:
            self.__current.handle_events(event)
    def draw(self, screen):
        if self.__current:
            self.__current.draw(screen)
    
import pygame



class Panel:
    def __init__(self, width, height, data):
        self.width = width
        self.height = height
        self.data = data
        self.font_init = pygame.font.init()
        self.font = pygame.font.Font()
        self.white = (255,255,255)

    def make(self, data):
        text = data
        panel = pygame.Surface(self.width, self.height)
        panel = pygame.font.render(text, False, self.white)
        panel = pygame.Surface((40,40))
        return panel
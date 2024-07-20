import pygame



class Panel:
    def __init__(self, width, height, data):
        self.width = width
        self.height = height
        self.data = data
        self.font_init = pygame.font.init()
        self.font = pygame.font.Font()
        self.white = (255,255,255)
        self.count = 0

    def add_text(self):
        text = self.data
        
        panel = pygame.font.render(text, False, self.white)
      
        self.count +=1
        return panel
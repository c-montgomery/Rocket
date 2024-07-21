import pygame



class Panel:
    def __init__(self, x_position, height, stat_name, stat):
        self.x_position = x_position
        self.height = height
        self.stat_name = stat_name
        self.stat = stat
        self.font_init = pygame.font.init()
        self.font = pygame.font.Font("cmb10.ttf", 16)
        self.white = (255,255,255)
        self.count = 0
        self.text_panel = None
    def add_text(self):
        text = str(self.stat_name) + " " + str(self.stat)
        self.text_panel = self.font.render(text, False, self.white, None)
      
        self.count +=1
        return self.text_panel
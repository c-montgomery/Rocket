import sys, pygame
from pygame import *
import math
black = (0,0,0)
white = (251,251,251)
size = (400,400)
screen = pygame.display.set_mode(size)
surface2 = pygame.Surface((2, 10))
shipRect = surface2.get_rect()
surface2.fill(white)

shipRect.x = 200
shipRect.y = 390
clock =  pygame.time.Clock()


class SimObject:
   
    #initialze
    def __init__(self, x_size, y_size, ):
        self.time = clock.tick()
        self.FPS = 60
        self.clock = pygame.time.Clock()
        self.elapsed = 0
       


    def initGame(self):
        pass

    def loop(self):
        #rect1 = Rect(0, 10 , 10, 20,)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
            self.update_pos()
            elapsed = self.clock.tick(self.FPS)
            self.elapsed += elapsed
            print(elapsed)
            print(self.elapsed)
   
    def update_pos(self):
        shipRect.y = math.floor((self.elapsed / 1000)*(5.92**2))
        screen.fill(black)
        #shipRect.fill(0, 125, 0)
        screen.blit(surface2, shipRect)
        pygame.display.flip()


simObj = SimObject(400,400)
simObj.initGame()
simObj.loop()




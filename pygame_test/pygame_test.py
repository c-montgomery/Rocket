import sys, pygame
from pygame import *
import math
import os

########################################################################################
# Run pygame
########################################################################################
black = (0,0,0)
grey  = (50,50,50)
lighter_grey = (150,150,150)
white = (251,251,251)
green = (60, 255, 175)

class SimObject:
   
    #initialze object
    def __init__(self, x_size, y_size):

        self.x_size = x_size    #Window size
        self.y_size = y_size    #Window size
        self.screen = pygame.display.set_mode((x_size, y_size))
        self.FPS = 60
        self.clock = pygame.time.Clock()
        self.time = self.clock.tick()
        self.elapsed = 0

        #Make rocket
        self.rocket = Rocket(6,31, 200, 0, 0, 20)
        self.rocket_png = pygame.image.load("rocket.png")
        self.rocket_png.convert_alpha()
        self.rotated_rocket = pygame.image.load("rocket.png")
        self.shipRect = self.rocket_png.get_rect()
        self.shipRect.x = self.x_size / 2
        self.shipRect.y = self.y_size 
        self.y_offset = 0
        self.x_offset = 0
        
    #Main loop 
    def loop(self):

        while True:
            self.check_keypresses()
            self.update_pos()
            
            elapsed = self.clock.tick(self.FPS)
            self.elapsed += elapsed
        #react to user inputs       
    def check_keypresses(self):
        self.maintain_center(3) #Maintain center without key presses, yuck
        for event in pygame.event.get():
            print("shitto")
            if event.type == pygame.QUIT: 
                sys.exit()

            
            
            elif event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
               

                elif event.key == pygame.K_LEFT:
                    print("Left")
                    self.maintain_center(0)
                    # self.rocket_png = pygame.transform.rotate(self.rocket_png, degrees)    

                elif event.key == pygame.K_RIGHT:
                    print("RIGHT")
                    
                    self.maintain_center(1)
                    #pygame.display.flip()
               
                elif event.key == pygame.K_UP:
                    print("THROTTLE UP")
                    current_throttle = self.rocket.get_throttle()
                    if int(current_throttle) < 100:
                        self.rocket.set_throttle(current_throttle +10)
                elif event.key == pygame.K_DOWN:
                    print("THROTTLE DOWN")
                    if self.rocket.get_throttle() > 0:
                        self.rocket.set_throttle(current_throttle - 10)

        #rotates image about center. rotates like jumping bean w/o this
    def maintain_center(self, direction ):
                degrees = self.rocket.get_rotation()
                if (direction ==1):
                    degrees -= 10
                    self.rocket.set_rotation(degrees)
                elif (direction ==0):
                    degrees += 10
                    self.rocket.set_rotation(degrees)
                else:
                    self.shipRect = self.rocket_png.get_rect()
                    self.screen.fill(grey)
                    x,y = self.shipRect.center
                    self.rotated_rocket = pygame.transform.rotate(self.rocket_png, degrees) 
                    self.x_offset, self.y_offset = self.rotated_rocket.get_rect().center
                    self.shipRect.center = (x ,y )
                  
            
        #Draw bounding rectangle
    def draw_rectangle(self, object):
        pygame.draw.rect(object, (255,255,255), object.get_bounding_rect(), width = 1)

        #fill screen, update image and rectangle placement. Display changes
    def update_pos(self):
        print(self.shipRect.x)
        print(self.shipRect.y)
        #print(self.x_offset)
        if self.rocket.get_rotation() != 0:
            self.shipRect.x = 200  -(self.x_offset)
            self.shipRect.y = self.y_size - ( math.floor(((self.elapsed/ 1000)**1 *(1.2**6)))) -self.y_offset 
            
        else:
            self.shipRect.x = 197
            self.shipRect.y = self.y_size - ( math.floor(((self.elapsed/ 1000)**1 *(1.2**6)))) -self.y_offset 
        
        self.screen.fill(grey)
        self.screen.blit(self.rotated_rocket, self.shipRect)
        pygame.display.flip()
        #self.draw_rectangle(self.screen)


########################################################################################
# Rocket
########################################################################################

class Rocket:
    def __init__(self, height, width, x, y, rotation, throttle, mass=100, fuel=999, max_fuel=999, max_thrust=100):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.center = (0,0)
        self.rotation = rotation
        self.throttle = throttle
        self.mass = mass
        self.fuel = fuel
        self.max_fuel = max_fuel
        self.max_thrust = max_thrust

    # SETTERS
    def set_x(self, x):
        self.x = x
    def set_y(self, y):
        self.y = y
    def set_rotation(self, rotate):
        self.rotation = rotate
    def set_throttle(self, throttle):
        self.throttle = throttle
    def set_fuel(self, fuel):
        self.fuel = fuel
    def set_height(self, height):
        self.height = height
    def set_width(self, width):
        self.width = width
    def set_center(self, center):
        self.center = center

    # GETTERS
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_width(self):
        return self.width
    def get_height(self):
        return self.height
    def get_weight(self):
        return self.weight
    def get_rotation(self):
        return self.rotation
    def get_throttle(self):
        return self.throttle
    def get_mass(self):
        return self.mass
    def get_fuel(self):
        return self.fuel
    def get_center(self, center):
        return self.center
        

simObj = SimObject(480,640)
simObj.loop()




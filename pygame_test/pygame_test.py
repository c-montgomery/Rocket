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
        self.rocket = Rocket(3,15, 0, 0)
        self.ship_surface = pygame.Surface((self.rocket.get_x(), self.rocket.get_y()))
        self.shipRect = self.ship_surface.get_rect(center=(self.rocket.get_x(), self.rocket.get_y()))
        self.shipRect.x = self.x_size / 2
        self.shipRect.y = self.y_size - 1
        self.ship_surface.fill(green)

    #game loop
    def loop(self):
        


        #Main loop 
        while True:
            self.check_keypresses()
            self.update_pos()
            
            elapsed = self.clock.tick(self.FPS)
            self.elapsed += elapsed

            
    def check_keypresses(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                elif event.key == pygame.K_LEFT:
                    print("Left")
                    degrees = self.rocket.get_rotation() + 10
                    self.rocket.set_rotation(degrees)
                    self.screen.fill(grey)
                    self.ship_surface = pygame.transform.rotate(self.ship_surface, degrees)        
                elif event.key == pygame.K_RIGHT:
                    print("RIGHT")
                    degrees = self.rocket.get_rotation() - 10
                    self.rocket.set_rotation(degrees)
                    self.screen.fill(grey)
                    self.ship_surface = pygame.transform.rotate(self.ship_surface, degrees)

                elif event.key == pygame.K_UP:
                    print("THROTTLE UP")
                elif event.key == pygame.K_DOWN:
                    print("THROTTLE DOWN")

  
        
    def update_pos(self):
        self.shipRect.y = self.y_size - math.floor((self.elapsed / 1000)*(1.2**6))
        self.screen.fill(grey)
        #shipRect.fill(0, 125, 0)
 
        self.screen.blit(self.ship_surface, self.shipRect)
        #self.screen.fill(lighter_grey)
        # ship = pygame.Surface((3,12))
        # rotated_ship = pygame.transform.rotate(ship, 45)
        # rotated_rect = rotated_ship.get_rect()
       

        #self.screen.blit(rotated_ship, rotated_rect )
        pygame.display.flip()



########################################################################################
# Rocket
########################################################################################

class Rocket:
    def __init__(self, x, y, rotation, thrust, mass=100, fuel=999, max_fuel=999, max_thrust=1000):
        self.x = x
        self.y = y
        self.rocket_png = pygame.image.load("rocket.png")
        self.rotation = rotation
        self.thrust = thrust
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
    def set_thrust(self, thrust):
        self.thrust = thrust
    def set_fuel(self, fuel):
        self.fuel = fuel

    # GETTERS
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_rotation(self):
        return self.rotation
    def get_thrust(self):
        return self.thrust
    def get_mass(self):
        return self.mass
    def get_fuel(self):
        return self.fuel
        








simObj = SimObject(500,400)
simObj.loop()




import sys, pygame
from pygame import *
from Rocket import *
import time
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
        #pygame.display.gl_set_attribute(GL_ACCELERATED_VISUAL, 1)
        pygame.key.set_repeat(200,50)
        self.FPS = 60
        self.clock = pygame.time.Clock()
        self.time = self.clock.tick()
        self.elapsed = 0
        self.last_time = time.time()
        self.time_segment = 0
        self.time_start = 0
        self.elapsed_total = 0
        self.isRunning = True

        self.rocket = Rocket(16,2, 100, 17, 0, 10)
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
        
        while (self.isRunning):
            self.check_keypresses()
            self.print_debug()
            self.update_pos()
            elapsed = time.time() - self.last_time
            self.time_segment = elapsed
            self.elapsed_total = time.time() - self.time_start
            self.rocket.set_time_segment(elapsed)
            self.last_time = self.time_start + self.elapsed_total

    def setup(self):
        
        pygame.display.set_caption("Rocket Simulation")
        self.time_start = time.time() 

        #react to user inputs       
    def check_keypresses(self):
        self.maintain_center(3) #Maintain center without key presses, yuck
        for event in pygame.event.get():
            current_throttle = self.rocket.get_throttle()
            if event.type == pygame.QUIT: 
                sys.exit()
            
            elif event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
  
                elif event.key == pygame.K_LEFT:
                    print("Left")
                    self.maintain_center(0)   

                elif event.key == pygame.K_RIGHT:
                    print("RIGHT")
                    self.maintain_center(1)
                    #pygame.display.flip()
               
                elif event.key == pygame.K_UP:
                    if (self.rocket.throttle > 80):
                        self.rocket_png = pygame.image.load("rocket_full_thrust.png")
                        self.rotated_rocket = pygame.image.load("rocket_full_thrust.png")

                    elif(self.rocket.throttle > 0):
                    
                        self.rocket_png = pygame.image.load("rocket_half_thrust.png")
                        self.rotated_rocket = pygame.image.load("rocket_half_thrust.png")

                    else:
                        self.rotated_rocket = pygame.image.load("rocket.png")
                        self.rocket_png = pygame.image.load("rocket.png")
                    
                    if int(current_throttle) < self.rocket.max_thrust:
                        self.rocket.set_throttle(current_throttle + 10)
                elif event.key == pygame.K_DOWN:
                    if self.rocket.get_throttle() <= 0:
                        self.rocket.set_throttle(0)
                    else:
                        self.rocket.set_throttle(self.rocket.get_throttle()-10)
                        
        

        #rotates image about center. rotates like jumping bean w/o this
    def maintain_center(self, direction ):
                degrees = self.rocket.get_rotation()
                if (direction ==1):
                    degrees -= 2
                    self.rocket.set_rotation(degrees)
                elif (direction ==0):
                    degrees += 2
                    self.rocket.set_rotation(degrees)
                
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

       
    def print_debug(self):
      
        print()
        print("get v ", self.rocket.get_v())
        print("get v_final", self.rocket.get_v_final())
        # print("get net_accel", str(self.rocket.net_accel))
        # print("get time segment", str(self.rocket.get_time_segment()))      
        # print("rocketx" ,str(self.rocket.get_x()))
        print("rockety", str(self.rocket.get_y()))
        print("rocketx", str(self.rocket.get_x()))
        print("throttle", self.rocket.throttle)
        # print(self.shipRect.y)
       

        #do math to find position, rotation, etc and print to screen
    def update_pos(self):
        
        x, y = self.rocket.calc_distance()[0], self.rocket.calc_distance()[1]
   
        self.shipRect.x = 147 + (x-self.x_offset)
        self.rocket.calc_net_accel()
        self.rocket.calc_v_final()
        self.shipRect.y = self.y_size - ( self.y_offset + y)
        if self.rocket.y <=17 and self.rocket.y_vel_final <= 0:
            self.shipRect.y = 1278
            self.rocket.y = 17
            self.throttle = 0
            self.y_accel = 0
            self.rocket.y_vel_final = 0
            self.rocket.y_vel = 0
            
        print("shipRect.x", self.shipRect.x)
        print("shipRect.y", self.shipRect.y)
        self.rocket.set_y = self.shipRect.y
        self.rocket.set_time_elapsed(self.elapsed)
        #update screen
        self.screen.fill(grey)
        self.screen.blit(self.rotated_rocket, self.shipRect)
        pygame.display.flip()
        
        


    #Create surface, populate with windowlets   
    def update_debug_panel(self):
        stats = [self.shipRect.x, self.shipRect.y] 
        display.get_window_size()[0]/4
        for i in stats:
           self.make_panel(i)

    def make_panel(self, stat):
        pass

        
        
    

simObj = SimObject(500,1300)
simObj.loop()




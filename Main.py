import time
from Grid import Grid
import sys
from Control import Control

#Setup and run systems
class Main:
    def __init__(self, fps=60, x=100, y=100 , has_panel=True):
        self.fps = 60
        self.x = x
        self.y = y
        self.has_panel = True
        #Constants
        self.GRAVITY = -9.81 #m/s^2
        self.WEIGHT = 1000 #kg
        self.frame_rate = 60
      
        self.time_between_frame = 1/60
        self.current_position = ["",""]

        #total frames
        self.iterations = 100

    
    #set the x and y
    def set_position(self, x, y):
        self.current_position[0] = self.y-y
        self.current_position[1] = self.x-x

    #add 1 to coordinates 
    def increase_position(self):
        self.set_position(self.x+1,0)
        #position[1]-=1
        return self.current_position


    #set frames/second
    def set_framerate(self, fps):
        self.fps = fps
        ms_per_frame = 1/fps

        return ms_per_frame
    
    #Startup
    def run(self):
    
        grid = Grid(self.x, self.y) 
        grid.make_grid()
        time_between_frame = self.set_framerate(60)
        self.set_position(50,0)
        x = 0
        while (x< self.iterations):

            
            
            grid.update_position(self.current_position[0], self.current_position[1])
            self.increase_position()
            grid.print_grid()
            time.sleep(time_between_frame)
            x += 1
        #start instance of Control for controlling vehicle
        # control = Control()
        # control.start_listener()
        
            #print(grid.x , iterations)
            # grid.x wont find current position; if (grid.x == 1):
            
if __name__ == '__main__':
    Main().run()
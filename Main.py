import time
from Grid import Grid
import sys
from Control import Control
from Rocket import Rocket
import threading

from pynput import keyboard


#Setup and run systems
class Main:
    def __init__(self, fps=60, x=100, y=100 , has_panel=True):
        self.fps = 60
        self.x = x #for grid x-dimension 
        self.y = y #for grid y-dimension 
        self.has_panel = True
        #Constants
        self.GRAVITY = -9.81 #m/s^2
        self.WEIGHT = 1000 #kg
        self.frame_rate = 60
      
        self.time_between_frame = 1/60
        self.current_position = ["",""]

        #total frames
        self.iterations = 100

    #routine to create rocket
    def create_rocket(self, length=3, width=1, weight=1000, angle=90):
        rocket = Rocket(length, width, weight, angle )
        return rocket



    
    #set the x and y
    def set_position(self, x, y):
        self.current_position[0] = self.y-y
        self.current_position[1] = self.x-x


    #add 1 to coordinates 
    def increase_position(self):
        self.set_position(self.x+1,self.y+1)
        #position[1]-=1
        return self.current_position


    #set frames/second
    def set_framerate(self, fps):
        self.fps = fps
        ms_per_frame = 1/fps

        return ms_per_frame
    
    # Function to handle keyboard input
    def on_press(key):
        print('Key {} pressed.'.format(key))

    #Startup
    def run(self):
    
        grid = Grid(self.x, self.y) 
        grid.make_grid()
        time_between_frame = self.set_framerate(30)
        print("position abouty to update")
        grid.update_position(50,0)
        x = 0
        rocket = self.create_rocket()
        #start instance of Control for controlling vehicle
        #control = Control()
        #control.start_listener()
        print("about to while")
        while (x< self.iterations):

            
            self.increase_position()
            grid.update_position(self.current_position[0], self.current_position[1])
            self.increase_position()
            grid.print_grid()
            print(round(time.time() * 1000))
            time.sleep(time_between_frame)
            print(round(time.time() * 1000))
            x += 1
            print("frame ", x)
        
            #print(grid.x , iterations)
            # grid.x wont find current position; if (grid.x == 1):
            
if __name__ == '__main__':
    animation_thread = threading.Thread(target=Main().run())
    animation_thread.daemon = True  # Daemonize the thread so it exits when the main thread exits
    animation_thread.start()
    # Start listening for keyboard input
    with keyboard.Listener(on_press=Main.on_press) as listener:
        listener.join()
  
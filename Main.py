import time
from Grid import Grid
import sys
from Rocket import Rocket
import threading
from Display_panel import Display_panel
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
        self.current_position = [0,0]

        #total frames
        self.iterations = 100

        #dict w/stats
        self.stats = {"velocity": 69}

    #routine to create rocket
    def create_rocket(self, length=3, width=1, weight=1000, angle=90):
        rocket = Rocket(length, width, weight, angle )
        return rocket



    
    #set the x and y
    def set_position(self, x, y):
        self.current_position[0] = x
        self.current_position[1] = y


    #add 1 to coordinates 
    def increase_position(self):
        self.set_position(self.x+1,self.y+1)
        
        return self.current_position


    #set frames/second
    def set_framerate(self, fps):
        self.fps = fps
        ms_per_frame = 1/fps

        return ms_per_frame
    
    # Function to handle keyboard input
    def on_press(key):

        print('{} press'.format(key))

    #Startup
    def run(self):
    
        grid = Grid(self.x, self.y) 
        grid.make_grid()
        time_between_frame = self.set_framerate(30)
        grid.update_position(5,5)
        x = 0
        rocket = self.create_rocket()
        display = Display_panel(True)
        while (x< self.iterations):

            self.current_position[0] +=1
            self.current_position[1] +=1
            grid.update_position(self.current_position[0], self.current_position[1])
            
            grid.print_grid()
            display.update_info_panel(self.stats)
            display.print_info_panel()
            time.sleep(time_between_frame)
            x += 1
            
if __name__ == '__main__':
    animation_thread = threading.Thread(target=Main().run())
    animation_thread.daemon = True  # Daemonize the thread so it exits when the main thread exits
    animation_thread.start()
    # Start listening for keyboard input
    with keyboard.Listener(on_press=Main.on_press) as listener:
        listener.join()
  
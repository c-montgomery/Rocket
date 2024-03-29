import time
from Grid import Grid
import sys
from Rocket import Rocket
import threading
from Display_panel import Display_panel
from pynput import keyboard


#Setup and run systems
class Main:
    def __init__(self, fps=60, x=50, y=50 , has_panel=True):
        self.fps = 60
        self.x = x #for grid x-dimension 
        self.y = y #for grid y-dimension 
        self.has_panel = True
        #Constants
        self.GRAVITY = -9.81 #m/s^2
        self.WEIGHT = 1000 #kg
        self.frame_rate = 60
        self.time_between_frame = 1/60

        self.current_position = [24,3]

        #total frames
        self.iterations = 4000

        self.stats = {"velocity": 0,
                      "key pressed: ": "",
                      "thrust: ": 0,
                      "thrust angle: ": 90,
                      "orientation: ": 90,
                      "debug": "",
                      "iterations: ": 0}
    
    #routine to create rocket object
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
        return self.current_positiond


    #set frames/second
    def set_framerate(self, fps):
        self.fps = fps
        ms_per_frame = 1/fps
        return ms_per_frame
    
    # Function to handle keyboard input 
    def on_press(self, key):
        try:
            self.stats["key pressed: "] = key.char
            if (key.char =='w'):
                if (self.stats["thrust: "] < 100):
                    self.stats["thrust: "] += 10
            elif(key.char == 's'):
                if (self.stats["thrust: "] >= 10):
                    self.stats["thrust: "] -= 10
            elif(key.char == 'a'):
                if (self.stats["orientation: "] != 360):
                    self.stats["orientation: "] += 10
                else:
                    self.stats["orientation: "] = 10

            elif(key.char == 'd'):
                if (self.stats["orientation: "] != 0):
                    
                    self.stats["orientation: "] -= 10
                else:
                    self.stats["orientation: "] = 350
        except AttributeError:
            print("Attribute Error caught")
            print("key: ", key)
            self.stats["key pressed: "] = key
            
    # Start listening for keyboard inputs
    def listen(self):
        
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()

    #Run simulations
    def run(self):   
        grid = Grid(self.x, self.y) 
        grid.make_grid()
        rocket = Rocket(3,1,1000,0)
        time_between_frame = self.set_framerate(30)
        #grid.clear_old_position()
        grid.update_position(5,5, rocket.get_orientation())
        x = 0
        display = Display_panel(True)
        while (self.stats["iterations: "] < self.iterations):

            #self.current_position[0] +=1
            #self.current_position[1] +=1
            grid.update_position(self.current_position[0], self.current_position[1],self.stats["orientation: "])
            
            grid.print_grid()
            self.stats["iterations: "] = x
            display.update_info_panel(self.stats)
            if (self.has_panel):
                display.print_info_panel()
            
            time.sleep(time_between_frame)
            x += 1
            
if __name__ == '__main__':
    main_instance = Main()
    animation_thread = threading.Thread(target=main_instance.run)
    keystroke = threading.Thread(target=main_instance.listen)
    animation_thread.daemon = True  # Daemonize the thread so it exits when the main thread exits
    animation_thread.start()
    keystroke.start()
    
  
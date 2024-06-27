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
        
        #Rocket
        self.orientation = 90
        self.throttle = 0
        #Constants
        self.GRAVITY = -9.81 #m/s^2
        self.WEIGHT = 1000 #kg
        self.frame_rate = 60

        self.current_position = [24,3]

        #total frames
        self.iterations = 4000
        self.start_time = 0
         #time
        self.elapsed = 0
        self.time_since_last_frame = 0

        self.stats = {"velocity": 0,
                      "acceleration: ": 0,
                      "key pressed: ": "",
                      "throttle: ": 0,
                      "thrust angle: ": 90,
                      "orientation: ": 90,
                      "fpv": 0,
                      "total_elapsed: ": 0,
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
                if (self.stats["throttle: "] < 100):
                    self.stats["throttle: "] += 10
                    self.throttle = self.stats["throttle: "]
            elif(key.char == 's'):
                if (self.stats["throttle: "] >= 10):
                    self.stats["throttle: "] -= 10
                    self.throttle = self.stats["throttle: "]
            elif(key.char == 'a'):
                if (self.stats["orientation: "] != 360):
                    self.stats["orientation: "] += 10
                    self.orientation = self.stats["orientation: "]
                else:
                    self.stats["orientation: "] = 10
                    self.orientation = self.stats["orientation: "]

            elif(key.char == 'd'):
                if (self.stats["orientation: "] != 0):
                    
                    self.stats["orientation: "] -= 10
                    self.orientation = self.stats["orientation: "]
                else:
                    self.stats["orientation: "] = 350
                    self.orientation = self.stats["orientation: "]
        except AttributeError or KeyError:
            print("Attribute Error caught")
            print("key: ", key)
            self.stats["key pressed: "] = key
            
    # Start listening for keyboard inputs
    def listen(self):
        
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()

    #pass info to rocket
    def update_rocket(self, object):
        object.set_throttle(self.throttle)
        object.set_orientation(self.orientation)


    #Run simulations
    def run(self):   
        self.start_time = time.time()
        grid = Grid(self.x, self.y)
        grid.make_grid()

        rocket = Rocket(3,1,1000,0)
        time_between_frame = self.set_framerate(30)
        grid.update_position(5,5, rocket.get_orientation())
        x = 0 #measures iterations
        
        display = Display_panel(True)
        start_time = time.time()
        while (self.stats["iterations: "] < self.iterations):
            
            self.elapsed = time.time() - start_time
            self.time_since_last_frame = time.time() - self.elapsed
            
            self.stats["elapsed: "] = "{:4.2f}".format(self.elapsed)
            grid.update_position(self.current_position[0], self.current_position[1],self.stats["orientation: "])
            
            grid.print_grid()
            self.stats["iterations: "] = x
            self.stats["acceleration: "] = rocket.calc_accel()
            self.stats["velocity: "] = rocket.calc_velocity()
            rocket.update_info_panel(self.stats)
            display.update_info_panel(self.stats)
            self.update_rocket(rocket)
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
    
  
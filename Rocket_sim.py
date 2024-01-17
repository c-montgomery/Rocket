import time
import pynput
from Grid import Grid
import sys





if __name__ == '__main__':

    #Constants
    GRAVITY = 9.81

    time_between_frame = 1/60
    position = [1,1]




    #total frames
    iterations = 100

    #current frame
    x = 1
    
    #add 1 to coordinates 
    def increase_position():
        position[0]+=1
        position[1]+=1
        return position

    #set the x and y
    def set_position(x, y):
        position[0] = x
        position[1] = y
        

    #set frames/second
    def set_speed(fps):
        ms_per_frame = 1/fps

        return ms_per_frame
        
    #Run it
    grid = Grid(100, 100) 
    grid.make_grid()
    time_between_frame = set_speed(1)
    while (x< iterations):
        
    
        
        increase_position()
        time_between_frame /=1.03
        grid.update_position(position[0], position[1])
        grid.print_grid()
        time.sleep(time_between_frame)
        x += 1
        #print(grid.x , iterations)
        # grid.x wont find current position; if (grid.x == 1):
sys.exit()

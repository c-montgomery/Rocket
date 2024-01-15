import time
import pynput

#Constants
GRAVITY = 9.81



rows = ["","","","","","","","","",""]*10
columns = ["","","","","","","","","",""]*10
grid = [rows,rows,rows,rows,rows,rows,rows,rows,rows,rows]

time_between_frame = 1/60
position = [1,1]




#total frames
iterations = 100

#current frame
x = 0



#print grid w/# in position
def make_frame(position):
    j=0
    k=0
    #Rows
    for y in rows:
        print("row: ", j)
        j+=1    
        #Columns
        for x in columns:
            if (j == position[0] and k == position[1]):
            
                print('#', end='')
            else:
                print(".", end='')
            k+=1
        k=0
    
    
def increase_position():
    position[0]+=1
    position[1]+=1


#set the x and y
def set_position(x, y):
    position[0] = x
    position[1] = y


#set frames/second
def set_speed(fps):
    ms_per_frame = 1/fps

    return ms_per_frame
    

time_between_frame = set_speed(20)
while (True):
    
    make_frame(position)
    increase_position()
    x+=1
    time.sleep(time_between_frame)
    
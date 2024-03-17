

class Grid:
    def __init__(self, x, y):
        self.x = x #x-dimension
        self.y = y #y-dimension
        self.grid = []
        self.last_position = [1,1]

    #create blank matrix x*y
    def make_grid(self):
        grid = []
        for i in range(self.x):
            row = ["."]*self.y
            grid.append(row)
        self.grid = grid
     
    #print grid to terminal
    def print_grid(self):
        print()
        for i in range(self.y):
            for j in range(self.x):
                print(self.grid[j][self.y - (i+1)], end="")
              
            print()

    #clear 8 spaces around last position, erase last frame
    #Should calc area by the size of rocket
    def clear_old_position(self):
        self.grid[int(self.last_position[0])][int(self.last_position[1])]= "."
        self.grid[int(self.last_position[0])][int(self.last_position[1]+1)]= "."
        self.grid[int(self.last_position[0])][int(self.last_position[1]-1)]= "."
        self.grid[int(self.last_position[0]+1)][int(self.last_position[1]+1)]= "."
        self.grid[int(self.last_position[0]-1)][int(self.last_position[1]-1)]= "."
        self.grid[int(self.last_position[0]+1)][int(self.last_position[1])]= "."
        self.grid[int(self.last_position[0]-1)][int(self.last_position[1])]= "."
        self.grid[int(self.last_position[0]-1)][int(self.last_position[1]+1)]= "."
        self.grid[int(self.last_position[0]+1)][int(self.last_position[1]-1)]= "."

    #erase last position, draw new
    
    def update_position(self, x, y, orientation):
        self.clear_old_position()
        try:
            #overwrite last position w/a "."
            #currently doesnt know orientation
            self.last_position = [x, y]
            if (orientation>67.5 and orientation <112.5 or orientation >247.5 and orientation <292.5):
                print("tripped first")
                self.grid[int(self.last_position[0])][int(self.last_position[1])]= "."
                self.grid[int(self.last_position[0])][int(self.last_position[1]+1)]= "."
                self.grid[int(self.last_position[0])][int(self.last_position[1]-1)]= "."
                self.last_position = [(x), (y)]
                self.grid[x][y] = "#" #rocket center
                self.grid[x][y+1]= "#"
                self.grid[x][y-1] = "#"
            elif (orientation>22.5 and orientation <67.5 or orientation >202.5 and orientation <247.5):
                print("tripped second")
                self.grid[int(self.last_position[0])][int(self.last_position[1])]= "."
                self.grid[int(self.last_position[0])][int(self.last_position[1]+1)]= "."
                self.grid[int(self.last_position[0])][int(self.last_position[1]-1)]= "."
                self.last_position = [(x), (y)]
                self.grid[x][y] = "#" #rocket center
                self.grid[x+1][y+1]= "#"
                self.grid[x-1][y-1] = "#"
            elif((orientation<22.5 or orientation >337.5 )or orientation>157.5 and orientation<202.5):
                print("tripped third")
                self.grid[int(self.last_position[0])][int(self.last_position[1])]= "."
                self.grid[int(self.last_position[0])][int(self.last_position[1]+1)]= "."
                self.grid[int(self.last_position[0])][int(self.last_position[1]-1)]= "."
                self.last_position = [(x), (y)]
                self.grid[x][y] = "#" #rocket center
                self.grid[x-1][y]= "#"
                self.grid[x+1][y] = "#"
            elif(orientation):
                print("DIDNT trip")
               
                self.last_position = [(x), (y)]
                self.grid[x][y] = "#" #rocket center
                self.grid[x-1][y+1]= "#"
                self.grid[x+1][y-1] = "#"

        except IndexError:
            print("out of range")
    
   










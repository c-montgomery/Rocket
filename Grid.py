

class Grid:
    def __init__(self, x, y):
        self.x = x #x-dimension
        self.y = y #y-dimension
        self.grid = []
        self.last_position = [1,1]
        self.x_constraint = x
        self.y_constraint = y


    #create blank matrix x*y
    def make_grid(self):
        grid = []
        
        for i in range(self.x):
            row = ["."]*self.y
            grid.append(row)
        self.grid = grid
     
    #print grid to terminal
    def print_grid(self):
        for i in range(self.y):
            #print (i, end="")
            for j in range(self.x):
                print(self.grid[j][i], end="")
               #print(j, end="")
            print()

    #erase last position, draw new
    def update_position(self, x, y):
        
        
       #print(self.last_position[0],[self.last_position[1]])
        self.grid[int(self.last_position[0])][int(self.last_position[1])]= "."
        self.last_position = [x, y]
        print("x", x, "y",  y)
        #print( self.grid[x][y])
        self.grid[x][y] = "#" #rocket center









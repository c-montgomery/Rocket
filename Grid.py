

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
        for i in range(self.y):
            #print (i, end="")
            for j in range(self.x):
                print(self.grid[j][i], end="")
               #print(j, end="")
            print()

    #erase last position, draw new
    #Converts NE Origin to SE
    def update_position(self, x, y):
        
        print("lastPosition")
        print(int(self.last_position[0]),int(self.last_position[1]))
        print("Length")
        print(len(self.grid))
        self.grid[int(self.last_position[0])][int(self.last_position[1])]= "."
        self.last_position = [(x), (y)]
        # print("x", x, "y",  y)
        # print("self.y ", self.y)
        # print("self.y - y " , end="")
        # print((self.y)-int(y))
        # print("self.x ", self.x)
        # print("self.x - x " , self.x-x)
        # print("len [0] ", len(self.grid[0]))
        # print("len [1] ", len(self.grid))
        #print( self.grid[x][y])
        try:
            self.grid[x][y] = "#" #rocket center
        except IndexError:
            print("out of range")











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
                print(self.grid[j][i], end="")
              
            print()

    #erase last position, draw new
    #Converts NE Origin to SE--incomplete
    def update_position(self, x, y):
        
       
        try:
            #overwrite last position w/a "."
            self.grid[int(self.last_position[0])][int(self.last_position[1])]= "."
            self.last_position = [(x), (y)]
            self.grid[x][y] = "#" #rocket center
        except IndexError:
            print("out of range")









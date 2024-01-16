

class Grid:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.grid = []
        self.last_position = [0,0]


    #create blank matrix x*y
    def make_grid(self):
        grid = []
        for i in range(self.y):
            row = ["."]*self.x
            grid.append(row)
        self.grid = grid
    

    def print_grid(self):
        for i in range(self.y):
            for j in range(self.x):
                print("", end='')
                print(self.grid[i][j], end="")
            print()

    def update_position(self, x, y):
        if self.last_position:
            self.grid[int(self.last_position[0])][int(self.last_position[1])]= "."
        self.last_position = [x,y]
        if (x < self.x and y < self.y):
            self.grid[x][y] = "#"





# blank = Grid(100,100)
# blank.make_grid()
# blank.print_grid(blank.x, blank.y)




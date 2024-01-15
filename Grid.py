

class Grid:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.grid = []

    #create blank matrix x*y
    def make_grid(self):
        grid = []
        for i in range(self.y):
            row = ["."]*self.x
            grid.append(row)
        self.grid = grid
    

    def print_grid(self, x , y):
        for i in range(self.x):
            for j in range(self.y):
                print(" ", end='')
                print(self.grid[i][j], end="")
            print()


   # def update_

blank = Grid(100,100)
blank.make_grid()
blank.print_grid(blank.x, blank.y)




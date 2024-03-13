
#class measures width of terminal and creates panel in any empty space
class Display_panel:
    def __init__ (self, is_displaying):
        self.is_displaying = is_displaying
        self.velocity = 0
        self.acceleration = 0
        self.x_position = 0
        self.info = {
            "velocity": self.velocity,
            "acceleration": self.acceleration,
            "x-position": self.x_position
        }

    def set_velocity(self, vel):
        self.velocity = vel
    
    def set_acceleration(self, accel):
        self.acceleration = accel
    
    def set_position(self, pos):
        self.position = pos

    def update_info_panel(self, info_in):
        for x in info_in.keys():
            if x == "velocity":
                self.info["velocity"] = info_in[x]
                print(info_in[x])
                print("rec'd some shit^^")

    def print_info_panel(self):
        for x in self.info:
            print(x, " " , end = "")
    
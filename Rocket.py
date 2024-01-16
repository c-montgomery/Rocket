class Rocket:
    def __init__(self, length, width, weight, thrust):
        self.length = length
        self.width = width
        self.weight = weight
        self.thrust = 0


    #Setters
    def set_length(self, length):
        self.length = length
    def set_width(self, width):
        self.width = width
    def set_weight(self, weight):
        self.weight = weight
    def set_thrust(self, thrust):
        self.thrust = thrust

    #Getter
    def get_length(self):
        return self.length
    def get_width(self):
        return self.width
    def get_weight(self):
        return self.weight
    def get_thrust(self):
        return self.thrust
    
    #draw rocket on grid
    def draw_rocket(self):
        pass
    #draw exhaust
    def draw_exhaust(self):
        pass
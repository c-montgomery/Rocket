
#Constant
GRAVITY = 9.81


class Rocket:
    def __init__(self, length, width, weight, angle = 0):
        self.length = length
        self.width = width
        self.weight = weight
        self.thrust = 0
        self.angle = 0
        self.is_engine_on = False
        self.has_visible_thrust = False

    #Setters
    def set_length(self, length):
        self.length = length

    def set_width(self, width):
        self.width = width

    def set_weight(self, weight):
        self.weight = weight

    def set_thrust(self, thrust):
        self.thrust = thrust

    def set_angle(self, angle):
        self.angle = angle

    


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

    #Bools
    def toggle_animate_thrust(self):
        pass

    def toggle_engine(self):
        if self.is_engine_on == True:
            self.is_engine_on = False
            self.has_visible_thrust = False
        else:
            self.is_engine_on = True
            self.has_visible_thrust = True
            #toggle_animate_thrust(self)

    
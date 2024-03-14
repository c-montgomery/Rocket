


class Rocket:
    def __init__(self, length, width, mass, angle = 0):
        self.LENGTH = length
        self.WIDTH = width
        self.MASS = mass
        self.thrust = 0#thrust force
        self.angle = 0#Angle of thrust
        self.orientation = 90 #orientation of vehicle
        self.has_visible_thrust = False
        self.GRAVITY = -9.81
        self.GRAVxMASS = self.GRAVITY * self.MASS
        

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
    def get_orientation(self):
        return self.orientation

    #draw rocket on grid
    def draw_rocket(self):
        pass
    #draw exhaust
    def draw_exhaust(self):
        pass

    #Bools
    def toggle_animate_thrust(self):
        pass

    

    
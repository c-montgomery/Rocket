
import time

class Rocket:
    def __init__(self, length, width, mass, angle = 0):
        self.time_delta = 0
        self.dist_delta = 0
        self.LENGTH = length
        self.WIDTH = width
        self.mass = mass
        self.MAX_THRUST = 1000000 #100000N
        self.throttle = 0#thrust percentage
        self.angle = 0#Angle of thrust
        self.orientation = 90 #orientation of vehicle
        self.has_visible_thrust = False
        self.GRAVITY = -9.81
        self.velocity = 0
        self.acceleration = 0
        self.info = {"throttle: ": 0,
                     "acceleration: ": 0
                     }

    #Setters
    def set_length(self, length):
        self.length = length

    def set_width(self, width):
        self.width = width
    #mass
    def set_weight(self, weight):
        self.weight = weight
    #acceleration of engine
    def set_throttle(self, throttle):
        self.throttle = throttle
    #orientation of vehicle
    def set_orientation(self, angle):
        self.orientation = angle


    #Getter
    def get_gravity(self):
        return -9.81

    def get_length(self):
        return self.length
    
    def get_width(self):
        return self.width
    
    def get_mass(self):
        return self.mass
    
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

    
    def update_info_panel(self, info_in):
        for x in info_in.keys():
            self.info[x] = info_in[x]
            if (x == "acceleration: "):
                self.acceleration = self.info[x]

    #Physics
    def calc_velocity(self):
        print("self.velocity = " , self.velocity)

        print("self.acceleration = " , self.acceleration)
        self.velocity = self.acceleration * self.time_delta
        return self.velocity
    

    def calc_accel(self):
        N_of_thrust = ((self.throttle/100) * self.MAX_THRUST) + \
        (self.mass * self.GRAVITY)
        self.accel = N_of_thrust/self.mass
        return N_of_thrust/self.mass

    def calc_position(self):
        pass
        self.velocity

    def calc_net_force(self):
        pass
        mg = self.GRAVxMASS
        accel = self.calc_accel()
        net = -(mg)+ accel
        return net
    
    def calc_altitude(self):
        pass

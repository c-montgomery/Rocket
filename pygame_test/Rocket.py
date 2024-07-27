
import math

########################################################################################
# Rocket
########################################################################################

class Rocket:
    def __init__(self, height, width, x, y, rotation, throttle=1, mass=100, fuel=999, max_fuel=999, max_thrust=8000):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.center = (0,0)
        self.rotation = rotation
        self.throttle = 0
        self.mass = 100
        self.fuel = fuel
        self.v = 0
        self.v_final = 0
        self.max_fuel = max_fuel
        self.max_thrust = max_thrust
        self.gravity = -9.81
        self.time_elapsed = 0
        self.time_delta=0
        self.distance = 0
        self.net_accel = 0
        self.x_accel = 0
        self.y_accel = 0
        self.x_vel = 0
        self.y_vel = 0
        self.x_vel_final = 0
        self.y_vel_final = 0
        self.vector_direction = 0
        self.velocity_vector = 0

    # SETTERS
    def set_x(self, x):
        self.x = x
    def set_y(self, y):
        self.y = y
    def set_rotation(self, rotate):
        self.rotation = rotate % 360
    def set_throttle(self, throttle):
        if throttle >100:
            self.throttle = 100
        elif throttle < 0:
            self.throttle = 0
        else:
            self.throttle = throttle     
    def set_fuel(self, fuel):
        self.fuel = fuel
    def set_height(self, height):
        self.height = height
    def set_width(self, width):
        self.width = width
    def set_center(self, center):
        self.center = center
    def set_time_delta(self,time):
        self.time_delta = time
    def set_time_elapsed(self,time):
        self.time_elapsed = time

    # GETTERS
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_throttle(self):
        return self.throttle
    def get_width(self):
        return self.width
    def get_height(self):
        return self.height
    def get_weight(self):
        return self.weight
    def get_rotation(self):
        return self.rotation
    def get_distance(self):
        return self.calc_distance
    def get_v(self):
        return self.v
    def get_v_final(self):
        return self.v_final
    def get_time_delta(self):
        return self.time_delta
    def get_vector_direction(self):
        self.vector_direction = math.atan2(self.y_vel,self.x_vel) 
           
            
        
        return self.vector_direction
    
    # def find_quadrant(self):
    #     if (self.rotation % 360 >180 and self.rotation % 360 < 270):
    #        self.vector_direction +=180
    #     elif(self.rotation % 360 >90 and self.rotation % 360 < 180 ):
    #         self.vector_direction = self.get_vector_direction() +90
    #     else:
    #         self.vector_direction = (self.get_vector_direction()) + 270
             
    
    def compute_update(self):
        self.calc_net_accel()
        self.calc_v_final()
         
    def calc_net_accel(self):
        mg = self.mass * self.gravity #-981
        propulsion = (self.throttle/100) * self.max_thrust
        self.x_accel = propulsion * math.cos((self.get_rotation())*(math.pi/180))
        self.y_accel = mg + (propulsion * math.sin((self.get_rotation())*(math.pi/180))) 
        self.net_accel = (mg + (self.y_accel * (self.throttle/100)))/10
        
    def calc_v_final(self):
        self.x_vel_final = self.x_vel + (self.x_accel * self.time_delta/1000)
        self.x_vel = self.x_vel_final
        self.y_vel_final = self.y_vel + (self.y_accel * self.time_delta/1000)
        self.y_vel = self.y_vel_final
        self.velocity_vector = math.sqrt(self.y_vel**2 + self.x_vel**2)

    def calc_distance(self):
        self.y +=(self.y_vel_final * (self.time_delta) + (.5 * self.y_accel * (self.time_delta)**2))
        self.x +=(self.x_vel_final * (self.time_delta) + (.5 * self.x_accel * (self.time_delta)**2))
        position = [self.x, self.y]

        return position
        #compensate for -x's and/or -y's
    
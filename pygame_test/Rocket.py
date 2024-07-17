
import math

########################################################################################
# Rocket
########################################################################################

class Rocket:
    def __init__(self, height, width, x, y, rotation, throttle=10, mass=100, fuel=999, max_fuel=999, max_thrust=1000):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.center = (0,0)
        self.rotation = rotation
        self.throttle = 98.1
        self.mass = 100
        self.fuel = fuel
        self.v = 0
        self.v_final = 0
        self.max_fuel = max_fuel
        self.max_thrust = max_thrust
        self.gravity = -9.81
        self.time_elapsed = 0
        self.time_segment=0
        self.distance = 0
        self.net_accel = 0
        self.x_accel = 0
        self.y_accel = 0
        self.x_vel = 0
        self.y_vel = 0
        self.x_vel_final = 0
        self.y_vel_final = 0

    # SETTERS
    def set_x(self, x):
        self.x = x
    def set_y(self, y):
        self.y = y
    def set_rotation(self, rotate):
        self.rotation = rotate
    def set_throttle(self, throttle):
        self.throttle = throttle
    def set_fuel(self, fuel):
        self.fuel = fuel
    def set_height(self, height):
        self.height = height
    def set_width(self, width):
        self.width = width
    def set_center(self, center):
        self.center = center
    def set_time_segment(self,time):
        self.time_segment = time
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
    def get_time_segment(self):
        return self.time_segment
    def compute_update(self):
        self.calc_net_accel()
        self.calc_v_final()
        
    
    def calc_net_accel(self):
        mg = self.mass * self.gravity #-981
        propulsion = (self.throttle/100) * self.max_thrust
        self.x_accel = math.cos(self.get_rotation())
        self.y_accel = math.sin(self.get_rotation())
        self.net_accel = mg + propulsion
        
        print("self.accel " , str(self.net_accel) + "m/s^2")
    
    def calc_v_final(self):
        #velocity
        self.v_final = self.v + self.net_accel *  self.time_segment
        self.v = self.v_final
      
        # self.v_final = self.v + self.net_accel* (self.time_elapsed/1000)
        # print("self.time_elapsed(ms)", self.time_elapsed)
        # self.v = self.v_final/10000 #Shot in the dark, the /1000
        # print("v_final", str(self.v_final) + "m/s")
        
    #Needs X and Y components.
    def calc_distance(self):
        #distance
        print("0")
        if (self.y <= self.get_height() and self.v_final < 0):
            print("1")
            self.y = self.get_height()
            self.v = 0
            self.v_final = 0
        else:
            print("2")
            self.y +=(self.y_vel_final * (self.time_segment) + (.5 * self.y_accel * (self.time_segment)**2))

            self.x +=(self.x_vel_final * (self.time_segment) + (.5 * self.x_accel * (self.time_segment)**2))

        return self.y
          #  time.sleep(.2)
        # self.distance = self.v*(self.time_elapsed/1000) + ( .5 * self.net_accel)* (self.time_elapsed/1000)**2
        # print("distance", str(self.distance) + "m")
        # return self.distance
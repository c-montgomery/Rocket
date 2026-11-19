import time
import pygame
import scipy
#projectile

class projectile:
    
    def __init__(self, mass=1, f=0, x=0, y=0, v=0, v_final=0, a=0, g=-9.81):
        self.mass = 1 #kg
        self.f = 1000 #N
        self.x = 0
        self.y = 0
        self.v = 0
        self.v_final = 0
        self.a = 0
        self.g = -9.81
        self.mg = 0
        self.thrust = 1 #kg
        self.throttle = 0
        self.last_time = time.time()
        self.time_segment = 0
        self.time_start = 0
        self.elapsed_total = 0
        self.propulsion = 0
        self.isRunning = True
        

    def output(self, height, mg):
        print()
        print("height " + str(round((self.y),4)))
        print( "throttle " + str(self.throttle))
        print("Propulsion", self.propulsion)
        print("v_initial "+ str(self.v))
        print("v_final "+ str(self.v_final))
        print("net+accel " + str(self.net_accel))
        
        print("====================")

    def manip_throttle(self, val):
         self.throttle = val

    def run(self):
        self.setup()
        #
        output = 0
        while(self.isRunning):
            
           
            self.time_segment = time.time() - self.last_time
            self.elapsed_total = time.time() - self.time_start
            self.last_time = self.time_start + self.elapsed_total

            #Forces
            self.mg = self.mass * self.g
            self.propulsion =  self.thrust * self.throttle 
            
            self.net_accel = self.mg + self.propulsion
            if round(self.elapsed_total, 1) % 1 == 0: #and round(self.elapsed_total,1)> output:
                self.output(self.y,self.mg)
                print(output)
                output+=1
                if self.y >= 60000:
                    
                    self.manip_throttle(1)

            #velocity
            self.v_final = self.v + self.net_accel * (self.time_segment)
            self.v = self.v_final
            self.vector()
            #distance
            if (self.y <= 0 and self.v_final < 0):
                self.y = 0
                self.v = 0
                self.v_final = 0
            else:
                self.y +=(self.v_final * (self.time_segment) + (.5 * self.net_accel * (self.time_segment)**2))
            time.sleep(.2)
            
         

    def setup(self):
        self.manip_throttle(15)
        self.time_start = time.time()


flying_rock = projectile()
flying_rock.setup()
flying_rock.run()
flying_rock.vector()
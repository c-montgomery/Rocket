import time

#projectile

class projectile:
    
    def __init__(self, mass=1, f=0, x=0, y=0, v=0, v_final=0, a=0, g=-9.81):
        self.mass = 1 #kg
        self.f = 0
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
        

    def output(self, height, mg):
        print()
        print( "throttle " + str(self.throttle))
        print( "mass x grav " + str(self.mg))
        print(self.y)
        print("height " + str(round((1000 *self.y),4)))
        print("v_initial "+ str(self.v))
        print("v_final "+ str(self.v_final))
        print("net+accel " + str(self.net_accel))
      #print("====================")

    def manip_throttle(self, val):
         self.throttle = val

    def run(self):
        self.setup()
        #
        while(True):
            self.time_segment = time.time() - self.last_time
            self.elapsed_total = time.time() - self.time_start
            self.last_time = self.time_start + self.elapsed_total

            #Forces
            self.mg = self.mass * self.g
            self.propulsion =  self.thrust * self.throttle 
            self.net_accel = self.mg + self.propulsion
            if round(self.elapsed_total, 1) % .50 == 0:
                self.output(self.y,self.mg)

            #velocity
            self.v_final = self.v + self.net_accel * (self.time_segment)
            self.v = self.v_final

            #distance
            self.y = self.v_final * (self.time_segment) + (.5 * self.net_accel * (self.time_segment)**2)
            


            

    def setup(self):
        self.manip_throttle(10)
        self.time_start = time.time()


flying_rock = projectile()
flying_rock.setup()
flying_rock.run()
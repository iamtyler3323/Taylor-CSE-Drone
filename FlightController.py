__author__ = 'Tyler'
from random import *

class Hover:
    def __init__(self, target, start_throttle):
        self.target = target
        self.throttle = start_throttle

    def get_target(self):
        return self.target

    def set_target(self, new_target):
        self.target = new_target

    def get_alt(self):
        return self.alt

    def get_speed(self):
        return self.speed

    def set_speed(self, speed):
        self.speed = speed

    def set_alt(self, alt):
        self.alt = alt

    def get_direction_vertspeed(self):
        if self.speed < 0:
            return "DOWN"
        elif self.speed > 0:
            return "UP"
        else:
            return "STABLE"

    def update(self, alt, speed):
        self.set_speed(speed)
        self.set_alt(alt)


class VertSpeed:
    def __init__(self, hover_class, debug):
        self.hover = hover_class
        self.debug = debug

    def update(self, cs):
        self.hover.update(cs.alt, cs.verticalspeed)
        self.p("\t\tThrottle: {0}\n\t\tDirection: {1}".format(self.hover.throttle, self.hover.get_direction_vertspeed()))
        if self.hover.get_direction_vertspeed() == "UP":
            if self.hover.get_target() < self.hover.get_alt():
                self.p("\t\tUpdating throttle...\n\t\tOld throttle: {}".format(self.hover.throttle))
                self.hover.throttle -= self.hover.get_speed()
                self.p("\t\tNew throttle: {}".format(self.hover.throttle))
            else:
                self.p("\t\tGoing up, keep her steady!\n\t\tAltitude: {0}\n\t\tDirection: {1}\n\t\tThrottle: {2}".format(self.hover.get_alt(), self.hover.get_direction_vertspeed(), self.hover.throttle))
        elif self.hover.get_direction_vertspeed() == "DOWN":
            if self.hover.get_target() > self.hover.get_alt():
                self.p("\t\tUpdating throttle...\n\t\tOld throttle: {}".format(self.hover.throttle))
                self.hover.throttle += self.hover.get_speed()
                self.p("\t\tNew throttle: {}".format(self.hover.throttle))
            else:
                self.p("\t\tGoing down, keep her steady!\n\t\tAltitude: {0}\n\t\tDirection: {1}\n\t\tThrottle: {2}".format(self.hover.get_alt(), self.hover.get_direction_vertspeed(), self.hover.throttle))
        elif self.hover.get_direction_vertspeed() == "STABLE":
            if self.hover.get_target() < self.hover.get_alt():
                self.p("\t\tUpdating throttle...\n\t\tOld throttle: {}".format(self.hover.throttle))
                self.hover.throttle -= 5
                self.p("\t\tNew throttle: {}".format(self.hover.throttle))
            elif self.hover.get_target() > self.hover.get_alt():
                self.p("\t\t\t\tUpdating throttle...\n\t\t\t\tOld throttle: {}".format(self.hover.throttle))
                self.hover.throttle += 5
                self.p("\t\t\t\tNew throttle: {}".format(self.hover.throttle))

    def p(self, string):
        if self.debug is True:
            print(string)




# Hover types
#   Vertical Speed hover: 0
#   Trending Hover: 1 - NOT IMPLEMENTED
#   Basic Altitude Hover(Not the best): 2 - NOT IMPLEMENTED

hover_type = 0

hover_class = Hover(1.0, 1500)
if hover_type == 0:
    hover = VertSpeed(hover_class, True)


for chan in range(1,9):
    Script.SendRC(chan,1500,False)
Script.SendRC(3,Script.GetParam('RC3_MIN'),True)

Script.Sleep(4000)
if cs.lat != 0:
    print('We got a  GPS signal!')
print('Lowering throttle voltage')
Script.SendRC(3,1000,False)
Script.SendRC(4,2000,True)
cs.messages.Clear()
print('Waiting for motors to be armed...')
Script.WaitFor('ARMING MOTORS', 5000)
print('Motors armed.')

ground_alt = cs.alt
target_altitude = ground_alt + 1
print('Ground alt: {0} | Target alt: {1}'.format(ground_alt,target_altitude))

#Setting yaw to not turn
Script.SendRC(4,1500,True) # 1000 - turn left 2000 - turn right

Script.SendRC(3,1500,True)

while cs.sonarrange < hover_class.get_target():
    Script.Sleep(50)
    Script.SendRC(3,1370,True)

for i in range(0,600):
    print("Run {}".format(i))
    cs.alt = randint(0,20)
    cs.verticalspeed = randint(-3,3)
    print("\tAlt: {0} \n\tVertical Speed: {1}".format(cs.alt, cs.verticalspeed))
    hover.update(cs)
    Script.SendRC(3,hover.hover.throttle,True)
    Script.Sleep(100)
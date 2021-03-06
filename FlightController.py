__author__ = 'Tyler'
from math import *

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
        if cs.alt >= 3:
            self.hover.update(cs.alt, cs.verticalspeed)
        else:
            self.hover.update(cs.sonarrange, cs.verticalspeed)
        self.p("\t\tThrottle: {0}\n\t\tDirection: {1}".format(self.hover.throttle, self.hover.get_direction_vertspeed()))
        if self.hover.get_direction_vertspeed() == "UP":
            if self.hover.get_target() < self.hover.get_alt():
                self.p("\t\tUpdating throttle...\n\t\tOld throttle: {}".format(self.hover.throttle))
                self.hover.throttle -= self.hover.get_speed() * 5
                self.p("\t\tNew throttle: {}".format(self.hover.throttle))
            else:
                self.p("\t\tGoing up, keep her steady!\n\t\tAltitude: {0}\n\t\tDirection: {1}\n\t\tThrottle: {2}".format(self.hover.get_alt(), self.hover.get_direction_vertspeed(), self.hover.throttle))
        elif self.hover.get_direction_vertspeed() == "DOWN":
            if self.hover.get_target() > self.hover.get_alt():
                self.p("\t\tUpdating throttle...\n\t\tOld throttle: {}".format(self.hover.throttle))
                self.hover.throttle += self.hover.get_speed() * 7
                self.p("\t\tNew throttle: {}".format(self.hover.throttle))
            else:
                self.p("\t\tGoing down, keep her steady!\n\t\tAltitude: {0}\n\t\tDirection: {1}\n\t\tThrottle: {2}".format(self.hover.get_alt(), self.hover.get_direction_vertspeed(), self.hover.throttle))
        elif self.hover.get_direction_vertspeed() == "STABLE":
            if self.hover.get_target() < self.hover.get_alt():
                self.p("\t\tUpdating throttle...\n\t\tOld throttle: {}".format(self.hover.throttle))
                self.hover.throttle -= 10
                self.p("\t\tNew throttle: {}".format(self.hover.throttle))
            elif self.hover.get_target() > self.hover.get_alt():
                self.p("\t\t\t\tUpdating throttle...\n\t\t\t\tOld throttle: {}".format(self.hover.throttle))
                self.hover.throttle += 15
                self.p("\t\t\t\tNew throttle: {}".format(self.hover.throttle))

    def p(self, string):
        if self.debug is True:
            print(string)

class Turn:
    
    def __init__(self):
        pass

    def turnTo(self, cs, dir, timeout):
        while (not (dir is self.direction(cs))) or timeout <= 0:
            #cs.yaw += randint(0,40)
            #Script.SendRC(4,2000,True)
            #Script.Sleep(500)
            timeout -= 100
            Script.Sleep(100)
            print("Need to face {0} and currently facing {1}".format(dir, self.direction(cs)))
        print("Hit direction or timout.")
        Script.SendRC(4,1500,True)

    def get_dir_to(self, lat1, long1, lat2, long2):
        margin = pi/90; # 2 degree tolerance for cardinal directions
        o = lat1 - lat2;
        a = long1 - long2;
        angle = atan2(o, a);

        if -margin < angle < margin:
                return "E"
        elif pi/2 - margin < angle < pi/2 + margin:
                return "N"
        elif pi - margin < angle < -pi + margin:
                return "W"
        elif -pi/2 - margin < angle < -pi/2 + margin:
                return "S"
        if 0 < angle < pi/2:
            return "NE"
        elif pi/2 < angle < pi:
            return "NW"
        elif -pi/2 < angle < 0:
            return "SE"
        else:
            return "SW"

    def direction(self, cs):
        directions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW", "N"]
        x = cs.yaw
        return directions[int(round(((x % 360) / 45)))]


# Hover types
#   Vertical Speed hover: 0
#   Trending Hover: 1 - NOT IMPLEMENTED
#   Basic Altitude Hover(Not the best): 2 - NOT IMPLEMENTED

hover_type = 0

hover_class = Hover(1.0, 1500)
if hover_type == 0:
    hover = VertSpeed(hover_class, True)

print("Start")
# while True:
#     print(Turn().get_dir(cs.lat,cs.lng,10,10))
#     Script.Sleep(100)
#     print("Facing north? {}".format(Turn().is_facing("N", cs)))
#     print("Facing south? {}".format(Turn().is_facing("S",cs)))
#     print("Facing east? {}".format(Turn().is_facing("E",cs)))
#     print("Facing west? {}".format(Turn().is_facing("W",cs)))
#     print("Facing ne? {}".format(Turn().is_facing("NE",cs)))
#     print("Facing se? {}".format(Turn().is_facing("SE",cs)))
#     print("Facing sw? {}".format(Turn().is_facing("SW",cs)))
#     print("Facing nw? {}".format(Turn().is_facing("NW",cs)))
#     print("Direction: {}".format(Turn().d(cs)))
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
#
ground_alt = cs.alt
target_altitude = ground_alt + 1
print('Ground alt: {0} | Target alt: {1}'.format(ground_alt,target_altitude))
#
#Setting yaw to not turn
Script.SendRC(4,1500,True) # 1000 - turn left 2000 - turn right
#
#
print('Lifting off')
for i in range(3,25):
    Script.SendRC(3,1300+(i*10),True)
    hover.hover.throttle = 1300+(i*10)
    print("Throttle: {}".format(1300+(i*10)))
    Script.Sleep(80)
    if cs.sonarrange >= target_altitude:
        i=26
timer = 60000

while timer >= 0:
    #print("Run {}".format(i))
    #print("\tAlt: {0} \n\tVertical Speed: {1}".format(cs.alt, cs.verticalspeed))
    print("{}".format(cs.alt))
    if cs.roll > 3:
        Script.SendRC(1,1450,True)
    elif cs.roll < -3:
        Script.SendRC(1,1550,True)
    else:
        Script.SendRC(1,1500,True)

    if cs.pitch > 3:
        Script.SendRC(2,1450,True)
    elif cs.pitch < -3:
        Script.SendRC(2,1550,True)
    else:
        Script.SendRC(2,1500,True)
    hover.update(cs)
    Script.SendRC(3,hover.hover.throttle,True)
    Script.Sleep(100)
    timer -= 100

print('Descending...')
for i in range(3,15):
    Script.SendRC(3,1530-(i*1),True)
    Script.Sleep(50)
    if cs.alt <= ground_alt+0.1:
        break
Script.SendRC(3,1515,True)
while cs.alt > ground_alt+0.1:
    Script.Sleep(50)
    print('Descent at: {0}'.format(cs.alt))

Script.SendRC(3,1000,False)
Script.SendRC(4,1000,True)
Script.WaitFor('DISARMING MOTORS',30000)
Script.SendRC(4,1500,True)


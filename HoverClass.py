__author__ = 'Tyler'

class Hover:
    def __init__(self,target,start_throttle):
        self.target = target
        self.throttle = start_throttle

    def get_target(self):
        return self.target

    def set_target(self,new_target):
        self.target = new_target

    def get_alt(self):
        return self.alt

    def get_speed(self):
        return self.speed

    def set_speed(self,speed):
        self.speed = speed

    def set_alt(self,alt):
        self.alt = alt

    def get_direction(self):
        if self.speed < 0:
            return "DOWN"
        elif self.speed > 0:
            return "UP"
        else:
            return "STABLE"

    def update(self,alt,speed):
        self.set_speed(speed)
        self.set_alt(alt)
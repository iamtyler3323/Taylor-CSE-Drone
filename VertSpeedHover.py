__author__ = 'Tyler'


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
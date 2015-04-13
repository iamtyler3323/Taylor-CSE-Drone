__author__ = 'Tyler'

class VertSpeed:
    def __init__(self,hover_class,debug):
        self.hover = hover_class
        self.debug = debug

    def update(self,cs):
        self.hover.update(cs.alt,cs.verticalspeed)
        if self.hover.get_direction() == "UP":
            if self.hover.get_target() < self.hover.get_alt():
                self.hover.throttle -= self.hover.get_speed()
            else:
                if self.debug is True:
                    print("Going up, keep her steady!\n\tAltitude: {0}\n\tDirection: {1}\n\tThrottle: {2}".format(self.hover.get_alt(),self.hover.get_direction(),self.hover.throttle))
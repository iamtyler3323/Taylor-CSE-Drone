__author__ = 'tgarcia'
from HoverClass import *
class Trending:
    def __init__(self, hover_class, debug):
        self.hover = hover_class
        self.debug = debug
        self.values = []
    def trend(self):
        up = 0
        down = 0
        same = 0
        prev = self.values[0]
        for i in range(1,len(self.values)):
            item = self.values[i]
            if item > prev:
                up += 1
            elif item < prev:
                down += 1
            else:
                same += 1
        if up > down and up > same:
            return "UP"
        elif down > up and down > same:
            return "DOWN"
        else:
            return "STEADY"

    def update(self, cs):
        if len(self.values) < 10:
            self.values.append(cs.alt)
        else:
            trend = self.trend()
            if self.debug:
                print("Trend: {}".format(trend))
            self.values = []
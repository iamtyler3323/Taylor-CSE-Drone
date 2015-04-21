__author__ = 'Tyler'
from HoverClass import *
from VertSpeedHover import *
from CSFake import *
from random import *

# Hover types
#   Vertical Speed hover: 0
#   Trending Hover: 1 - NOT IMPLEMENTED
#   Basic Altitude Hover(Not the best): 2 - NOT IMPLEMENTED

hover_type = 0

hover_class = Hover(10.0, 1500)
cs = cs()
if hover_type == 0:
    hover = VertSpeed(hover_class, True)


for i in range(0,100):
    print("Run {}".format(i))
    cs.alt = randint(0,20)
    cs.verticalspeed = randint(-3,3)
    print("\tAlt: {0} \n\tVertical Speed: {1}".format(cs.alt, cs.verticalspeed))
    hover.update(cs)
__author__ = 'Tyler'
from HoverClass import *
from VertSpeedHover import *

# Hover types
#   Vertical Speed hover: 0
#   Trending Hover: 1 - NOT IMPLEMENTED
#   Basic Altitude Hover(Not the best): 2 - NOT IMPLEMENTED

hover_type = 0

hover_class = Hover(1.0, 1500)

if hover_type == 0:
    hover = VertSpeed(hover_class, True)
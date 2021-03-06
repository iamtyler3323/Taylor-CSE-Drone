__author__ = 'tgarcia'
from math import *

class Turn:
    def __init__(self):
        pass

    # Turns to given direction. Direction will be one of the following: ["N", "NE", "E", "SE", "S", "SW", "W", "NW", "N"]
    #   cs = CommandScript object
    #   dir = Direction to turn to
    #   timeout = time in milliseconds before timing out and canceling turn
    def turnTo(self, cs, dir, timeout):
        while (not (dir is self.direction(cs))) or timeout <= 0:
            # cs.yaw += randint(0,40)
            #Script.SendRC(4,2000,True)
            #Script.Sleep(500)
            timeout -= 100
            Script.Sleep(100)
            print("Need to face {0} and currently facing {1}".format(dir, self.direction(cs)))
        print("Hit direction or timout.")
        Script.SendRC(4, 1500, True)

    # Output: String of direction needed for target coordinates
    #   lat1 = current latitude
    #   long1 = current longitude
    #   lat2 = target latitude
    #   long2 = target longitude
    def get_dir_to(self, lat1, long1, lat2, long2):
        margin = pi / 90  # 2 degree tolerance for cardinal directions
        o = lat1 - lat2
        a = long1 - long2
        angle = atan2(o, a)

        if -margin < angle < margin:
            return "E"
        elif pi / 2 - margin < angle < pi / 2 + margin:
            return "N"
        elif pi - margin < angle < -pi + margin:
            return "W"
        elif -pi / 2 - margin < angle < -pi / 2 + margin:
            return "S"
        if 0 < angle < pi / 2:
            return "NE"
        elif pi / 2 < angle < pi:
            return "NW"
        elif -pi / 2 < angle < 0:
            return "SE"
        else:
            return "SW"

    # Return direction we are facing
    def direction(self, cs):
        directions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW", "N"]
        x = cs.yaw
        return directions[int(round(((x % 360) / 45)))]


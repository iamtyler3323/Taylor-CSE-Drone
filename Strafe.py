__author__ = 'tgarcia'

class Strafe:
    def __init__(self):
        pass

    def strafe_left(self, time):
        while time >= 0:
            cs.SendRC(1,1400,True)
        cs.SendRC(1,1500,True)

    def strafe_right(self, time):
        while time >= 0:
            cs.SendRC(1,1600,True)
        cs.SendRC(1,1500,True)

    def forward(self, time):
        while time >= 0:
            cs.SendRC(2,1600,True)
        cs.SendRC(2,1500,True)

    def backward(self, time):
        while time >= 0:
            cs.SendRC(2,1400,True)
        cs.SendRC(2,1500,True)
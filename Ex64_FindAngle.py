import math
class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __sub__(self, no):
        x_sub = self.x - no.x
        y_sub = self.y - no.y
        z_sub = self.z - no.z
        return Points(x_sub,y_sub,z_sub)
    def dot(self, no):
        x_dot = self.x*no.x
        y_dot = self.y*no.y
        z_dot = self.z*no.z
        return x_dot+y_dot+z_dot
    def cross(self, no):
        x_cross = self.y*no.z - self.z*no.y
        y_cross = self.z*no.x - self.x*no.z
        z_cross = self.x*no.y - self.y*no.x
        return Points(x_cross,y_cross,z_cross)
    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

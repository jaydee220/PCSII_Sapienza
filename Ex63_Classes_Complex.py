import math
class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        added_real = self.real + no.real
        added_im = self.imaginary + no.imaginary
        return Complex(added_real,added_im)

    def __sub__(self, no):
        sub_real = self.real - no.real
        sub_im = self.imaginary - no.imaginary
        return Complex(sub_real,sub_im)

    def __mul__(self, no):
        mul_real = (self.real*no.real)-(self.imaginary*no.imaginary)
        mul_im = (self.real*no.imaginary) + (self.imaginary*no.real)
        return Complex(mul_real,mul_im)
    def __truediv__(self, no):
        try:
            div_real = ((self.real*no.real + self.imaginary*no.imaginary)/(no.real**2+no.imaginary**2))
            div_im = ((self.imaginary*no.real-self.real*no.imaginary)/(no.real**2+no.imaginary**2))
            return Complex(div_real,div_im)
        except ZeroDivisionError as err:
            print (err)
            return None

    def mod(self):
        mod_real = math.sqrt(self.real**2+self.imaginary**2)
        mod_im = 0
        return Complex(mod_real, mod_im)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result
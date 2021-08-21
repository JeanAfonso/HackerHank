# Classes: Dealing with Complex Numbers
# Olá

import math


class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        rea = self.real + no.real
        ima = self.imaginary + no.imaginary
        return Complex(rea, ima)

    def __sub__(self, no):
        rea = self.real - no.real
        ima = self.imaginary - no.imaginary
        return Complex(rea, ima)

    def __mul__(self, no):
        rea = self.real * no.real - self.imaginary * no.imaginary
        ima = self.real * no.imaginary + self.imaginary * no.real
        return Complex(rea, ima)

    def __truediv__(self, no):
        denominator = no.real * no.real + no.imaginary * no.imaginary
        rea_num = (self.real * no.real + self.imaginary * no.imaginary) / denominator
        ima_num = (self.imaginary * no.real - self.real * no.imaginary) / denominator
        return Complex(rea_num, ima_num)

    def mod(self):
        return Complex(math.sqrt(self.real ** 2 + self.imaginary ** 2), 0)

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


if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x + y, x - y, x * y, x / y, x.mod(), y.mod()]), sep='\n')
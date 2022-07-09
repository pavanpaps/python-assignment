import math

class ComplexNum:

    def __init__(self):
        self.real = float(input('Enter the real value: '))
        self.img = float(input('Enter the imaginary value: '))

    def absolute(self):
        abs = math.sqrt(self.real ** 2 + self.img ** 2)
        return abs

    def __add__(self, A):
        return complex(A.real + self.real, A.img + self.img)

    def __mul__(self, A):
        return complex(A.real * self.real - A.img * self.img, A.real
                       * self.img + A.img * self.real)

def main():
    c1 = ComplexNum()
    c2 = ComplexNum()
    print ('Product of complex numbers = ', c1 * c2)
    print ('Sum of the complex numbers =', c1 + c2)

if __name__ == '__main__':
    main()
import math
class QuadraticEquation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def discriminant(self):
        return ((self.b)**2) - (4 * self.a * self.c)

    def root1(self):
        if self.discriminant() < 0:
            return None
        else:
            return (-self.b + math.sqrt(self.discriminant())) / (2 * self.a)

    def root2(self):
        if self.discriminant() < 0:
            return None
        else:
            return (-self.b - math.sqrt(self.discriminant())) / (2 * self.a)
if __name__ == "__main__":
    p1 = QuadraticEquation(1,0,-9)
    print (p1.root1())
    print (p1.root2())
    print (p1.discriminant())


"""
The line if __name__ == "__main__":
tells the program that the code inside this
if statement should only be executed if the
program is executed as a standalone program.
It will not be executed if the program is imported as a module.


"""

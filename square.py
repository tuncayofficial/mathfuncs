import math

class Square:
    def __init__(self, ab, bc, cd, ad):
        self.ab = ab;
        self.bc = bc;
        self.ad = ad;
        self.cd = cd;

    def area(self):
       return print("Area is : " + str(self.ab * self.bc))
    
    def perimeter(self):
        perimeter = 2 * (self.ab + self.bc)
        print("Perimeter is : " + str(perimeter))

    def diagonal(self):
        diagonal = math.floor(math.sqrt(self.ab ** 2 + self.bc **2))
        print("Diagonal is : " + str(diagonal))

    def circleDrawnIntoSquare(self):
        r = self.ab / 2
        length = math.floor(math.pi * 2 * r)
        print("Length of Circle is : " + str(length))

square = Square(4,5,5,4)
square.area()
square.perimeter()
square.diagonal()
square.circleDrawnIntoSquare()
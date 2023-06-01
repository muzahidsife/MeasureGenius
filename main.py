class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width


class Square(Rectangle):
    def __init__(self, length, width):
        super().__init__(length, width)

    def area(self):
        return self.length * self.width


class Cube(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def volume(self):
        return self.height * self.length * self.width


# Input section for Square and area
length = float(input("Enter the length of the square: "))
width = float(input("Enter the width of the square: "))
square = Square(length, width)
print("Area of the square:", square.area())

# Input section for Cube and volume
length = float(input("Enter the length of the cube: "))
width = float(input("Enter the width of the cube: "))
height = float(input("Enter the height of the cube: "))
cube = Cube(length, width, height)
print("Volume of the cube:", cube.volume())

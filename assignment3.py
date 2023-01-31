class Shape:
    def __init__(self, color):
        self.color = color

    def area(self):
        pass

class Square(Shape):
    def __init__(self, color, side_length):
        super().__init__(color)
        self.side_length = side_length

    def area(self):
        return self.side_length**2

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2

square = Square("red", 5)
print("Square area:", square.area(), "color:", square.color)

circle = Circle("blue", 3)
print("Circle area:", circle.area(), "color:", circle.color)

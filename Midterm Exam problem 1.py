class Circle:
    def __init__(self, radius):
        self.radius = radius
        import math
        self.pi = math.pi

    def area(self):
        return self.pi * self.radius ** 2

    def perimeter(self):
        return 2 * self.pi * self.radius

    def display(self):
        print("Area:", round(self.area(),2))
        print("Perimeter:", round(self.perimeter(),2))


circle = Circle(float(input("Enter a Measurement: ")))
circle.display()
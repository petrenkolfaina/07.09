class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height =height

    def square(self):
        print(f"Square: {self.width * self.height}")

    def perimeter(self):
        print(f"Perimeter: {(self.height+ self.width)*2}")

    def showinfo(self):
        self.square()
        self.perimeter()

obj1 =Rectangle(17,25)
obj1.showinfo()
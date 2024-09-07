class Shape:
    def area(self):
        raise NotImplementedError("Subclasses should implement this method")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2


def main():
    try:
        shape = int(input("Enter 1 for Rectangle, 2 for Triangle, 3 for Square, 4 for Circle: "))
        
        if shape == 1:
            length = float(input("Enter Length: "))
            width = float(input("Enter Width: "))
            if length <= 0 or width <= 0:
                raise ValueError("Dimensions must be positive numbers.")
            rectangle = Rectangle(length, width)
            print(f'Area of Rectangle: {rectangle.area()}')

        elif shape == 2:
            base = float(input("Enter Base: "))
            height = float(input("Enter Height: "))
            if base <= 0 or height <= 0:
                raise ValueError("Dimensions must be positive numbers.")
            triangle = Triangle(base, height)
            print(f'Area of Triangle: {triangle.area()}')

        elif shape == 3:
            length = float(input("Enter Length: "))
            if length <= 0:
                raise ValueError("Length must be a positive number.")
            square = Square(length)
            print(f'Area of Square: {square.area()}')

        elif shape == 4:
            radius = float(input("Enter Radius: "))
            if radius <= 0:
                raise ValueError("Radius must be a positive number.")
            circle = Circle(radius)
            print(f'Area of Circle: {circle.area()}')

        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

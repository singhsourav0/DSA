class areas:
    def __init__(self, radius, Length, Width, height, base):
        self.Length = Length
        self.Width = Width
        self.height = height
        self.base = base
        self.radius = radius


    def rectangle(length, width):
        area = length*width
        return area
    
    def triangle(base, height):
        area = 0.5*base*height
        return area
    
    def square(length):
        return length*length
    
    def circle(radius):
        area = 3.14*radius*radius
        return area
    

def main():

    shape = int(input("Enter 1, 2, 3 or 4 for Area of Rectangle, Triangle, Square, Circle respectively: "))
    if shape == 1:
        length = int(input("Enter Length: "))
        width = int(input("Enter Width: "))

        area =areas.rectangle(length, width)
        print(area)

    elif shape == 2:
        base = int(input("Enter Base: "))
        height = int(input("Enter Height: "))
        area =areas.triangle(base, height)
        print(area)

    elif shape == 3:
        length = int(input("Enter Length: "))
        area =areas.square(length)
        print(area)

    elif shape == 4:
        radius = int(input("Enter Radius: "))

        area =areas.circle(radius)
        print(f'the Area of Circle is: {area}')

    else:
        print("Tu smja nhi... tu nhi smja")

if __name__ =="__main__":
    main()


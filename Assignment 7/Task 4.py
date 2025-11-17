class Rectangle:

    def __init__(self, length, width):

        self.length = length

        self.width = width



# Taking user input

length = float(input("Enter length: "))

width = float(input("Enter width: "))



r = Rectangle(length, width)

print("Length:", r.length)

print("Width:", r.width)

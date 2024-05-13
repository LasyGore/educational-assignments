

class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__sides = list(sides) if len(sides) == self.sides_count else [1] * self.sides_count
        self.__color = color
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(0 <= c <= 255 for c in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def set_sides(self, *sides):
        if self.__is_valid_sides(*sides):
            self.__sides = list(sides)

    def __is_valid_sides(self, *sides):
        return all(isinstance(side, int) and side > 0 for side in sides) and len(sides) == self.sides_count

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, radius):
        super().__init__(color, radius)
        self.__radius = radius

    def get_square(self):
        return 3.14 * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__height = 6  # assuming a default height for demonstration purposes

    def get_square(self):
        # Assuming Heron's formula to calculate triangle area
        a, b, c = self.__sides  # assuming the sides provided are correct for a triangle
        s = (a + b + c) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, side_length):
        super().__init__(color, side_length)
        self.__sides = [side_length] * self.sides_count

    def get_volume(self):
        return self.__sides[0] ** 3


# Testing the code
circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)
triangle1 = Triangle((180,160,210), 3,4,5)

circle1.set_color(55, 66, 77)
cube1.set_color(300, 70, 15)
print('1 - ', circle1.get_color())
print('2 - ', cube1.get_color())

cube1.set_sides(5, 3, 12, 4, 5)
circle1.set_sides(15)
print('3 - ', cube1.get_volume())
print('4 - ', circle1.get_square())

print('5 - ', len(circle1))
print('6 - ', cube1.get_volume())

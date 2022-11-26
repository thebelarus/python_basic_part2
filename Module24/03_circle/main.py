import math


class Circle:
    def __init__(self, cordinate_x=0, cordinate_y=0, radius=1):
        self.cordinate_x = cordinate_x
        self.cordinate_y = cordinate_y
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

    def get_perimeter(self):
        return 2 * math.pi * self.radius

    def increase_size(self, mutltiple):
        if mutltiple > 1:
            self.radius *= mutltiple

    def distance_to_another_circle(self, other_circle):
        return math.sqrt(
            (self.cordinate_x - other_circle.cordinate_x)**2
            + (self.cordinate_y - other_circle.cordinate_y)**2
            )

    def is_intersection_with(self, other_circle):
        distance = self.distance_to_another_circle(other_circle)
        if distance < self.radius + other_circle.radius:
            return True
        elif distance == 0 and self.radius == other_circle.radius:
            return True
        elif (distance == self.radius + other_circle.radius
                or distance == abs(self.radius - other_circle.radius)):
            return True
        elif distance > self.radius + other_circle.radius:
            return False
        elif distance < abs(self.radius - other_circle.self.radius):
            return False
        return True

    def __str__(self):
        circle_stats = (
            f'x: {self.cordinate_x}, y:{self.cordinate_y}, '
            f'radius:{self.radius}, area:{self.get_area():.2f}, '
            f'perimeter: {self.get_perimeter():.2f}')
        return circle_stats


def main():
    circle_1 = Circle(1, 1, 3)
    circle_2 = Circle(5, 5, 4)
    intersection_result = circle_1.is_intersection_with(circle_2)
    if intersection_result:
        print('Окружности пересекаются')
    else:
        print('Окружности не пересекаются')
    print(circle_1)
    circle_1.increase_size(3)
    print(circle_1)


if __name__ == '__main__':
    main()

import math


class Car:
    def __init__(self, coordinate_x, coordinate_y):
        self.__coordinate_x = coordinate_x
        self.__coordinate_y = coordinate_y

    def move(self, distance, angle):
        if not (isinstance(distance, int) and isinstance(angle, int)):
            raise ValueError('Расстояние и угол не целые числа!')
        self.__coordinate_x = self.__coordinate_x + distance * math.cos(angle)
        self.__coordinate_y = self.__coordinate_y + distance * math.sin(angle)
        return distance

    def get_coordinates(self):
        return (self.__coordinate_x, self.__coordinate_y)


class Bus(Car):
    PASSENGER_LIMIT = 20
    PRICE_DISTANCE = 2

    def __init__(self, coordinate_x, coordinate_y, passengers):
        super().__init__(coordinate_x, coordinate_y)
        self.__passengers = passengers
        self.__cash = 0

    def get_cash(self):
        return self.__cash

    def get_passengers_count(self):
        return self.__passengers

    def set_passengers_up(self, count):
        if self.__passengers + count > Bus.PASSENGER_LIMIT:
            raise ValueError('Невозможно посадить столько пассажиров!')
        self.__passengers += count
        return self.get_passengers_count()

    def set_passengers_down(self, count):
        if self.__passengers-count < 0:
            raise ValueError('Слишком много пассажиров для высадки!')
        self.__passengers -= count
        return self.get_passengers_count()

    def move(self, distance, angle):
        super().move(distance, angle)
        self.__cash += distance \
            * Bus.PRICE_DISTANCE \
            * self.get_passengers_count()
        return distance


def main():
    bus = Bus(coordinate_x=0, coordinate_y=0, passengers=10)
    print(f'Координаты автобуса {bus.get_coordinates()}')
    print(f'Заработано: {bus.get_cash()} денег')
    bus.move(distance=10, angle=0)
    print(f'Количество пассажиров в автобусе: {bus.get_passengers_count()}')
    bus.set_passengers_up(5)
    bus.move(distance=15, angle=90)
    print(f'Количество пассажиров в автобусе: {bus.get_passengers_count()}')
    print(f'Заработано: {bus.get_cash()} денег')
    bus.set_passengers_down(15)
    print(f'Количество пассажиров в автобусе: {bus.get_passengers_count()}')
    print(f'Заработано: {bus.get_cash()} денег')
    print(f'Координаты автобуса {bus.get_coordinates()}')


if __name__ == '__main__':
    main()

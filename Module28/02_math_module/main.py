import math


class MyMath:
    @classmethod
    def circle_len(cls, radius: int) -> float:
        '''Вычисление длины окружности.'''
        return 2 * math.pi * radius

    @classmethod
    def circle_sq(cls, radius: int) -> float:
        '''Вычисление площади окружности.'''
        return math.pi * radius ** 2

    @classmethod
    def cube_volume(cls, size: int) -> int:
        '''Вычисление объёма куба.'''
        return size ** 3

    @classmethod
    def sphere_area(cls, radius: int) -> float:
        '''Вычисление площади поверхности сферы.'''
        return 4 * math.pi * radius ** 2

    @classmethod
    def arc_length(cls, radius: int, n_measure: int) -> float:
        '''Вычисление длины дуги окружности.'''
        return (math.pi * radius * n_measure) / 180


def main() -> None:
    res_1 = MyMath.circle_len(radius=5)
    res_2 = MyMath.circle_sq(radius=6)
    res_3 = MyMath.cube_volume(size=5)
    res_4 = MyMath.sphere_area(radius=6)
    res_5 = MyMath.arc_length(radius=6, n_measure=2)
    print('Длина окружности ', res_1)
    print('Площади окружности ', res_2)
    print('Объёма куба ', res_3)
    print('Площадь поверхности сферы ', res_4)
    print('Длина дуги окружности ', res_5)


if __name__ == '__main__':
    main()

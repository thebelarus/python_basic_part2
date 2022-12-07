from collections.abc import Iterable
from typing import Iterator


class SquareGenerator:
    def __init__(self, limit: int) -> None:
        self.__limit = limit
        self.__counter = 0

    def __next__(self) -> int:
        if self.__counter < self.__limit:
            self.__counter += 1
            return self.__counter ** 2
        else:
            raise StopIteration

    def __iter__(self) -> Iterator[int]:
        return self


def square_generator(limit: int) -> Iterable[int]:
    for number in range(limit):
        yield (number + 1) ** 2


def main():
    number_input = int(input('Вводите число N: '))
    print('Класс-итератор')
    square_enerator_class = SquareGenerator(number_input)
    for number in square_enerator_class:
        print(number)
    print('Функция-генератор')
    square_enerator_function = square_generator(number_input)
    for number in square_enerator_function:
        print(number)
    print('Генераторное выражение')
    square_enerator_expression = (
        number ** 2 for number in range(1, number_input + 1))
    for number in square_enerator_expression:
        print(number)


if __name__ == '__main__':
    main()

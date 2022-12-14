from functools import reduce


def main() -> None:
    '''Tестирование кода'''
    floats = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
    names = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
    numbers = [22, 33, 10, 6894, 11, 2, 1]
    new_floats = list(map(lambda number: round(number ** 3, 3), floats))
    new_names = list(filter(lambda name: len(name) >= 5, names))
    new_numbers = reduce(lambda storage, number: storage * number, numbers)
    print(('Каждое число из списка floats возводится в ',
           'третью степень и округляется до трёх знаков после запятой.'))
    print(new_floats)
    print('Имена минимум из пяти букв.')
    print(new_names)
    print('Произведение всех чисел.')
    print(new_numbers)


if __name__ == '__main__':
    main()

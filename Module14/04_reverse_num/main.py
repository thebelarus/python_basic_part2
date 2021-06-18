def make_split_and_reverse_number(number) -> float:
    '''
    Разделение числа на целую и дробную часть с переворотом цифр.

    Возврат число с типом float.
    '''
    part_1, part_2 = str(number).split('.')
    result = '.'.join(
        [
            make_reverse_number(part_1),
            make_reverse_number(part_2),
        ]
    )
    return float(result)


def make_reverse_number(number) -> str:
    '''Переворачивание цифр в числе.

    Возврат тип string.
    '''
    return str(number)[::-1]


if __name__ == '__main__':
    first_number = float(input('Введите первое число: '))
    second_number = float(input('Введите второе число: '))
    first_number_reversed = make_split_and_reverse_number(
        first_number
    )
    second_number_reversed = make_split_and_reverse_number(
        second_number
    )
    sum_of_numbers = first_number_reversed + second_number_reversed
    print(f'Первое число наоборот: {first_number_reversed}')
    print(f'Второе число наоборот: {second_number_reversed}')
    print(f'Сумма: {sum_of_numbers}')

# TODO применить рекомендации данные ранее

def get_fibonacci_number(number_position, value_previous=1, value_second=1):
    values_sum = value_previous + value_second
    value_previous = value_second
    value_second = values_sum
    if number_position <= 3:
        return values_sum
    return get_fibonacci_number(number_position - 1, value_previous, value_second)


def main():
    number_position_input = int(
        input('Введите позицию числа в ряде Фибоначчи: ')
        )
    result = get_fibonacci_number(number_position_input)
    print(f'Число: {result}')


if __name__ == '__main__':
    main()

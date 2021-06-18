def smallest_divisor_of_number(number):
    if number <= 1:
        raise ValueError('Натуральное число меньше или равно 1')
    div_number = 1
    while div_number <= number:
        div_number = div_number + 1
        if number % div_number == 0:
            break
    return div_number


if __name__ == '__main__':
    number_input = int(input('Введите число: '))
    # TODO два раза объявили
    number_input = 6
    result = smallest_divisor_of_number(number_input)
    print(f'Наименьший делитель, отличный от единицы: {result}')

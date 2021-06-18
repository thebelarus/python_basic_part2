def is_three_equal_digits_in_number(number) -> bool:
    """Определяет наличия трех равных цифр в 4-ех значном числе."""
    digits = list(str(number))
    digits_len = len(digits)
    if digits_len != 4:
        raise ValueError('Число не четырехзначное!')
    digits_without_repeat = set(digits)
    if digits_len - len(digits_without_repeat) == 2:
        for item in digits_without_repeat:
            if digits.count(item) == 3:
                return True
    return False


if __name__ == '__main__':
    year_start_input = int(input('Введите первый год: '))
    year_end_input = int(input('Введите второй год: '))
    if year_start_input >= year_end_input:
        raise ValueError('Год начала периода больше года конца периода.')
    for year in range(year_start_input, year_end_input + 1):
        if is_three_equal_digits_in_number(year):
            print(year)

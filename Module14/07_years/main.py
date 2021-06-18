def is_three_equal_digits_in_number(number) -> bool:
    '''Определяет наличия трех равных цифр в 4-ех значном числе.'''
    # TODO list tuple dict set зарезервированные слова не используем их в именовании переменных
    number_list = list(str(number))
    number_list_len = len(number_list)
    if number_list_len != 4:
        raise ValueError('Число не 4-ех значноe!')
    number_list_set = set(number_list)
    if number_list_len - len(number_list_set) == 2:
        for item in number_list_set:
            if number_list.count(item) == 3:
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

# TODO применить рекомендации данные ранее

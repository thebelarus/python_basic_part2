
# TODO Параметры как и имя функции не должны подчеркиваться и пересекаться с глобальными переменными
def calculate_number_of_digits(number):
    '''
    Вычисление количества цифр в числе.
    '''
    return len(list(str(number)))


def calculate_sum_of_digits(number):
    '''
    Вычисление суммы всех цифр числа.
    '''
    return sum([int(x) for x in list(str(number))])


if __name__ == '__main__':
    number = int(input('Введите число: '))
    number_of_digits = calculate_number_of_digits(number)
    print(f'Кол-во цифр в числе: {number_of_digits}')
    sum_of_digits = calculate_sum_of_digits(number)
    print(f'Сумма цифр: {sum_of_digits}')
    difference_of_results = sum_of_digits - number_of_digits
    print(f'Разность суммы и кол-ва цифр: {difference_of_results}')



# TODO Есть недочеты в форматировании по PEP8, используйте пункт меню в пайчарме

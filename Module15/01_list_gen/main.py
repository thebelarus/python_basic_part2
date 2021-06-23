
def generate_odds_numbers(number) -> list:
    if not isinstance(number, int):
        raise ValueError('Требуется целое число!')
    return [item for item in range(number+1) if item % 2 != 0]


def generate_odds_numbers_second_version(number) -> list:
    numbers = [item for item in range(number+1)]
    if not isinstance(number, int):
        raise ValueError('Требуется целое число!')
    return numbers[1::2]


if __name__ == '__main__':
    number_input = int(input('Введите число: '))
    generated_numbers = generate_odds_numbers(number_input)
    print(f'Список нечетных чисел: {generated_numbers}')
    generated_numbers = generate_odds_numbers_second_version(number_input)
    print(f'Список нечетных чисел: {generated_numbers}')

# зачет!

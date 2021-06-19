def generate_odds_numbers(n) -> list:
    if not isinstance(n, int):
        raise ValueError('Требуется целое число!')
    return [x for x in range(n+1) if x % 2 != 0]


def generate_odds_numbers_second_version(n) -> list:
    generated_numbers_l = [x for x in range(n+1)]
    if not isinstance(n, int):
        raise ValueError('Требуется целое число!')
    return generated_numbers_l[1::2]


if __name__ == '__main__':
    number = int(input('Введите число: '))
    print(generate_odds_numbers(number))
    print(generate_odds_numbers_second_version(number))

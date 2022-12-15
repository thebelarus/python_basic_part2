from collections import Counter


def can_be_poly(string: str) -> bool:
    '''Функция которая принимает на вход строку
    и проверяет, можно ли получить из неё палиндром.
    '''
    return sum(
        symbol_entries % 2 for symbol_entries
        in Counter(string).values()
    ) <= 1


def main() -> None:
    '''Tестирование кода'''
    print('Результат:')
    result = can_be_poly('abcba')
    print(result)
    result = can_be_poly('acbb')
    print(result)


if __name__ == '__main__':
    main()

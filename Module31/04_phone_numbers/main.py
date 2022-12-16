import re

REGEX_PHONE = r'[89]{1}\d{9}'


def is_valide_phone(number_string: str) -> bool:
    result = re.match(REGEX_PHONE, number_string)
    if result:
        return True
    return False


def main() -> None:
    '''Tестирование регулярного выражения'''
    print('Результат:')
    phones = ['9999999999', '999999-999', '99999x9999']
    for phone_number in phones:
        print(f'номер {phone_number}: ', end='')
        if is_valide_phone(phone_number):
            print('всё в порядке')
        else:
            print('не подходит')


if __name__ == '__main__':
    main()

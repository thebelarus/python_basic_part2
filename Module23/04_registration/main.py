import datetime


def is_validate_data(data):
    try:
        data_splited = data.split()
        if len(data_splited) != 3:
            raise IndexError('НЕ присутствуют все три поля')
        name, email, age = data_splited
        for char in name:
            if not char.isalpha():
                raise NameError(' Поле «Имя» содержит НЕ только буквы')
        for char in ['.', '@']:
            if char not in email:
                raise SyntaxError('Поле «Имейл» НЕ содержит @ и . (точку)')
        if not (age.isnumeric() and 10 < int(age) < 99):
            raise ValueError('Поле «Возраст» НЕ является числом от 10 до 99')
    except Exception as error:
        return False, error
    else:
        return True, ''


def parse_file(filename='registrations.txt'):
    amount = 0
    try:
        with open(filename, encoding='utf8') as file:
            for line in file.readlines():
                is_valid_data_status, message = is_validate_data(line.strip())
                if is_valid_data_status:
                    write_good_result(line)
                else:
                    write_bad_result(line, message)
    except FileNotFoundError:
        print(f'Файл {filename} не найден!')
    finally:
        return amount


def write_good_result(data, filename='registrations_good.log'):
    with open(filename, 'a', encoding='utf8') as file:
        file.write(data)


def write_bad_result(data, error_message, filename='registrations_bad.log'):
    with open(filename, 'a', encoding='utf8') as file:
        file.write(f'{data.strip()} {error_message}\n')


def main():
    parse_file()


if __name__ == '__main__':
    main()

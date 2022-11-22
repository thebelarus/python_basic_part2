import datetime


def parse_file(filename='people.txt'):
    amount = 0
    try:
        with open(filename, encoding='utf8') as file:
            for line_index, line_value in enumerate(file.readlines()):
                line_length = len(line_value.strip())
                try:
                    if line_length < 3:
                        raise ValueError(
                            f'Ошибка: менее трёх символов \
                                в строке {line_index}.')
                except ValueError as error:
                    print(error)
                    error_to_log(error)
                finally:
                    amount += line_length
    except FileNotFoundError:
        print(f'Файл {filename} не найден!')
    finally:
        return amount


def error_to_log(data, filename='errors.log'):
    with open(filename, 'a', encoding='utf8') as file:
        txt = f"{datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')} \
            {data}\n"
        file.write(txt)


def main():
    result = parse_file()
    print(result)


if __name__ == '__main__':
    main()

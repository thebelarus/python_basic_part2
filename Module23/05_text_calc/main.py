import datetime


def validate_and_count_expression(line):
    operators = ['+', '-', '/', '*', '//', '%']
    try:
        operand_1, operator, operand_2 = line.split()
        operand_1 = int(operand_1)
        operand_2 = int(operand_2)
        if operator not in operators:
            raise ValueError
        if operand_2 == 0 and operator in ['/', '//', '%']:
            raise ZeroDivisionError
        result = eval(f'{operand_1}{operator}{operand_2}')
        return True, result
    except (ValueError, ZeroDivisionError):
        return False, ''


def parse_file(filename='calc.txt'):
    amount = 0
    try:
        with open(filename, encoding='utf8') as file:
            for line in file.readlines():
                line_clean = line.strip()
                result_status, result_value = validate_and_count_expression(
                    line_clean)
                if result_status:
                    amount += result_value
                    continue
                fix_select = input(
                    'Обнаружена ошибка в строке: '
                    f'{line_clean} Хотите исправить? ')
                if fix_select == 'Да':
                    fix_expression_value = input(
                        'Введите исправленную строку: ')
                    (
                        result_status,
                        result_value
                    ) = validate_and_count_expression(
                        fix_expression_value)
                    if result_status:
                        amount += result_value
                    else:
                        print('Обнаружена ошибка в строке: '
                              f'{fix_expression_value}'
                              )
            print(f'Сумма результатов: {amount}')
    except FileNotFoundError:
        print(f'Файл {filename} не найден!')
    finally:
        return amount


def main():
    parse_file()


if __name__ == '__main__':
    main()

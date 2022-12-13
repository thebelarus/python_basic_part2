from datetime import datetime
from functools import wraps
from typing import Any, Callable


def logging(function: Callable) -> Any:
    '''Декоратор для логирования функций. 
    На экран выводится название функции и её документация. 
    Если во время выполнения декорируемой функции возникла 
    ошибка, то в файл `function_errors.log` записываются названия функции и ошибки.
    '''
    @wraps(function)
    def wrapper(*args, **kwargs) -> Any:
        print('Имя функции: ', function.__name__)
        print('Документация: ', function.__doc__)
        try:
            result = function(*args, **kwargs)
            return result
        except Exception as error:
            with open('function_errors.log', 'w', encoding='utf8') as file:
                current_time = datetime.now().strftime("%H:%M:%S")
                file.write((f'{current_time} Функция: {function.__name__}, '
                            f'ошибка: {error}'))
    return wrapper


@logging
def test() -> None:
    '''Test print function'''
    print('<Тут что-то происходит...>')


@logging
def get_multiplication(number_1: int, number_2: int) -> int:
    '''Get multiplication of two numbers'''
    return number_1 * number_2


@logging
def get_division(number_1: int, number_2: int) -> float:
    '''Get division of two numbers'''
    return number_1 / number_2


def main() -> None:
    test()
    multiplication_result = get_multiplication(10, 5)
    print(multiplication_result)
    division_result = get_division(10, 5)
    print(division_result)
    division_error_result = get_division(10, 0)
    print(division_error_result)


if __name__ == '__main__':
    main()

from datetime import datetime
from functools import wraps
from typing import Any, Callable


def counter(function: Callable) -> Any:
    function_base = {}

    @wraps(function)
    def wrapper(*args, **kwargs) -> Any:
        func_name = function.__name__
        if func_name in function_base:
            function_base[func_name] += 1
        else:
            function_base[func_name] = 1
        print(f'Функция вызвана {function_base[func_name]} раз')
        return function(*args, **kwargs)
    return wrapper


@counter
def test() -> None:
    '''Test print function'''
    print('<Тут что-то происходит...>')


@counter
def get_multiplication(number_1: int, number_2: int) -> int:
    '''Get multiplication of two numbers'''
    return number_1 * number_2


@counter
def get_division(number_1: int, number_2: int) -> float:
    '''Get division of two numbers'''
    return number_1 / number_2


def main() -> None:
    test()
    multiplication_result = get_multiplication(10, 5)
    print(multiplication_result)
    division_result = get_division(10, 5)
    print(division_result)
    multiplication_result = get_multiplication(10, 10)
    print(multiplication_result)


if __name__ == '__main__':
    main()

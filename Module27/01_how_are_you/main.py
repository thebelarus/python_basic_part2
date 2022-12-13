from functools import wraps
from typing import Any, Callable


def how_are_you(function: Callable) -> Any:
    '''Декоратор, при вызове декорируемой функции спрашивает
    у пользователя «Как дела?», вне зависимости от ответа
    отвечает что-то вроде «А у меня не очень!» и
    только потом запускает саму функцию
    '''
    @wraps(function)
    def wrapper(*args, **kwargs):
        _ = input('Как дела? ')
        print('А у меня не очень! Ладно, держи свою функцию.')
        return function(*args, **kwargs)
    return wrapper


@how_are_you
def test():
    print('<Тут что-то происходит...>')


@how_are_you
def get_multiple(number_1: int, number_2: int):
    return number_1 + number_2


def main() -> None:
    test()
    result = get_multiple(10, 5)
    print(result)


if __name__ == '__main__':
    main()

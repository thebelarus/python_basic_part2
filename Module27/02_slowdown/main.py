import random
import time
from functools import wraps
from typing import Any, Callable


def slowly(function: Callable) -> Any:
    '''Декоратор, который перед выполнением декорируемой 
    функции ждёт несколько секунд.
    '''
    @wraps(function)
    def wrapper(*args, **kwargs):
        random_number = random.randint(2, 5)
        time.sleep(random_number)
        return function(*args, **kwargs)
    return wrapper


@slowly
def test():
    print('<Тут что-то происходит...>')


@slowly
def get_multiplication(number_1: int, number_2: int):
    return number_1 * number_2


def main() -> None:
    test()
    result = get_multiplication(10, 5)
    print(result)


if __name__ == '__main__':
    main()

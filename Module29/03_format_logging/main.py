import functools
import time
from datetime import datetime


def timer(cls, function, date_format):
    '''Декоратор для вывода даты и времени запуска фунцки'''
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        date_format_fixed = ''
        for symbol in date_format:
            if symbol.isalpha():
                date_format_fixed += f'%{symbol}'
            else:
                date_format_fixed += symbol
        datetime_string = datetime.now().strftime(date_format_fixed)
        print(
            (
                f'- Запускается \'{cls.__name__}.{function.__name__}.\' '
                f'Дата и время запуска: {datetime_string}'))
        start_time = time.time()
        result = function(*args, **kwargs)
        elapsed_time = round(time.time() - start_time, 3)
        print(
            (f'- Завершение \'{cls.__name__}.{function.__name__}\'',
             f', время работы = {elapsed_time}s '))
        return result
    return wrapper


def log_methods(datetime_format: str):
    '''Декоратор для логирования всех методов декорируемого класса'''
    def decorate(cls):
        for method_name in dir(cls):
            if method_name.startswith('__') is False:
                current_method = getattr(cls, method_name)
                decorated_method = timer(cls, current_method, datetime_format)
                setattr(cls, method_name, decorated_method)
        return cls
    return decorate


@log_methods("b d Y - H:M:S")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods("b d Y - H:M:S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


def main() -> None:
    '''Tестирование класса'''

    my_obj = B()
    my_obj.test_sum_1()
    my_obj.test_sum_2()


if __name__ == '__main__':
    main()

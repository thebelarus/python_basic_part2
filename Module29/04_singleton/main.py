from typing import Callable, Type


def singleton(cls) -> Callable:
    '''Декоратор, превращает класс в одноэлементный экземпляр.'''
    def wrappper(*args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = cls(*args, **kwargs)
        return cls.instance
    return wrappper


@singleton
class Example:
    pass


def main() -> None:
    '''Tестирование класса'''

    my_obj = Example()
    my_another_obj = Example()
    print(id(my_obj))
    print(id(my_another_obj))
    print(my_obj is my_another_obj)


if __name__ == '__main__':
    main()

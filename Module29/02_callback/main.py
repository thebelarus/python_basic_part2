from typing import Any, Callable, Dict
import functools


class App:
    '''Класс приложения веб-сервиса.'''
    routes: Dict[str, Callable[[Any], str]] = {}

    @classmethod
    def get(cls, route_name: str) -> Callable:
        '''Получение функции роутинга.'''
        return cls.routes.get(route_name, False)


def callback(route: str) -> Callable:
    '''Декоратор обратного вызова.'''
    def wrapper_outer(function: Callable) -> Callable:
        App.routes[route] = function

        @functools.wraps(function)
        def wrapper_inner(*args, **kwargs) -> Any:
            return function(*args, **kwargs)
        return wrapper_inner
    return wrapper_outer


@callback('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


def main() -> None:
    '''Tестирование класса'''
    app = App()
    route = app.get('//')
    if route:
        response = route()
        print('Ответ:', response)
    else:
        print('Такого пути нет')


if __name__ == '__main__':
    main()

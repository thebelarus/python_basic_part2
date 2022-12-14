import functools
from typing import Any, Callable

user_permissions = ['admin']


def check_permission(user: str) -> Callable:
    '''
    Декоратор который проверяет,
    есть ли у пользователя доступ к вызываемой функции,
    и если нет, то выдаёт исключение PermissionError.
    '''
    def wrapper_outer(function: Callable) -> Callable:
        @functools.wraps(function)
        def wrapper_inner(*args, **kwargs) -> Any:
            if user not in user_permissions:
                raise PermissionError(
                    ('У пользователя недостаточно прав, ',
                     'чтобы выполнить функцию {}'.format(
                         function.__name__
                     ))
                )
            return function(*args, **kwargs)
        return wrapper_inner
    return wrapper_outer


@check_permission('admin')
def delete_site():
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


def main() -> None:
    '''Tестирование декоратора'''
    delete_site()
    add_comment()


if __name__ == '__main__':
    main()

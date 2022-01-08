"""Task 3 solution."""
from typing import Tuple
from functools import reduce


def search(array, detail) -> Tuple[int, int]:
    '''Search detail in shop.'''
    filtered_array = list(filter(lambda a: a[0] == detail, array))
    if not filtered_array:
        raise ValueError('Ошибка! Деталь не найдена!')
    amount = reduce(lambda a, b: a + b[1], filtered_array, 0)
    return len(filtered_array), amount


if __name__ == '__main__':
    shop = [
        ['каретка', 1200], ['шатун', 1000],
        ['седло', 300], ['педаль', 100],
        ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200],
        ['седло', 2700]
        ]

    search_param = input('Название детали: ')
    detail_count, detail_amount = search(shop, search_param)
    print(f'Кол-во деталей - {detail_count}')
    print(f'Общая стоимость - {detail_amount}')

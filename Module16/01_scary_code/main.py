"""Task 1 solution."""
from typing import List


def calc_num_in_array(array: List[int], num: int) -> int:
    ''' Calculate num count in array.'''
    return array.count(num)


if __name__ == '__main__':
    array_main: List[int] = [1, 5, 3]
    array_second: List[int] = [1, 5, 1, 5]
    array_third: List[int] = [1, 3, 1, 5, 3, 3]
    array_main.extend(array_second)
    five_num_count_result = calc_num_in_array(array_main, 5)
    array_main = list(filter(lambda item: item != 5, array_main))
    array_main.extend(array_third)
    three_num_count_result = calc_num_in_array(array_main, 3)
    print(f'Кол-во цифр 5 при первом объединении: {five_num_count_result}')
    print(f'Кол-во цифр 3 при втором объединении: {three_num_count_result}')
    print(f'Итоговый список: {array_main}')

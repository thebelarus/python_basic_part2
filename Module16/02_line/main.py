"""Task 2 solution."""
from typing import List


def generate_classmate(low: int, high: int, step: int) -> List[int]:
    '''Generate classmate'''
    result = []
    for item in range(low, high + 1, step):
        result.append(item)
    return result


if __name__ == '__main__':
    classmate_one = generate_classmate(160, 176, 2)
    classmate_two = generate_classmate(162, 180, 3)
    classmate_one.extend(classmate_two)
    classmate_one.sort()
    print(classmate_one)

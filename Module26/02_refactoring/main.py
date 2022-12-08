from collections.abc import Iterable


def number_finder(
        list_1_value: list[int],
        list_2_value: list[int],
        to_find_value: int
        ) -> Iterable[str]:
    for x in list_1_value:
        for y in list_2_value:
            result = x * y
            yield f'{x} {y} {result}'
            if result == to_find_value:
                yield 'Found!!!'
                return


def main() -> None:
    list_1 = [2, 5, 7, 10]
    list_2 = [3, 8, 4, 9]
    to_find = 56
    for number in number_finder(list_1, list_2, to_find):
        print(number)


if __name__ == '__main__':
    main()

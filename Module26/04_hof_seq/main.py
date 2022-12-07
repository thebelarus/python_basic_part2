from typing import Iterator


class QHofstadter:
    def __init__(self, array: list[int] = [1, 1]) -> None:
        if not (
            isinstance(array, list)
            and len(array) == 2
            and array != [1, 2]
        ):
            raise ValueError(
                (
                    'Ошибка! Последовательность не '
                    f'совпадает с условием или равна {array}!'
                )
            )
        self.__sequence = array
        self.__counter = 2

    def __next__(self) -> list[int]:
        self.__counter += 1
        new_data = self.__sequence[
            self.__counter - self.__sequence[
                self.__counter - 2] - 1] + self.__sequence[
                    self.__counter - self.__sequence[
                        self.__counter - 3
                        ] - 1]
        self.__sequence.append(new_data)
        return self.__sequence

    def __iter__(self) -> Iterator[list[int]]:
        return self


def main() -> None:
    hofstadter_genertor = QHofstadter([1, 1])
    for _ in range(10):
        result_array = next(hofstadter_genertor)
        print(result_array)


if __name__ == '__main__':
    main()

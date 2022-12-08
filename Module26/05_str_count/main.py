import os
from collections.abc import Iterable


def is_valid_row(row: str) -> bool:
    row_stiped = row.strip()
    if row_stiped.startswith('#') or len(row_stiped) == 0:
        return False
    return True


def read_file_and_count_rows(path: str) -> int:
    with open(path, encoding='utf8') as file:
        row_count = 0
        for row in file.readlines():
            if is_valid_row(row):
                row_count += 1
        return row_count


def py_parser(path: str = '.') -> Iterable[str]:
    row_in_all_count = 0
    for root, _, files in os.walk(path):
        for file in files:
            if not file.endswith('.py'):
                break
            row_count = read_file_and_count_rows(os.path.join(root, file))
            row_in_all_count += row_count
            yield (
                f'В файле {file} {row_count} строк кода. '
                f'Всего в директории {row_in_all_count} строк кода'
                )


def main() -> None:
    parser_generator = py_parser('.')
    for result in parser_generator:
        print(result)


if __name__ == '__main__':
    main()

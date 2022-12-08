import os
from collections.abc import Iterable


def gen_files_path(to_find_directory: str, path: str = "/") -> Iterable[str]:
    for root, _, files in os.walk(path):
        if root == to_find_directory:
            yield f"Каталог {to_find_directory} найден!"
            return
        for filename in files:
            yield root+filename


def main() -> None:
    for file_path in gen_files_path('2023', "C:\\"):
        print(file_path)


if __name__ == '__main__':
    main()

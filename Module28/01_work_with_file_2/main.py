from typing import TextIO, Union


class File:
    def __init__(self, name: str) -> None:
        '''Конструктор класса'''
        self.name = name
        self.file: Union[TextIO, None] = None

    def __enter__(self) -> TextIO:
        '''Инициализации контекста'''
        try:
            self.file = open(self.name, encoding='utf8')
        except:
            self.file = open(self.name, 'w', encoding='utf8')
        finally:
            return self.file

    def __exit__(self, ex_type, ex_value, ex_traceback) -> bool:
        '''Выход из контекста'''
        self.file.close()
        return True


def main() -> None:
    with File('1.txt') as file:
        file.write('sss')
    with File('2.txt') as file:
        file.read()


if __name__ == '__main__':
    main()

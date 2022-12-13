class Date:
    months_days = {
        '1': 31,
        '2': 28,
        '3': 31,
        '4': 30,
        '5': 31,
        '6': 30,
        '7': 31,
        '8': 31,
        '9': 30,
        '10': 31,
        '11': 30,
        '12': 31,
    }

    def __init__(self, day: int = 0, month: int = 0, year: int = 0) -> None:
        '''Конструктор класса'''
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        '''Функция преобразования класа в строку'''
        return f'День: {self.day}\tМесяц: {self.month}\tГод: {self.year}'

    @classmethod
    def from_string(cls, string: str) -> 'Date':
        '''Функция рреобразование строки в класс Date.'''
        if cls.is_date_valid(string):
            day, month, year = [int(item) for item in string.split('-')]
            return cls(day, month, year)
        raise ValueError('Строка не является валидной для создания объекта Date')

    @classmethod
    def is_date_valid(cls, string: str) -> bool:
        '''Функция проверки коректности даты c учетом высокосного года.'''
        try:
            day, month, year = [int(item) for item in string.split('-')]
            if year <= 0:
                return False
            if not str(month) in cls.months_days.keys():
                return False
            if not (
                    day in range(1, cls.months_days[str(month)] + 1)
                    or year % 4 == 0 and day == 29):
                return False
            return True
        except ValueError:
            return False


def main() -> None:
    '''Tестирование класса'''
    date = Date.from_string('10-12-2077')
    print(date)
    print(Date.is_date_valid('10-12-2077'))
    print(Date.is_date_valid('а0-12-2077'))
    print(Date.is_date_valid('29-02-2024'))
    print(Date.is_date_valid('29-02-2025'))

if __name__ == '__main__':
    main()

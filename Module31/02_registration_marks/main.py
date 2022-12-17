import re
from typing import List

symbols = ['А', 'В', 'Е', 'К', 'М', 'Н', 'О', 'Р', 'С', 'Т', 'У', 'Х']
symbols_str = ''.join(symbols)
REGEX_EXPRESSION_CARS = r'[' + symbols_str + \
    r']{1}\d{3}[' + symbols_str + r']{2}\d{2,3}'
REGEX_EXPRESSION_TAXI = r'[' + symbols_str + r']{2}\d{3}\d{2,3}'


def main() -> None:
    '''Tестирование регулярного выражения'''
    text = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'
    results_cars: List[str] = re.findall(REGEX_EXPRESSION_CARS, text)
    results_taxi: List[str] = re.findall(REGEX_EXPRESSION_TAXI, text)
    print('Результат:')
    print(f'писок номеров частных автомобилей: {results_cars}')
    print(f'Список номеров такси: {results_taxi}')  # ['ОР233787', 'СТ46599']


if __name__ == '__main__':
    main()

import requests
from typing import List, Tuple, Union
import time
API_URL = 'https://swapi.dev/api/'


def get_births_days_from_api(url: str) -> Tuple[bool, Union[List[float], str]]:
    '''Функция загрузки дней рождения персонажей на основание цвета
    волос(blond) и количесва участия в более 2-ух фильмах.'''
    endpoint = url + 'people'
    characters: List[float] = []
    try:
        while True:
            response = requests.get(endpoint)
            dataset = response.json()
            for character in dataset['results']:
                if (character["hair_color"] == "blond"
                        and len(character["films"])) >= 2:
                    birth_year = float(character["birth_year"][:-3])
                    characters.append(birth_year)
            if dataset["next"]:
                endpoint = dataset["next"]
                time.sleep(2)
            else:
                break
        return True, characters
    except requests.ConnectionError:
        return False, ''


def average_count(data: List[Union[int, float]]) -> float:
    '''Функция расчета среднего арифметического на наборе
    данных чисел упакованных в List'''
    return sum(data) / len(data)


def main() -> None:
    '''Tестирование приложения'''
    print('Результат:')
    url = API_URL
    get_status, dataset = get_births_days_from_api(url)
    if get_status and dataset:
        average_birth = average_count(dataset)
        print('Среднее значение: ', average_birth)
    elif get_status:
        print('Допустимых данных отвечающим условию нет.')
    else:
        print('Не удалось загрузить данные с {}'.format(
            url
        ))


if __name__ == '__main__':
    main()

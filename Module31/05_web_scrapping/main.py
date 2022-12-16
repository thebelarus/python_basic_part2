import re
import requests
from typing import List, Tuple


def get_page(url: str) -> Tuple[bool, str]:
    '''Функция загрузки веб-страницы и возврата результат в виде текста.'''
    try:
        response = requests.get(url)
        return True, response.text
    except requests.ConnectionError:
        return False, ''


def parse_page(page: str) -> List[str]:
    '''Функция парсинга текса веб-страницы на наличие
    HTML заголовков 3-го уровня и возврат их в виде массива.'''
    regex_expression = r'<h3 id=\"\w+\">(.+)<\/h3>'
    results: List[str] = re.findall(regex_expression, page)
    return results


def main() -> None:
    '''Tестирование приложения'''
    print('Результат:')
    url = 'http://www.columbia.edu/~fdc/sample.html'
    get_status, page_data = get_page(url)
    if get_status:
        headers = parse_page(page_data)
        for header in headers:
            print(header)
    else:
        print('Не удалось загрузить страницу {}'.format(
            url
        ))


if __name__ == '__main__':
    main()

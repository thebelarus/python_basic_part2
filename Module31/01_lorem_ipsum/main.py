from typing import List
import re
text = """ Lorem ipsum dolor sit amet, consectetuer adipiscing elit. 
Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, 
nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. 
Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate 
"""

REGEX_EXPRESSION = r'\b\w{4}\b'


def main() -> None:
    '''Tестирование регулярного выражения'''
    words: List[str] = re.findall(REGEX_EXPRESSION, text)
    print(words)


if __name__ == '__main__':
    main()

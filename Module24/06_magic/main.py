class ElementWater:
    name = 'Вода'

    def __add__(self, other):
        if isinstance(other, ElementAir):
            return NewElement('Шторм')
        if isinstance(other, ElementFire):
            return NewElement('Пар')
        if isinstance(other, ElementGround):
            return NewElement('Грязь')
        return None

    def __str__(self):
        return self.name


class ElementAir:
    name = 'Воздух'

    def __add__(self, other):
        if isinstance(other, ElementWater):
            return NewElement('Шторм')
        if isinstance(other, ElementFire):
            return NewElement('Молния')
        if isinstance(other, ElementGround):
            return NewElement('Пыль')
        return None

    def __str__(self):
        return self.name


class ElementFire:
    name = 'Огонь'

    def __add__(self, other):
        if isinstance(other, ElementWater):
            return NewElement('Пар')
        if isinstance(other, ElementAir):
            return NewElement('Молния')
        if isinstance(other, ElementGround):
            return NewElement('Лава')
        return None

    def __str__(self):
        return self.name


class ElementGround:
    name = 'Земля'

    def __add__(self, other):
        if isinstance(other, ElementWater):
            return NewElement('Грязь')
        if isinstance(other, ElementAir):
            return NewElement('Пыль')
        if isinstance(other, ElementFire):
            return NewElement('Лава')
        return None

    def __str__(self):
        return self.name


class NewElement:
    def __init__(self, answer):
        self.answer = answer


def main():
    first_element = ElementWater()
    second_element = ElementAir()
    new_element = first_element + second_element
    print(f'{first_element} + {second_element} = {new_element.answer}')


if __name__ == '__main__':
    main()

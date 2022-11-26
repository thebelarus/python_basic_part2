class Potato:
    states = {0: 'Отсутсвует', 1: 'Росток', 2: 'Зеленая', 3: 'Зрелая'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def is_ripe(self):
        if self.state == 3:
            return True
        return False

    def print_state(self):
        print(f'Картошка {self.index} сейчас {self.state}')


class PotatoGarden:
    def __init__(self, count):
        self.potatoes = []
        self.seed_garden(count)

    def grow_all(self):
        print('Картошка прорастает')
        for potato in self.potatoes:
            potato.grow()

    def are_all_ripe(self):
        if not all([potato.is_ripe() for potato in self.potatoes]):
            print('Картошка еще не созрела!\n')
            return False
        else:
            print('Вся картошка созрела. Можно собирать!\n')
            return True

    def seed_garden(self, count=5):
        self.potatoes = [Potato(index) for index in range(1, count + 1)]


class Gardener:
    def __init__(self, name, garden):
        self.name = name
        self.garden = garden

    def take_care(self):
        if not self.garden.potatoes:
            print('Грядка пуста! Садим картошку!')
            self.garden.seed_garden()
        else:
            self.garden.grow_all()

    def harvest(self):
        if self.garden.are_all_ripe():
            self.garden.potatoes = []
            print('Урожай собран!')
        else:
            print('Урожай еще не созрел!')


def main():
    my_garden = PotatoGarden(5)
    my_gardener = Gardener('John', my_garden)
    for _ in range(3):
        my_gardener.take_care()
    my_gardener.harvest()
    my_gardener.take_care()
    my_gardener.take_care()


if __name__ == '__main__':
    main()

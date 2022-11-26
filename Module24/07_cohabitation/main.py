import random


class House:
    def __init__(self, fridge=50, money=0):
        self.fridge = 50
        self.money = 0


class Man:
    def __init__(self, name, house, health=50):
        self.name = name
        self.house = house
        self.health = health

    def eat(self):
        if self.health == 0:
            raise ValueError(
                f'Man {self.name}, not enough food in fridge for eat!')
        self.house.fridge -= 1
        self.health += 1

    def work(self):
        if self.health == 0:
            raise ValueError(f'Man {self.name}, not enough health for work!')
        self.health -= 1
        self.house.money += 1

    def play(self):
        if self.health == 0:
            raise ValueError(f'Man {self.name}, not enough health for play!')
        self.health -= 1

    def shopping(self):
        if self.house.money == 0:
            raise ValueError(
                f'Man {self.name}, not enough money for shopping!')
        self.house.money -= 1
        self.house.fridge += 1

    def simulate_day(self):
        random_num = random.randint(1, 6)
        if self.health < 0:
            raise ValueError(f'Man {self.name} is dead')
        elif self.health < 20:
            self.eat()
        elif self.house.fridge < 10:
            self.shopping()
        elif self.house.money < 50:
            self.work()
        elif random_num == 1:
            self.work()
        elif random_num == 2:
            self.eat()
        else:
            self.play()


def main():
    days_count = 365
    sweet_house = House()
    people = (
            Man('John', sweet_house),
            Man('Ann', sweet_house),
            Man('Bob', sweet_house),
            Man('Jennie', sweet_house),
        )
    for _ in range(days_count):
        for man in people:
            man.simulate_day()
    print(f'Stats ater {days_count} days')
    for man in people:
        print(f'Name: {man.name}')
        print(f'\tHealth: {man.health}')
        print(f'\tFridge: {man.house.fridge}')
        print(f'\tMoney: {man.house.money}')


if __name__ == '__main__':
    main()

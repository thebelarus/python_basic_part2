import random


class House:
    def __init__(
        self,
        human_food=50,
        money=100,
        cat_food=30,
        garbage=0
    ):
        self.__human_food = human_food
        self.__money = money
        self.__cat_food = cat_food
        self.__garbage = garbage
        self.__money_counter = 0
        self.__food_counter = 0

    def get_money_counter(self):
        return self.__money_counter

    def get_food_counter(self):
        return self.__food_counter

    def get_money(self):
        return self.__money

    def set_money(self, amount):
        self.__money = amount
        self.__money_counter += amount

    def get_human_food(self):
        return self.__human_food

    def set_human_food(self, amount):
        if amount < self.__human_food:
            self.__food_counter += self.__human_food - amount
        self.__human_food = amount

    def get_cat_food(self):
        return self.__cat_food

    def set_cat_food(self, amount):
        if amount < self.__cat_food:
            self.__food_counter += self.__cat_food - amount
        self.__cat_food = amount

    def get_garbage(self):
        return self.__garbage

    def set_garbage(self, amount):
        self.__garbage = amount

    def make_garbage(self):
        self.set_garbage(self.get_garbage() + 5)


class Human:
    def __init__(self, name, house, health=30, happiness=100):
        self.__name = name
        self.__house = house
        self.__health = health
        self.__happiness = happiness
        self.__food_eated = 0

    def get_name(self):
        return self.__name

    def get_house(self):
        return self.__house

    def get_health(self):
        return self.__health

    def get_happiness(self):
        return self.__happiness

    def set_name(self, amount):
        self.__name = amount

    def set_house(self, amount):
        self.__house = amount

    def get_house(self):
        return self.__house

    def set_health(self, amount):
        self.__health = amount

    def set_happiness(self, amount):
        self.__happiness = amount

    def pet_cat(self):
        self.__happiness += 5

    def eat(self):
        amount = random.randint(10, 30)
        if self.__house.get_human_food() < amount:
            raise ValueError('Недостаточно еды!')
        self.__health += amount
        self.__food_eated += amount
        self.__house.set_human_food(self.__house.get_human_food() - amount)
        return self.__health

    def decrease_health(self, amount=10):
        if self.__health - amount >= 0:
            self.__health -= amount
            return self.__health
        raise ValueError(f'{self.__name} умер от голода!')

    def check_garbage(self, amount=10):
        if self.__house.get_garbage() > 90:
            self.__happiness -= amount

    def check_happiness(self, amount=10):
        if self.house.get_happiness():
            self.happiness -= amount

    def day_checks(self):
        self.decrease_health()
        self.__house.make_garbage()
        self.check_garbage()


class Husband(Human):
    def play(self):
        self.day_checks()
        self.set_happiness(self.get_happiness() + 20)

    def work(self):
        self.day_checks()
        self.get_house().set_money(self.get_house().get_money() + 150)

    def simulate_day(self):
        if self.get_health() < 20:
            self.eat()
        if self.get_house().get_money() < 210:
            self.work()
        elif self.get_happiness() < 50:
            self.play()
        else:
            self.pet_cat()


class Wife(Human):
    def __init__(self, name, house, health=30, happiness=100):
        super().__init__(name, house, health, happiness)
        self.__coat_counter = 0

    def get_coat_count(self):
        return self.__coat_counter

    def buy_food(self, amount=100):
        self.day_checks()
        if self.get_house().get_cat_food() < 50:
            amount = 20
            if not self.get_house().get_money() >= amount:
                raise ValueError('Недостаточно денег для покупки еды коту!')
            self.get_house().set_money(self.get_house().get_money() - amount)
            self.get_house().set_cat_food(
                self.get_house().get_cat_food() + amount
                )
        if self.get_house().get_human_food() < 100:
            amount = 80
            if not self.get_house().get_money() >= amount:
                raise ValueError('Недостаточно денег для покупки еды людям!')
            self.get_house().set_money(self.get_house().get_money() - amount)
            self.get_house().set_human_food(
                self.get_house().get_human_food() + amount
            )

    def buy_coat(self):
        self.day_checks()
        if self.get_house().get_money() >= 350:
            self.__coat_counter += 1
            self.get_house().set_money(self.get_house().get_money() - 350)
            self.set_happiness(self.get_happiness() + 60)
            return True
        return False

    def clean_house(self, amount=100):
        self.day_checks()
        if amount > 0:
            if amount > self.get_house().get_garbage():
                self.get_house().set_garbage(0)
            else:
                self.get_house().set_garbage(
                    self.get_house().get_garbage() - amount
                )
            return True
        raise ValueError('Нелья убрать такое количество грязи!')

    def simulate_day(self):
        if self.get_health() < 20:
            self.eat()
        if self.get_house().get_garbage() > 50:
            self.clean_house()
        elif (self.get_house().get_human_food() < 100
                or self.get_house().get_cat_food() < 10):
            self.buy_food()
        elif self.get_house().get_money() >= 350:
            self.buy_coat()
        else:
            self.pet_cat()


class Cat:
    def __init__(self, name, house, health=30):
        self.__health = health
        self.__house = house
        self.__name = name

    def print_stats(self):
        print('health', self.__health)
        print('name', self.__name)

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def eat(self, amount=10):
        if self.__house.get_cat_food() >= amount:
            self.__health += amount * 2
            self.__house.set_cat_food(self.__house.get_cat_food() - amount)
            return self.__health
        raise ValueError('Столько нельзя съесть')

    def decrease_health(self, amount=10):
        if self.__health - amount >= 0:
            self.__health -= amount
            return self.__health
        raise ValueError(f'Кот {self.__name} умер от голода!')

    def sleep(self):
        self.decrease_health()

    def tear_wallpaper(self, amount=5):
        self.decrease_health()
        self.__house.set_garbage(self.__house.get_garbage() + amount)

    def simulate_day(self):
        if self.__health < 20:
            self.eat()
        random_number = random.randint(1, 2)
        if random_number == 1:
            self.tear_wallpaper()
        elif random_number == 2:
            self.sleep()


def main():
    days_count = 365
    sweet_house = House()
    husband = Husband('Tom', sweet_house)
    wife = Wife('Ann', sweet_house)
    cat = Cat('Bob', sweet_house)
    citizens = (
        husband,
        wife,
        cat
    )
    for _ in range(1, days_count + 1):
        for citizen in citizens:
            citizen.simulate_day()
    print(f'Ститистика после {days_count} дней')
    print('Было заработано денег:', sweet_house.get_money_counter())
    print('Cъедено еды:', sweet_house.get_food_counter())
    print('Куплено шуб:', wife.get_coat_count())


if __name__ == '__main__':
    main()

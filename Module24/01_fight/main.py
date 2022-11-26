import random


class Warrior:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def hit_to_rival(self, rival):
        if isinstance(rival, Warrior):
            rival.set_damage_hit()

    def set_damage_hit(self, damage=20):
        self.health -= damage

    def __str__(self):
        return self.name


def get_fight_log(sender, receiver):
    return f'{sender} атаковал {receiver}, у \
        противника {receiver.health} здоровья'


def main():
    warrior_1 = Warrior('Воин 1')
    warrior_2 = Warrior('Воин 2')
    while warrior_1.health > 0 and warrior_2.health > 0:
        ramdom_number = random.randint(0, 10)
        if ramdom_number > 5:
            warrior_1.hit_to_rival(warrior_2)
            fight_log = get_fight_log(warrior_1, warrior_2)
            print(fight_log)
        else:
            warrior_2.hit_to_rival(warrior_1)
            fight_log = get_fight_log(warrior_2, warrior_1)
            print(fight_log)
    winner = warrior_1 if warrior_1.health > warrior_2.health else warrior_2
    print(f'{winner.name} победитель')


if __name__ == '__main__':
    main()

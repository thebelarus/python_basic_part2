import random


class Card:
    def __init__(self, suit, rate, value):
        self.suit = suit
        self.rate = rate
        self.value = value

    def __str__(self):
        return f'{self.suit} {self.rate}'

    def __repr__(self):
        return f'{self.suit} {self.rate}'


class Deck:
    def __init__(self):
        self.cards = []
        for suit in ('Черви', 'Бубны', 'Пике', 'Трефи'):
            for rate in range(2, 11):
                self.cards.append(Card(suit, rate, rate))
            for rate in ('Король', 'Дама', 'Валет'):
                self.cards.append(Card(suit, rate, 10))
            self.cards.append(Card(suit, 'Ace', 11))

    def get_card(self):
        random_number = random.randint(0, len(self.cards) - 1)
        return self.cards.pop(random_number)


class Player:
    def __init__(self, deck):
        self.deck = deck
        self.my_cards = []
        for _ in range(2):
            if self.deck:
                self.my_cards.append(self.deck.get_card())

    def get_cards_rate_amount(self):
        amount = 0
        for card in self.my_cards:
            if card.value == 11 and amount + 11 > 21:
                amount += 1
            else:
                amount += card.value
        return amount

    def get_new_card(self):
        self.my_cards.append(self.deck.get_card())

    def show_cards(self):
        return ', '.join([str(card) for card in self.my_cards])


def main():
    deck = Deck()
    user_player = Player(deck)
    computer_player = Player(deck)
    print(f'Ваши карты: {user_player.show_cards()}')
    while user_player.get_cards_rate_amount() < 22:
        user_choise = input('Хотите взять ещё карту? (Да или Нет) ')
        if user_choise == 'Да':
            user_player.get_new_card()
            print(f'Ваши карты: {user_player.show_cards()}')
        elif user_choise == 'Нет':
            break
    user_rate = user_player.get_cards_rate_amount()
    pc_rate = computer_player.get_cards_rate_amount()
    text_stats = f'Вы набрали {user_rate} очков, компьютер {pc_rate} очков'
    if pc_rate < user_rate < 22:
        print(f'Вы победели! {text_stats}')
    elif pc_rate == user_rate:
        print(f'Ничья! {text_stats}')
    else:
        print(f'Вы проиграли! {text_stats}')
    print(f'Карты компьютера: {computer_player.show_cards()}')


if __name__ == '__main__':
    main()

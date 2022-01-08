"""Task 4 solution."""

from typing import List

if __name__ == '__main__':
    guests: List[str] = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
    end_party: bool = False
    while(not end_party):
        party_length = len(guests)
        print(f'Сейчас на вечеринке {party_length} человек: {guests}')
        command = input('Гость пришёл или ушёл? ')
        if command == 'пришёл':
            guest_name = input('Имя гостя: ')
            if len(guests) > 6:
                print(f'Прости, {guest_name}, но мест нет.')
                continue
            guests.append(guest_name)
        elif command == 'ушёл':
            guest_name = input('Имя гостя: ')
            if guest_name in guests:
                guests.remove(guest_name)
                print(f'Пока, {guest_name}!')
            else:
                print(f'{guest_name} нет на вечеринке!')
        elif command == 'Пора спать':
            end_party = True

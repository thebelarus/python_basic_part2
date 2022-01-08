"""Task 9 solution."""
if __name__ == '__main__':
    try:
        friends_count = int(input('Кол-во друзей: '))
        receipts_count = int(input('Долговых расписок: '))
        friends_array = [0 for _ in list(range(friends_count))]
        for receipt in range(1, receipts_count + 1):
            print(f'{receipt} расписка')
            friend_to = int(input('Кому: '))
            if not 0 < friend_to <= len(friends_array):
                raise IndexError('Ошибка! Данного друга нет в списке!')
            friend_from = int(input('От кого: '))
            if not 0 < friend_from <= len(friends_array):
                raise IndexError('Ошибка! Данного друга нет в списке!')
            if friend_from == friend_to:
                raise IndexError('Ошибка! Нельзя передавать себе же деньги!')
            amount = int(input('Сколько: '))
            friends_array[friend_to - 1] -= amount
            friends_array[friend_from - 1] += amount
        print('Баланс друзей:')
        for friend, amount in enumerate(friends_array):
            print(f'{friend + 1} : {amount}')
    except ValueError:
        print('Ошибка! Все данные должны быть целыми числами!')
    except IndexError as e:
        print(e)

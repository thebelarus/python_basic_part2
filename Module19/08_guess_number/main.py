if __name__ == '__main__':
    hidden_number = 3
    max_number = int(input('Введите максимальное число: '))
    numbers = set(range(1, max_number + 1))
    while True:
        player_input = input('Нужное число есть среди вот этих чисел: ')
        if player_input == 'Помогите!':
            break
        player_attempt_nums = set([int(item) for item in player_input.split()])
        if hidden_number in player_attempt_nums:
            numbers = player_attempt_nums
            print('Ответ Артёма: Да')
        else:
            numbers -= player_attempt_nums
            print('Ответ Артёма: Нет')
    result = ' '.join([str(number) for number in numbers])
    print(f'Артём мог загадать следующие числа: {result}')

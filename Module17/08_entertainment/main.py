def make_sticks_array(sticks=10):
    return ['I' for x in range(sticks)]


def hit_stick_array(start, end, array):
    return ['.' if start <= index+1 <= end or
            array[index] == '.' else 'I' for index in range(len(array))]


if __name__ == '__main__':
    stick_count_input = int(input('Кол-во палок: '))
    attempt_count_input = int(input('Кол-во бросков: '))
    game_sticks_array = make_sticks_array(stick_count_input)
    for attempt in range(attempt_count_input):
        while True:
            start_hit = int(input('Начало диапазона удара: '))
            end_hit = int(input('Конец диапазона удара: '))
            if 1 <= start_hit <= end_hit <= len(game_sticks_array):
                game_sticks_array = hit_stick_array(
                    start_hit, end_hit, game_sticks_array)
                print(f'Бросок {attempt + 1}. Сбиты палки с номера '
                      'f{start_hit} по номер {end_hit}')
                attempt_count_input -= 1
                break
            print('Неверный диапазон удара или выход за рамки размера игры!')
    final_sticks = ''.join(game_sticks_array)
    result = f'Результат: {final_sticks}'
    print(result)

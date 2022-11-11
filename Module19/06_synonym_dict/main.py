if __name__ == '__main__':
    pairs = {}
    pairs_count = int(input('Введите количество пар слов: '))
    for pair_num in range(1, pairs_count + 1):
        pair_input_data = input(f'{pair_num} пара: ')
        word_1, word_2 = [word.lower()
                          for word in pair_input_data.split(' — ')]
        pairs[word_1] = word_2
        pairs[word_2] = word_1
    while True:
        word_input = input('Введите слово: ').lower()
        if word_input in pairs:
            print(f'Синоним: {pairs[word_input]}')
            break
        print('Такого слова в словаре нет.')

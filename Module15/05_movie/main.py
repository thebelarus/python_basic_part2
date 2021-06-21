films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']

if __name__ == '__main__':
    favorite_films = []
    while True:
        user_input = input('Введите фильм или exit для выхода: ')
        if user_input == 'exit':
            break
        elif user_input in films:
            favorite_films.append(user_input)
            print(f'Фильм {user_input} добавлен в список любимых!')
        else:
            print('Ошибка! Данного фильма нет в списке фильмов!')
    result = ', '.join(favorite_films) if favorite_films else 'пуст'
    print(f'Cписок любимых фильмов: {result}.')

# зачет!

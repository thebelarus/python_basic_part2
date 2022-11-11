violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}


if __name__ == '__main__':
    song_count_input = int(input('Сколько песен выбрать? '))
    songs_duration = 0
    for song_number in range(1, song_count_input + 1):
        while True:
            song_name = input(f'Название {song_number} песни: ')
            song_duration = violator_songs.get(song_name, False)
            if song_duration:
                songs_duration += song_duration
                break
            print('Данной песени нет в списке!')
    result = round(songs_duration, 2)
    print(f'Общее время звучания песен: {result} минуты')

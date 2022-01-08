"""Task 5 solution."""
if __name__ == '__main__':
    violator_songs = [
        ['World in My Eyes', 4.86],
        ['Sweetest Perfection', 4.43],
        ['Personal Jesus', 4.56],
        ['Halo', 4.9],
        ['Waiting for the Night', 6.07],
        ['Enjoy the Silence', 4.20],
        ['Policy of Truth', 4.76],
        ['Blue Dress', 4.29],
        ['Clean', 5.83]
    ]
    songs_duration = 0
    song_count = int(input('Сколько песен выбрать? '))
    for song_num in range(1, song_count + 1):
        song_name = input(f'Название {song_num} песни: ')
        filtered_song = list(
            filter(lambda a: a[0] == song_name, violator_songs)
        )
        if filtered_song:
            _, song_duration = filtered_song[0]
            songs_duration += song_duration
        else:
            print('Песня на найдена!')

    print(f'Общее время звучания песен: {songs_duration:.2f} минут')

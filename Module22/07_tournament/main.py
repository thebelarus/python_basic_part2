import os


def is_file_exists(filename):
    filepath = os.path.join(os.getcwd(), filename)
    if os.path.exists(filepath):
        return True
    return False


def write_results_to_file(filename, base):
    with open(filename, 'w', encoding='utf8') as file:
        file.write('2\n')
        for index, (name, score) in enumerate(base):
            file.write(f'{index + 1}) {name} {score}\n')


def read_lines_from_tour_file(filename):
    with open(filename, encoding='utf8') as file:
        lines = [line.strip() for line in file.readlines()]
    return lines


def main():
    filename_for_read = 'first_tour.txt'
    filename_for_write = 'second_tour.txt'
    game_base = {}
    if is_file_exists(filename_for_read):
        lines = read_lines_from_tour_file(filename_for_read)
        tour_score = int(lines.pop(0))
        for line in lines:
            last_name, first_name, score = line.split()
            score = int(score)
            if score > tour_score:
                key = f'{first_name[0]} {last_name}'
                game_base[key] = int(score)
        sorted_base = sorted(game_base.items(), key=lambda x: -x[1])
        write_results_to_file(filename_for_write, sorted_base)
    else:
        print(f'Файла {filename_for_read} не существует!')


if __name__ == '__main__':
    main()

def make_histogram(text: str):
    result = {}
    for char in text:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result


def get_inverted_histogram(data: dict):
    result = {}
    for key, value in data.items():
        if value in result:
            result[value].append(key)
        else:
            result[value] = [key]
    return result


if __name__ == '__main__':
    histogram = {}
    text_input = input('Введите текст: ')
    print('Оригинальный словарь частот:')
    histogram = make_histogram(text_input)
    for key, value in histogram.items():
        print(f'{key} : {value}')
    inverted_histogram = get_inverted_histogram(histogram)
    print('Инвертированный словарь частот:')
    for key, value in inverted_histogram.items():
        print(f'{key} : {value}')

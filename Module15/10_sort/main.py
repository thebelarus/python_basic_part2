def l_sort(value_l):
    for i in range(len(value_l)):
        for j in range(i, len(value_l)):
            if value_l[j] > value_l[i]:
                value_l[i], value_l[j] = value_l[j], value_l[i]


if __name__ == '__main__':
    l_input = [1, 4, -3, 0, 10]
    print(f'Изначальный список: {l_input}')
    l_sort(l_input)
    print(f'Отсортированный список: {l_input}')

# TODO применить рекомендации данные ранее

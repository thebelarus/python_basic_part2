def generate_array(number=12):
    outer = number // 3
    inner = number // outer
    return [[el for el in range(
        o + 1, inner * outer + 1, outer)]for o in range(outer)]


if __name__ == '__main__':
    print(generate_array())

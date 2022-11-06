def decompress_array(array):
    return [
        level_3 for level_1 in array for level_2 in level_1
        for level_3 in level_2
    ]


if __name__ == '__main__':
    nice_list = [
        [
            [1, 2, 3], [4, 5, 6], [7, 8, 9]
        ],
        [
            [10, 11, 12], [13, 14, 15], [16, 17, 18]
        ]
    ]
    print(decompress_array(nice_list))

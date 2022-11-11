goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}


if __name__ == '__main__':
    for good_name, good_value in goods.items():
        price = sum(
            [
                item['price']*item['quantity']
                for item in store[good_value]
            ]
        )
        quantity = sum(
            [
                item['quantity']
                for item in store[good_value]
            ]
        )
        print(f'{good_name} — {quantity} штук, стоимость {price} рубля')

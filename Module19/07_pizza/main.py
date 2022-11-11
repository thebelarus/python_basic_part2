if __name__ == '__main__':
    buyers = {}
    orders_count = int(input('Введите количество заказов: '))
    for orders_num in range(1, orders_count + 1):
        order_input_data = input(f'{orders_num} заказ: ')
        name, pizza_name, count = [
            word for word in order_input_data.split()]
        pizza_count = int(count)
        if name in buyers:
            if pizza_name in buyers[name]:
                buyers[name][pizza_name] += pizza_count
            else:
                buyers[name][pizza_name] = pizza_count
        else:
            buyers[name] = {}
            buyers[name][pizza_name] = pizza_count
    for buyer in sorted(buyers.keys()):
        print(f'{buyer}: ')
        for order in sorted(buyers[buyer].keys()):
            print(f'\t{order}: {buyers[buyer][order]}')

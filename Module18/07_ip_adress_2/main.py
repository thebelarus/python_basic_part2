def validate_ip(ip_string):
    notice_message = 'Адрес — это четыре числа, разделённые точками.'
    if not ip_string:
        return False, notice_message
    ip_string_array = ip_string.split('.')
    if not len(ip_string_array) == 4:
        return False, notice_message
    for ip_octet in ip_string_array:
        if not ip_octet.isnumeric():
            return False, f'{ip_octet} — это не целое число.'
        if not 0 <= int(ip_octet) <= 255:
            return False, f'{ip_octet} превышает 255.'
    return True, 'IP-адрес корректен.'


if __name__ == '__main__':
    ip_input = input('Введите строку: ')
    _, coded_sting = validate_ip(ip_input)
    print(coded_sting)

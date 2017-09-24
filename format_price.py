import math


def validation_price(price):
    val_for_zero_check = 0
    try:
        price = float(price)
    except (TypeError, ValueError):
        return 'Wrong format of number!'
    if price < val_for_zero_check:
        return 'Price cant be negative!'


def format_price(input_price):
    mod_0, mod_1, mod_2, mod_3, mod_4 = 0, 1, 2, 3, 4
    try:
        int_part_price, fract_part_price = input_price.split('.')
        fract_part_price = '{}.{}'.format(mod_0, fract_part_price)
        fract_part_price = round(float(fract_part_price), mod_2)
    except ValueError:
        int_part_price = input_price
        fract_part_price = 0
    len_list = len(int_part_price) + len(int_part_price) // mod_3
    int_part_price = list(int_part_price)
    int_part_price.reverse()
    for elem in range(len_list):
        if (not (elem + mod_1) % mod_4) and elem != len_list - mod_1:
            int_part_price.insert(elem, ' ')
    int_part_price.reverse()
    formated_price = ''
    for elem in int_part_price:
        formated_price = '{}{}'.format(formated_price, elem)
    if fract_part_price:
        formated_price = '{}{}'.format(formated_price, fract_part_price)
    return formated_price


if __name__ == '__main__':
    input_price = input('Enter price: ')
    validation_price = validation_price(input_price)
    if not validation_price:
        format_price = format_price(input_price)
        print(format_price)
    else:
        print(validation_price)

import math


def get_validation_result(price):
    val_for_zero_check = 0
    try:
        price = float(price)
    except (TypeError, ValueError):
        return 'Wrong format of number!'
    if price < val_for_zero_check:
        return 'Price cant be negative!'


def get_parts_of_price(price):
    mod_0, mod_2 = 0, 2
    try:
        int_part_price, fract_part_price = input_price.split('.')
        fract_part_price = '{}.{}'.format(mod_0, fract_part_price)
    except ValueError:
        int_part_price = input_price
        fract_part_price = 0

    return int_part_price, fract_part_price


def format_int_part_price(int_part_price):
    mod_0, mod_1, mod_3, mod_4 = 0, 1, 3, 4
    len_list = len(int_part_price) + len(int_part_price) // mod_3
    int_part_price = list(int_part_price)
    int_part_price.reverse()
    for elem in range(len_list):
        if (not (elem + mod_1) % mod_4) and elem != len_list - mod_1:
            int_part_price.insert(elem, ' ')
    int_part_price.reverse()
    int_formated_price = ''
    for elem in int_part_price:
        int_formated_price = '{}{}'.format(int_formated_price, elem)
    return int_formated_price


def format_fract_part_price(fract_part_price):
    mod_0, mod_2 = 0, 2
    mod_001 = 0.01
    if fract_part_price:
        format_price_step_1 = float(fract_part_price)
        if format_price_step_1 < mod_001:
            return mod_0
        else:
            format_price_step_2 = round(format_price_step_1, mod_2)
            format_price_step_3 = str(format_price_step_2)[1:]
            return format_price_step_3
    return fract_part_price


def get_full_formated_price(int_formated_price, fract_formated_price):
    if fract_formated_price:
        formated_price = '{}{}'.format(
                int_formated_price, fract_formated_price)
    else:
        formated_price = int_formated_price
    return formated_price


if __name__ == '__main__':
    input_price = input('Enter price: ')
    validation_price = get_validation_result(input_price)
    if not validation_price:
        parts_of_price = get_parts_of_price(input_price)
        format_int_part_price = format_int_part_price(parts_of_price[0])
        format_fract_part_price = format_fract_part_price(parts_of_price[1])
        full_formated_price = get_full_formated_price(
                format_int_part_price, format_fract_part_price)
        print(full_formated_price)
    else:
        print(validation_result)

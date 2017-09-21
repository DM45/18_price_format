import math


def validation_price(price):
	val_for_zero_check = 0
	try:
		price = float(price)
	except:
		return 'Something wrong with number!'
	if price < val_for_zero_check:
		return 'Price cant be negative!'


def format_price(input_price):
    mod_1, mod_2, mod_3 = 1, 2, 3
    fract_part_price, int_part_price = math.modf(float(price))
    fract_part_price = round(fract_part_price, mod_2)
    formated_price = ''
    int_part_price = str(int(int_part_price))
    len_price = len(int_part_price)
    int_part_price = int_part_price[::-mod_1]
    for number in range(mod_1, len_price + mod_1):
        if not number % mod_3:
        	if formated_price:
        		formated_price = '{} {}'.format(
        			    formated_price, int_part_price[number - mod_3:number])
        	else:
        		formated_price = int_part_price[number - mod_3:number]
    if len_price % mod_3:
    	if not (len_price - mod_1) % mod_3:
            formated_price = '{} {}'.format(
            	    formated_price, int_part_price[number - mod_1:number])
    	else:
    		formated_price = '{} {}'.format(
    			    formated_price, int_part_price[number - mod_2:number])
    formated_price = formated_price[::-mod_1]
    if fract_part_price:
    	zero_arg, fract_arg = str(fract_part_price).split('.')
    	formated_price = '{}.{}'.format(formated_price, fract_arg)
    return formated_price


if __name__ == '__main__':
    input_price = input('Enter price: ')
    validation_price = validation_price(price)
    if not validation_price:
        format_price = format_price(price)
        print(format_price)
    else:
        print(validation_price)

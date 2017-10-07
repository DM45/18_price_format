# Price Formatter

Change format input price from 1234.0000 to 1 234.

Tests included.

# How to Install

Python 3 should be already installed.

Clone project from github and start.

# How to Start

## For Command Line Interface:
```bash
python format_price.py
```
## For import to site:

```python
import format_price

    input_price = input('Enter price: ')
    validation_result = format_price.get_validation_result(input_price)
    if not validation_result:
        parts_of_price = format_price.get_parts_of_price(input_price)
        format_int_part_price = format_price.format_int_part_price(parts_of_price[0])
        format_fract_part_price = format_price.format_fract_part_price(parts_of_price[1])
        full_formated_price = format_price.get_full_formated_price(
                format_int_part_price, format_fract_part_price)
        print(full_formated_price)
    else:
        print(validation_result)
```
# Start tests

```bash
python tests.py
```
# Input example

```bash
456123456
```

# Output example

```bash
456 123 456
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)


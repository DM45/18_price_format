# Price Formatter

Change format input price from 1234.0000 to 1 234.

Tests included.

# How to Install

Python 3 should be already installed.

Clone project from github and start.

# How it work

## For Command Line Interface:
```bash
python format_price.py
```
## For import to site:

```python
from format_price import validation_price, format_price

if not validation_price(price):
    format_price(price)
else:
    validation_price(price)
```
Where price - your price

If format of price acceptable this code return formated price

Else - error

# Output

```bash
456 123 456
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)


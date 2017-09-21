import unittest
from format_price import validation_price


class FormatPriceTestCase(unittest.TestCase):
    def test_negetive_price(self):
        price = validation_price(-1)
        self.assertIsNotNone(price)

    def test_input_date_with_letters(self):
        price = validation_price('abc')
        self.assertIsNotNone(price)

    def test_input_date_with_comma(self):
        price = validation_price(0,5)
        self.assertIsNotNone(price)


if __name__ == '__main__':
    unittest.main()

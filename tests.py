import unittest
from format_price import validation_price, format_price


class FormatPriceTestCase(unittest.TestCase):
    def test_negative_price(self):
        price = validation_price('-1')
        self.assertIsNotNone(price)

    def test_input_date_with_letters(self):
        price = validation_price('abc')
        self.assertIsNotNone(price)

    def test_input_date_with_comma(self):
        price = validation_price('0,5')
        self.assertIsNotNone(price)
    
    def test_change_price_after_formated(self):
        price = format_price('3333333333333333333333333')
        formated_price = '3 333 333 333 333 333 333 333 333'
        self.assertEqual(price, formated_price)
    
    def test_fractional_part_formated(self):
        price = format_price('123.000000000')
        formated_price = '123'
        self.assertEqual(price, formated_price)


if __name__ == '__main__':
    unittest.main()

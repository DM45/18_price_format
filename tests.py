import unittest
from format_price import (get_validation_result, format_int_part_price,
        format_fract_part_price, get_full_formated_price)


class FormatPriceTestCase(unittest.TestCase):
    def test_negative_price(self):
        price = get_validation_result('-1')
        self.assertIsNotNone(price)

    def test_input_date_with_letters(self):
        price = get_validation_result('abc')
        self.assertIsNotNone(price)

    def test_input_date_with_comma(self):
        price = get_validation_result('0,5')
        self.assertIsNotNone(price)
    
    def test_change_price_after_formated(self):
        price = format_int_part_price('3333333333333333333333333')
        formated_price = '3 333 333 333 333 333 333 333 333'
        self.assertEqual(price, formated_price)
    
    def test_fractional_part_formated(self):
        price = format_fract_part_price('0.001')
        formated_price = 0
        self.assertEqual(price, formated_price)

    def test_merge_parts_of_price(self):
        price = get_full_formated_price('123', '.01')
        formated_price = '123.01'
        self.assertEqual(price, formated_price)


if __name__ == '__main__':
    unittest.main()

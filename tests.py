import unittest

from format_price import validation_price


class FormatPriceTestCase(unittest.TestCase):
    def test_negetive_price(self):
        price = validation_price(-1)
        self.assertIsNotNone(price)

    def test_cant_be_floated(self):
        price = validation_price('abc')
        self.assertIsNotNone(price)


if __name__ == '__main__':
    unittest.main()

import sys
from pathlib import Path
from unittest import TestCase

try:
    from money import Dollar
except ModuleNotFoundError:
    sys.path.append(str((Path(__file__).parent.parent)))
    sys.path.append(str((Path(__file__).parent.parent / "src")))
    from money import Dollar


class MoneyTest(TestCase):
    def test_multiplication(self) -> None:
        five = Dollar(5)
        product: Dollar = five.times(2)
        self.assertEqual(10, product.amount)
        product = five.times(3)
        self.assertEqual(15, product.amount)

    def test_equality(self) -> None:
        self.assertTrue(Dollar(5).equals(Dollar(5)))
        self.assertFalse(Dollar(5).equals(Dollar(6)))

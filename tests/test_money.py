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
        self.assertEqual(Dollar(10), five.times(2))
        self.assertEqual(Dollar(15), five.times(3))

    def test_equality(self) -> None:
        self.assertTrue(Dollar(5) == Dollar(5))
        self.assertFalse(Dollar(5) == Dollar(6))

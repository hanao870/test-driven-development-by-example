"""Dummy comments."""


class Dollar:
    """通貨処理クラス."""

    def __init__(self, amount: int) -> None:
        """イニシャライザ.

        Args:
            amount (int): 金額(USD)
        """
        self.amount = amount

    def times(self, multiplier: int) -> "Dollar":
        """乗数の金額を返す.

        Args:
            multiplier (int): 乗数
        """
        return Dollar(self.amount * multiplier)

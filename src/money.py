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

    def equals(self, object: "Dollar") -> bool:
        """オブジェクトが等価か確認する.

        Args:
            object (Dollar): 比較オブジェクト

        Returns:
            bool: オブジェクトが等価の場合は `True` を返す. それ以外は `False` を返す.
        """
        return self.amount == object.amount

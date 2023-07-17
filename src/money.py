"""Dummy comments."""


class Dollar:
    """通貨処理クラス."""

    def __init__(self, amount: int) -> None:
        """イニシャライザ.

        Args:
            amount (int): 金額(USD)
        """
        self.__amount = amount

    def times(self, multiplier: int) -> "Dollar":
        """乗数の金額を返す.

        Args:
            multiplier (int): 乗数
        """
        return Dollar(self.__amount * multiplier)

    def __eq__(self, __value: object) -> bool:
        """オブジェクトが等価か確認する.

        Args:
            __value (object): 比較オブジェクト

        Returns:
            bool: オブジェクトが等価の場合は `True` を返す. それ以外は `False` を返す.
        """
        if not isinstance(__value, Dollar):
            return False

        return self.__amount == __value.__amount

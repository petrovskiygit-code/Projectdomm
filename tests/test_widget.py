from src.widget import mask_account_card, get_date
import pytest


@pytest.mark.parametrize("card, result", [
    ("mastercard 5555666677778888", "mastercard  5555 66** **** 8888"),
    ("visa 1111222233334444", "visa  1111 22** **** 4444"),
    ("visa  1111 22** **** 4444", "Не корректный ввод данных"),
    ("visa 111122223333", "Не корректный ввод данных")
])
def test_mask_account_card(card: str, result: str) -> None:
    assert mask_account_card(card) == result


@pytest.mark.parametrize("oksi, result", [
    ("2025.11.11", "11.11.2025"),
    ("2025-11-11", "11.11.2025")
])
def test_get_date(oksi: str, result: str) -> None:
    assert get_date(oksi) == result

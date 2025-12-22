import pytest

from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize(
    "number,result",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("5555666677778888", "5555 66** **** 8888"),
        ("70007922661111", "Не корректные данные"),
        ("55556666777788880000", "Не корректные данные")
    ]
)
def test_get_mask_card_number(number: str, result: str) -> None:
    assert get_mask_card_number(number) == result


@pytest.mark.parametrize(
    "zed,result",
    [
        ("76677722228844483333", "**3333"),
        ("76677788444833332222", "**2222"),
        ("7667778844482222", "Не корректный ввод данных"),
        ("7667778844482222", "Не корректный ввод данных")
    ]
)
def test_get_mask_account(zed: str, result: str) -> None:
    assert get_mask_account(zed) == result

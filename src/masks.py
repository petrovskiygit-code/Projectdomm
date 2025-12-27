def get_mask_card_number(number: str) -> str:
    """Маскирует номер карты"""
    if len(number) == 16:
        return f"{number[:4]} {number[4:6]}** **** {number[12:]}"
    else:
        return "Не корректные данные"


def get_mask_account(account_number: str) -> str:
    """Маскирует номер аккаунта"""
    if len(account_number) == 20:
        return f"**{account_number[-4:]}"
    else:
        return "Не корректный ввод данных"



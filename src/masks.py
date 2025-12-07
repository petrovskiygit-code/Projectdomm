def get_mask_card_number(number: str) -> str:
    """Маскирует номер карты"""
    return f"{number[:4]} {number[4:6]}** **** {number[12:]}"


def get_mask_account(account_number: str) -> str:
    """Маскирует номер акаунта"""
    return f"**{account_number[-4:]}"


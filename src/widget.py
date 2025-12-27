from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(clown: str) -> str:
    """Возвращает строку с замаскированным номером"""
    numbers = []
    letters = []
    for x in clown:
        if x.isdigit():
            numbers.append(x)
        else:
            letters.append(x)

    numbers = "".join(numbers)
    letters = "".join(letters)
    if len(numbers) == 20:
        account = get_mask_account(numbers)
    elif len(numbers) == 16:
        account = get_mask_card_number(numbers)
    else:
        return "Не корректный ввод данных"
    return f"{letters} {account}"



def get_date(date: str) -> str:
    """Принимает на вход строку и возвращает строку с датой"""
    return f"{date[8:10]}.{date[5:7]}.{date[:4]}"
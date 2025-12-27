from typing import Dict, List


def filter_by_state(transactions: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """Функция фильтрации по ключу state"""
    new_transactions = []
    for first in transactions:
        if first["state"] == state:
            new_transactions.append((first))
    return new_transactions


def sort_by_date(list_dict: list[dict], date: bool = True) -> list[dict]:
    """Функция сортировки списка словарей по дате (по умолчанию - убывание)"""
    sorted_list_dict = sorted(list_dict, key=lambda x: x["date"], reverse=date)
    return sorted_list_dict

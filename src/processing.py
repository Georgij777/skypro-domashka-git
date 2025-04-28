from typing import Iterable


def filter_by_state(users_data: Iterable[dict], state: str = "EXECUTED") -> list:
    """Эта функция возвращает данные по запросу: state == EXECUTED"""
    state_ex = []
    for data in users_data:
        if data.get("state", 0) == state.upper():
            state_ex.append(data)
    return state_ex


def sort_by_date(users_data: Iterable[dict], descending=True) -> list:
    """Сортирует по дате"""
    return sorted(users_data, key=lambda x: x.get("date", 0), reverse=descending)

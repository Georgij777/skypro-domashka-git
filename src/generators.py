from typing import Generator, Iterable


def filter_by_currency(transactions: Iterable[dict], currency: str = "USD") -> Generator[dict]:
    """Выводит отфильтрованный список транзакций по требуемой валюте"""
    for i in transactions:
        x = i["operationAmount"]["currency"]["code"]
        if x == currency:
            yield i


def transaction_descriptions(transactions: Iterable[dict]) -> Generator[None]:
    """Принимает список транзакций и выводит информацию из раздела 'description'"""
    for i in transactions:
        x = i["description"]
        yield x


def card_number_generator(start: int = 1, end: int = 2) -> Generator[str, None, None]:
    """Генерирация номеров карт в заданном диапозоне"""
    for i in range(start, end + 1):
        card_number = str(i).zfill(16)
        yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"

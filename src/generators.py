from typing import Generator


def filter_by_currency(transactions, currency='USD'):
    """Выводит отфильтрованный список транзакций по требуемой валюте """
    for i in transactions:
        x = i["operationAmount"]["currency"]["code"]
        if x == currency:
            yield i


def transaction_descriptions(transactions):
    """Принимает список транзакций и выводит из раздела 'description'"""
    for i in transactions:
        x = i['description']
        yield x


def card_number_generator(start: int, end: int) -> Generator[str, None, None]:
    """Генерирация номеров карт в заданном диапозоне"""
    for i in range(start, end + 1):
        card_number = str(i).zfill(16)
        yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"

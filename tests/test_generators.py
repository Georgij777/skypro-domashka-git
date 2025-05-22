import src.generators
from typing import Generator
from typing import Iterable


def test_filter_by_currency(coll_generators_1: Iterable[dict], currency: str = "USD") -> None:
    generator_1 = src.generators.filter_by_currency(coll_generators_1, "RUB")
    assert next(generator_1) == {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    }
    generator_2 = src.generators.filter_by_currency(coll_generators_1, "USD")
    assert next(generator_2) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    generator_3 = src.generators.filter_by_currency(coll_generators_1)
    assert next(generator_3) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }


def test_transaction_descriptions(coll_generators_1: Iterable[dict]) -> Generator[None]:
    generator_1 = src.generators.transaction_descriptions(coll_generators_1)
    assert next(generator_1) == "Перевод организации"
    assert next(generator_1) == "Перевод со счета на счет"


def test_card_number_generator(start: int = 1, end: int = 2) -> [list]:
    assert list(src.generators.card_number_generator(1, 5)) == [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005",
    ]
    assert list(src.generators.card_number_generator()) == ["0000 0000 0000 0001", "0000 0000 0000 0002"]

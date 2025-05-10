import pytest


@pytest.fixture
def coll_mask_1():
    return "7000792289606361"


@pytest.fixture
def coll_mask_2():
    return "73654108430135874305"


@pytest.fixture
def coll_widget_1():
    return "T02:26:18.671407"


@pytest.fixture
def coll_widget_2():
    return "2024-03-11T02:26:18.671407"


@pytest.fixture
def coll_processing_1():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2019-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2022-06-30T02:08:58.425572"},
    ]

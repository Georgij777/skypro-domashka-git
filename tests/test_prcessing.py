import src.processing


def test_filter_by_state(coll_processing_1, state: str = "EXECUTED") -> list:
    assert src.processing.filter_by_state(coll_processing_1, "EXECUTED") == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2022-06-30T02:08:58.425572"},
    ]


def test_filter_by_state(coll_processing_1, state = "EXECUTED"):
    assert src.processing.filter_by_state(coll_processing_1, "CANCELED") == [
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2019-09-12T21:27:25.241689"},
    ]


def test_sort_by_date(coll_processing_1, descending=True):
    assert src.processing.sort_by_date(coll_processing_1, False) == [
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 594226727, "state": "CANCELED", "date": "2019-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2022-06-30T02:08:58.425572"},
    ]
    assert src.processing.sort_by_date(coll_processing_1, True) == [
        {"id": 939719570, "state": "EXECUTED", "date": "2022-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2019-09-12T21:27:25.241689"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]

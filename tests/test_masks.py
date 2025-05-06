import pytest

import src.masks

@pytest.fixture
def coll_mask_1():
    return "73654108430135874305"


def test_get_mask_card_number(coll_mask_1: str) -> str:
    assert src.masks.get_mask_card_number(coll_mask_1) == "7365 41** **** 4305"


@pytest.fixture
def coll_mask_2():
    return "73654108430135874305"


def test_get_mask_account(coll_mask_2: str) -> str:
    assert src.masks.get_mask_account(coll_mask_2) == "**4305"

import pytest

import src.masks


def test_get_mask_card_number(coll_mask_1: str) -> str:
    assert src.masks.get_mask_card_number(coll_mask_1) == "7000 79** **** 6361"
    # assert src.masks.get_mask_card_number(coll_mask_2) == "Это не карта"


def test_get_mask_account(coll_mask_2: str) -> str:
    assert src.masks.get_mask_account(coll_mask_2) == "**4305"

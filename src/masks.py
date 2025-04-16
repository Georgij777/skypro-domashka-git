def get_mask_card_number(card_number: str) -> str:
    """Функция, которая маскирует номер карты в формат ХХХХ ХХ** **** ХХХХ"""

    return card_number[0:4] + " " + card_number[4:6] + "**" + " " + "****" + " " + card_number[-4:]


def get_mask_account(account_number: str) -> str:
    """Функция, которая маскирует номер счёта и выводит последние четыре цифры"""

    return "**" + account_number[-4:]

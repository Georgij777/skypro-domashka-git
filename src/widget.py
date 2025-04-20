def mask_account_card(user_data: str) -> str | None:
    """Эта функция маскирует номер счёта или карты"""
    x = user_data.split(" ")

    if len(x[-1]) == 20:
        from src.masks import get_mask_account

        y = get_mask_account(x[-1])
        x[-1] = y


        return " ".join(x)
    elif len(x[-1]) != 20:
        from src.masks import get_mask_card_number
        y = get_mask_card_number(x[-1])
        x[-1] = y

        return " ".join(x)


def get_date(recipient_date: str) -> str:
    """Эта функция возвращает дату в формате ДД.ММ.ГГГГ."""
    x = recipient_date.split("-")
    y = x[2].split("T")
    day = y[0]
    month = x[1]
    year = x[0]
    date = day, month, year
    return f'ДД.ММ.ГГГГ ({day}.{month}.{year})'
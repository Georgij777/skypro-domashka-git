from src.masks import get_mask_card_number
from src.masks import get_mask_account

card_number = input("Введите номер карты: ")

account_number = input("Введите номер счёта: ")


print(get_mask_card_number(card_number))
print(get_mask_account(account_number))

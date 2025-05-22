# from src.masks import get_mask_card_number
# from src.masks import get_mask_account
#
# card_number = input("Введите номер карты: ")
#
# account_number = input("Введите номер счёта: ")
#
#
# print(get_mask_card_number(card_number))
# print(get_mask_account(account_number))

# from src.widget import mask_account_card
#
# user_data: str = input("Введите данные карты или счёта")
#
#
# print(mask_account_card(user_data))
#
#
# from src.widget import get_date
#
#
# print(get_date("2024-03-11T02:26:18.671407"))


# from transactions import transactions
# from src.generators import filter_by_currency
#
# y = filter_by_currency(transactions, 'USD')
# print(next(y))
# print(next(y))
# print(next(y))
# print(next(y))
#
# from src.generators import transaction_descriptions
#
# x = transaction_descriptions



from src.generators import card_number_generator


# for card_number in card_number_generator(12, 46):
#     print(card_number)

print(card_number_generator(12, 46))
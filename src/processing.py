def filter_by_state(, state:'EXECUTED'):
    """Эта функция возвращает данные по запросу: state == EXECUTED"""
    state_ex = []
    for data in users_data:
        if data.get('state') == 'EXECUTED':
            state_ex.append(data)
    return state_ex


def sort_by_date(,descending):
    """Сортирует по дате"""
    return sorted(users_data, key=lambda x: x.get('date', 0), reverse=descending)
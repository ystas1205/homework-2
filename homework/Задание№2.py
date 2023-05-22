import collections

cook_book = {
    'Омлет': [
        {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
        {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
        {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
    'Утка по-пекински': [
        {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
        {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
        {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
        {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
    'Запеченный картофель': [
        {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
        {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
        {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    ]
}


def get_shop_list_by_dishes(dishes, person_count):
    d = collections.defaultdict(int)
    list_dish = []
    for dish in dishes:
        for _ in cook_book[dish]:
            list_dish.extend([_['ingredient_name']])
            dict_dishes = {
                _['ingredient_name']: {'measure': _['measure'], 'quantity': _['quantity'] * person_count}
            }
            for i, j in dict_dishes.items():
                k = []
                k.append(j)
            for i in k:
                d[i['measure']] += i["quantity"]
    d = ([{'measure': k, 'quantity': v} for k, v in d.items()])
    for l_d, j in zip(list_dish, d):
        dict_dishes = {l_d: j}
        print(dict_dishes)


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

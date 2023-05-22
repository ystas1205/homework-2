from pprint import pprint

with open('123.txt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        c_b = line.strip()
        count = int(file.readline())
        dish = []
        for i in range(count):
            d = file.readline()
            ingredient_name, quantity, measure = d.strip().split('|')
            dish_ = {
                'ingredient_name': ingredient_name,
                'quantity':
                    quantity,
                'measure':
                    measure,
            }
            dish.append(dish_)
        file.readline()
        cook_book[c_b] = dish
    pprint(cook_book)

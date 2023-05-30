from pprint import pprint

file_path = 'recipes.txt'

def read_cook_book_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        menu = {}
        for line in file:
            dish_name = line[:-1]
            dish_count = file.readline().strip()
            ingridients_list = []
            for i in range(int(dish_count)):
                dish_items = dict.fromkeys(['ingredient_name', 'quantity', 'measure'])
                ingridient_name = file.readline().strip().split(' | ')
                for item in ingridient_name:
                    dish_items['ingredient_name'] = ingridient_name[0]
                    dish_items['quantity'] = ingridient_name[1]
                    dish_items['measure'] = ingridient_name[2]
                ingridients_list.append(dish_items)
                cook_book = {dish_name: ingridients_list}
                menu.update(cook_book)
            file.readline()
    return menu

def get_shop_list_by_dishes(dishes, person_count):
    menu = read_cook_book_in_file(file_path)
    necessary_ingredients = {}
    for dish in dishes:
        for item in menu[dish]:
            items_list = dict(
                [(item['ingredient_name'], {'measure': item['measure'], 'quantity': int(item['quantity']) * person_count})])
            if necessary_ingredients.get(item['ingredient_name']):
                additional_ingredient = (int(necessary_ingredients[item['ingredient_name']]['quantity']) +
                              int(items_list[item['ingredient_name']]['quantity']))
                necessary_ingredients[item['ingredient_name']]['quantity'] = additional_ingredient

            else:
                necessary_ingredients.update(items_list)
    print(f"Для приготовления блюд на {person_count} человек  нам необходимо купить:")
    pprint(necessary_ingredients)

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
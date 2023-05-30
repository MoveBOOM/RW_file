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
    pprint(menu)

read_cook_book_in_file(file_path)
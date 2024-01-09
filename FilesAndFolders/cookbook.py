import pprint

def get_cook_book(file):
    cook_book = {}
    line_id = 1
    with open(file, encoding='utf-8') as f:
        line = f.readline()
        while line:
            if line_id == 1:
                recipe_name = line.rstrip()
                line_id = 2
            else:
                ingredient_qty = int(line.rstrip())
                line = f.readline()
                ingredients = []
                for _ in range(ingredient_qty):
                    ingredient = line.rstrip().split(' | ')
                    ingredients.append({'ingredient_name': ingredient[0], 'quantity': int(ingredient[1]), 'measure': ingredient[2]})
                    line = f.readline()
                cook_book[recipe_name] = ingredients
                line_id = 1
            line = f.readline()
    return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    cook_book = get_cook_book('recipes.txt')
    for dishe in dishes:
        if dishe in cook_book:
            ingredients = cook_book[dishe]
            for ingredient in ingredients:
                ingredient_name = ingredient['ingredient_name']
                quantity = ingredient['quantity'] * person_count
                measure = ingredient['measure']
                if ingredient_name in shop_list:
                    shop_list[ingredient_name]['quantity'] += quantity
                    continue
                shop_list[ingredient_name] = {'measure': measure, 'quantity': quantity}
    return dict(sorted(shop_list.items()))
                

if __name__ == '__main__':
    pprint.pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
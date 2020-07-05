cook_book = {}
dish_list = []  # список блюд
dish_count = -1  # иницируем счетчик блюд
with open('recipes.txt', encoding='utf8') as f:
    for line in f:  # цикл по строкам
        dish_list.append(line.strip())  # читаем первую строку файла - названия блюд получаем
        inredients_count = int(f.readline().strip())  # читаем вторую строку файла
        dish_count += 1  # увеличиваем счетчик блюд на 1
        blank_dict = {}  # создаем временный словарь
        ingredients_list = []  # создаем список ингридиентов

        for index in range(inredients_count):  # цикл по ингридиентам  в диапазоне inredients_quantity
            ingridients = f.readline().strip().split(' | ')  # в каждой строке считываем ингридиенты
            blank_dict = {'ingredient_name': ingridients[0], 'quantity': int(ingridients[1]),
                             'measure': ingridients[2]}
            ingredients_list.append(blank_dict)  # добавляем в список ингридиентов словари
            cook_book[dish_list[dish_count]] = ingredients_list  # формируем словарь блюд

        f.readline()

print('Список блюд: ', cook_book)
print()

def get_shop_list_by_dishes(input_dishes, person_count):
    list_dishes = [] # создаем пустой список блюд
    for element in input_dishes: # проходим по списку
        list_dishes.append(element)

    for x in list_dishes: # проходим по списку
        if x in cook_book: # проверяем наличие элемента в cook_book
            pass

    shop_list_dict = {} # создаем словарь
    count = 1 # ставим счетчик

    for dish in list_dishes:
        for i in cook_book[dish]:
            shop_list_dict[i['ingredient_name']] = {'quantity': i['quantity'] * count * person_count,
                                                       'measure': i['measure']}

    print('Количество ингридиентов на блюда: ', shop_list_dict)


get_shop_list_by_dishes(['Утка по-пекински', 'Запеченный картофель'], 2)
# 1. Работа со словарями.
my_dict = {'Pasha': 1989, 'Vitya': 2001, 'Sergey': 1998}
print('Словарь: ', my_dict)
my_dict.update({'Kate': 1975,
                'Peter': 2007})
print('Существующее значение: ', my_dict.get('Pasha'))
print('Несуществующее значение: ', None)
print('Удалённое значение: ', my_dict.pop('Vitya'))
print('Измененный словарь: ', my_dict)
# 2. Работа со множествами.
my_set = {12, 'Arbiter', True}
print('Множество: ', my_set)
my_set.add(23.23)
my_set.add((5, 25))
my_set.remove(12)
print('Новое множество: ', my_set)

# key_list = ['Pasha', 'Vitya', 'Sergey']
# my_dict = dict(names)
# print(names)
# def names(*args):
#     if not args:
#         return None
# for names in key_list():
#     if key_list in names:
#         input('Введите имя: ')
#         print('Существующее значение: ', names.values())
# for key in names:
#     if key not in names and value not in names.values():
#         print('Несуществующее значение: ', None)


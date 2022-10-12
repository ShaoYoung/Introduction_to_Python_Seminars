# Семинар 6

import pprint

def mystr():
    return '555'
def nest():
    return [1,2,3]


my_dict = {
    'a': 'abc',
    'b': 'big',
    'name': 'Masha',
    'age': '25',
    mystr(): nest(),    # последняя запятая на всякий случай
    # nest(): mystr()   # нельзя, так как список - изменяемый объект
}

for k, v in my_dict.items():
    print(k, v)

x = my_dict.get('is car', 'default')# получить ключ словаря, если его нет, то возвращается default
                                    # в словарь ничего не добавляется
print(x)
print(my_dict)
my_dict.setdefault('is car', True)  # обращение к ключу, если его нет, то устанавливается значение

list1 = [1,2,3]
pprint.pprint(my_dict)      # должен выводить построчно ключ - значение
print(my_dict)

x = 100
print(f'x = {x}')   # Одинаково
print(f'{x = }')


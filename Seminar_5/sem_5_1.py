# Семинар 5
# 1. В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.

# поиск недостающего числа
def find_missing_number(number_list):
    for i in range(0, len(number_list)-1):
        if number_list[i]+1 != number_list[i+1]:
            return number_list[i]+1
    return None

file_name = 'file_5_1.txt'
with open(file_name, 'r') as data:
    string_list = data.read()

number_list = list(map(int, string_list.split()))
print(f'Список чисел из файла {file_name}: {number_list}')

missing_number = find_missing_number(number_list)
if missing_number:
    print(f'Среди чисел из файла {file_name} не хватает числа {missing_number}')
else:
    print(f'В файле {file_name} все числа удовлетворяют заданному условию!')
# Семинар 6
# 1.Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.
# Пример:
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;
# Добавьте возможность использования скобок, меняющих приоритет операций.
# Пример:
# 1+2*3 => 7;
# (1+2)*3 => 9;

# Метод eval() анализирует выражение, переданное этому методу,
# и запускает выражение (код) Python внутри программы.
# Проще говоря, функция eval() запускает код Python
# (который передается в качестве аргумента) в программе.
# Очень опасная функция !!! Обязательна проверка передаваемого выражения !!!

# Добавить проверку на корректность ввода в eval

operations_list = ['q2+2', '1+2*3', '1-2*3', '1+2*3', '(1+2)*3', '3.5*10']
av_symbol = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '/', '(', ')', '.', ',']

for i in range(0, len(operations_list)):
    # проверка каждого символа строки - элемента списка на наличие символа не из списка допустимых символов
    symbol = list(filter(lambda x: not x in av_symbol, operations_list[i]))
    if len(symbol):
        print(f'В строке {operations_list[i]} присутствуют недопустимые символы! Выполнение операции невозможно!')
        operations_list[i] = 'None'

for item in operations_list:
    print(eval(item))

from random import randint, uniform, choice
from string import ascii_letters

range_type = input('1 - генератор случайных целых чисел,\n2 - генератор случайных вещественных чисел,\n'
                   '3 - генератор случайных символов.\nВыберите один из генераторов: ')

if range_type == '1':
    left_range_limit = int(input('Левая граница диапазона (целое число): '))
    right_range_limit = int(input('Правая граница диапазона (целое число): '))
    if left_range_limit <= right_range_limit:
        result = randint(left_range_limit, right_range_limit)
        print(result)
    elif left_range_limit > right_range_limit:
        print('Значение левой границы диапазона превышает значения правой границы.')
elif range_type == '2':
    left_range_limit = float(input('Левая граница диапазона (вещественное число): '))
    right_range_limit = float(input('Правая граница диапазона (вещественное число): '))
    if left_range_limit <= right_range_limit:
        result = round(uniform(left_range_limit, right_range_limit), 1)
        print(result)
    elif left_range_limit > right_range_limit:
        print('Значение левой границы диапазона превышает значения правой границы.')
elif range_type == '3':
    left_range_limit = input('Левая граница диапазона (от a до z): ').lower()
    right_range_limit = input('Правая граница диапазона (от a до z): ').lower()
    first_let_idx = ascii_letters.find(left_range_limit)
    second_let_idx = ascii_letters.find(right_range_limit)
    if first_let_idx <= second_let_idx:
        result = choice(ascii_letters[first_let_idx:second_let_idx + 1])
        print(result)
    elif first_let_idx > second_let_idx:
        print('Нарушен алфавитный порядок границ диапазона символов.')
else:
    print(f'Генератор {range_type} отсутствует в списке генераторов.')

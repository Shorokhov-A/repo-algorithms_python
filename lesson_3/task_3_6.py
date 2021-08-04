from random import randint

list_1 = [randint(-5, 5) for _ in range(20)]

print(list_1)
min_el = list_1[0]
max_el = list_1[0]
for item in list_1:
    if item < min_el:
        min_el = item
    elif item > max_el:
        max_el = item

# Из списка list_1 создадим список элементов, в который не будут включены минимальный и максимальный элементы.
list_2 = []
for item in list_1:
    if min_el < item < max_el:
        list_2.append(item)

# Посчитаем сумму элементов списка list_2.
els_sum = sum(list_2)

print(f'Минимальный элемент массива: {min_el}\nМаксимальный элемент массива: {max_el}')
print(f'Сумма элементов массива, находящихся между минимальным и максимальным элементами: {els_sum}')

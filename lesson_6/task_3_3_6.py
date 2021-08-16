# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
from random import randint
from sys import getsizeof

list_1 = [randint(-5, 5) for _ in range(20)]

print(list_1)
min_el = list_1[0]
max_el = list_1[0]
for item in list_1:
    if item < min_el:
        min_el = item
    elif item > max_el:
        max_el = item

min_el_idx = []
max_el_idx = []
for idx in range(len(list_1)):
    if list_1[idx] == min_el:
        min_el_idx.append(idx)
    elif list_1[idx] == max_el:
        max_el_idx.append(idx)

for item in min_el_idx:
    list_1[item] = max_el
for item in max_el_idx:
    list_1[item] = min_el

print(list_1)
# Посчитаем объем памяти, выделенный под переменные в данной программе вручную, операясь на данные таблицы из методички.
# Переменная list_1 содержит 20 целых чисел. Одно целое число занимает в памяти 24 байта. Объём памяти, занимаемый
# списком рассчитывается по формуле 40 + 8 * длина списка. Соответственно, объем памяти, выделенный под список
# list_1 должен рассчитываться по формуле:
# 24 * 20 + (40 + 8 * 20) = 680 B = 0,68 kB
# Переменные min_el и max_el содержат целые числа и займут в памяти по 24 байта.
# В переменные min_el_idx и max_el_idx сохраняются индексы минимальных и максимальных элементов массива list_1.
# Подсчитать теоретический объем занимаемой ими памяти не представляется возможным, поскольку при каждом новом запуске
# данной программы генерируются новые случайные исходные данные.
# Попробуем вычислить объемы памяти, выделенный под переменные list_1, min_el, max_el, min_el_idx, max_el_idx
# средствами Python:
list_1_size = getsizeof(list_1[0]) * len(list_1) + getsizeof(list_1)
min_el_size = getsizeof(min_el)
max_el_size = getsizeof(max_el)
min_el_idx_size = getsizeof(min_el_idx[0]) * len(min_el_idx) + getsizeof(min_el_idx)
max_el_idx_size = getsizeof(max_el_idx[0]) * len(max_el_idx) + getsizeof(max_el_idx)
print(f'Объем памяти, занимаемый переменной list_1: {list_1_size} B')
print(f'Объем памяти, занимаемый переменной min_el: {min_el_size} B')
print(f'Объем памяти, занимаемый переменной max_el: {max_el_size} B')
print(f'Объем памяти, занимаемый переменной min_el_idx: {min_el_idx_size} B')
print(f'Объем памяти, занимаемый переменной max_el_idx: {max_el_idx_size} B')
# Результат расчёта средствами Python показал, что переменная list_1 заняла больше памяти, чем ожидалось.
# Так получилось потому, что типом данных для переменной list_1 является list comprehension, а не обычный список list.
# Тип данных list comprehension даёт выигрыш в скорости выполнения программы, но способствует большему расходу памяти.
# В качестве исходных данных мы могли бы использовать кортеж. Но условия задачи подразумевают внесение изменений в
# исходные данные, и в этом случае нам пришлось бы создавать дополнительную переменную, которая бы хранила массив
# исходных данных с учётом изменений, сделанных программой.
# Результаты вычисления объема памяти, занимаемого переменными min_el и max_el практически совпали с теоретическими
# расчётами.
# Индексы минимальных и максимальных элементов массива list_1 сохраняются в переменные min_el_idx и max_el_idx, имеющие
# тип данных list. Таким образом переменные min_el_idx и max_el_idx хранят динамические даные, получаемые в процессе
# работы программы. Для данных переменных могли бы использовать тип данных set. Но использование такого типа данных
# привело бы к повышению расхода памяти.
# Использование памяти в данной задаче считаю достаточно эффективным.
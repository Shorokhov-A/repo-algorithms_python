# Во втором массиве сохранить индексы четных элементов первого массива. Например, если
# дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 1,
# 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля), т.к. именно в этих позициях первого
# массива стоят четные числа.
from sys import getsizeof


numbers = (8, 3, 15, 6, 4, 2)
even_numbers_indices = []
for idx in range(len(numbers)):
    if numbers[idx] % 2 == 0:
        even_numbers_indices.append(idx)

print(numbers)
print(even_numbers_indices)
# Посчитаем объем памяти, выделенный под переменные в данной программе вручную, операясь на данные таблицы из методички.
# Переменная numbers содержит 6 целых чисел. Одно целое число занимает в памяти 24 байта. Объём памяти, занимаемый
# кортежем рассчитывается по формуле 24 + 8 * длина кортежа. Соответственно, объем памяти, выделенный под кортеж
# numbers должен рассчитываться по формуле:
# 24 * 6 + (24 + 8 * 6) = 216 B = 0,22 kB
# В результате работы программы в переменную even_numbers_indices запишется список, состоящий из четырёх целых чисел,
# являющихся индексами четырёх четных чисел из кортежа numbers. Объём памяти, занимаемый списком рассчитывается по
# формуле 40 + 8 * длина списка. Соответственно, объем памяти, выделенный под список even_numbers_indices должен
# рассчитываться по формуле:
# 24 * 4 + (40 + 8 * 4) = 168 B = 0,17 kB
# Попробуем вычислить объемы памяти, выделенный под переменные numbers и even_numbers_indices средствами Python:
numbers_size = getsizeof(numbers[0]) * len(numbers) + getsizeof(numbers)
even_numbers_indices_size = getsizeof(even_numbers_indices[0]) * len(even_numbers_indices) + \
                            getsizeof(even_numbers_indices)
print(f'Объем памяти, занимаемый переменной numbers: {numbers_size} B')
print(f'Объем памяти, занимаемый переменной even_numbers_indices: {even_numbers_indices_size} B')
# Результат расчёта средствами Python практически совпал с результатами теоретических расчётов.
# Кортеж numbers, содержащий исходные данные для работы программы, занимает меньше места, чем занимал бы список,
# содержащий эти же данные. Поэтому, если задача не предполагает внесение изменений в исходные данные, то хранение
# исходных данных в виде кортежа вполне целесообразно.
# Для хранения результата работы программы в переменной even_numbers_indices используется тип данных list, поскольку
# even_numbers_indices содержит динамическую информацию. В качестве типа данных для переменной even_numbers_indices
# могли бы использовать и множество, но множество заёмет в памяти больший объем, чем объем, который занимает список.
# Использование памяти в данной задаче считаю эффективным.
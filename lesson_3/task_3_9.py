from random import randint


# Функцию можно не рассматривать.
# Сюда помещен тот самый алгоритм красивости вывода матрицы на экран из решения восьмой задачи.
def show_matrix(matrix):
    print('Матрица:')
    max_el_len = 0
    first_negative_el = False
    for matrix_str in matrix:
        if not first_negative_el and matrix_str[0] < 0:
            first_negative_el = 1
        for el in matrix_str:
            if len(str(el)) > max_el_len:
                max_el_len = len(str(el))
    for matrix_str in matrix:
        el_str = ''
        if first_negative_el:
            el_str = ' '
        for el in matrix_str:
            max_space = max_el_len + 2
            if el < 0:
                el_str = el_str.rsplit(' ', 1)[0]
                max_space += 1
            el = str(el)
            el_str += ''.join(el)
            for _ in range(abs(len(el) - max_space)):
                el_str += ''.join(' ')
        el_str = el_str.rstrip()
        print(el_str)


matrix_5x4 = [[randint(-50, 50) for _ in range(4)]for _ in range(5)]
show_matrix(matrix_5x4)
# Можно снова писать циклы...
# Предлагаю почудить. Используя фишки Python сделаем решение задания максимально коротким.
# Решение выглядит, как издевательство над объемом функции красивости вывода матрицы на экран. )
columns_min_els = []
for column in zip(*[el for el in matrix_5x4]):
    columns_min_els.append(min(column))

max_among_min = max(columns_min_els)
print(f'Максимальный элемент среди минимальных элементов столбцов матрицы: {max_among_min}')

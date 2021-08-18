# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный
# случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный
# массивы
# ---------------------------------------------------------------------------------------------------------------------
from random import uniform, randint


def qsort_inplace(lst, start=0, end=None):
    def subpart(sub_lst, sub_start, sub_end, sub_pivot_index):
        sub_lst[sub_start], sub_lst[sub_pivot_index] = sub_lst[sub_pivot_index], sub_lst[sub_start]
        pivot = sub_lst[sub_start]
        sub_x = sub_start + 1
        sub_y = sub_start + 1
        while sub_y <= sub_end:
            if sub_lst[sub_y] <= pivot:
                sub_lst[sub_y], sub_lst[sub_x] = sub_lst[sub_x], sub_lst[sub_y]
                sub_x += 1
            sub_y += 1
        sub_lst[sub_start], sub_lst[sub_x - 1] = sub_lst[sub_x - 1], sub_lst[sub_start]
        return sub_x - 1
    if end is None:
        end = len(lst) - 1
    if end - start < 1:
        return
    pivot_index = randint(start, end)
    x = subpart(lst, start, end, pivot_index)
    qsort_inplace(lst, start, x - 1)
    qsort_inplace(lst, x + 1, end)


if __name__ == '__main__':
    my_array = [round(uniform(0, 50), 2) for _ in range(20)]
    print(my_array)
    qsort_inplace(my_array)
    print(my_array)

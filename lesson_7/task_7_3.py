# Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите
# в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части: в
# одной находятся элементы, которые не меньше медианы, в другой – не больше медианы.
# Задачу можно решить без сортировки исходного массива. Но если это слишком сложно, то
# используйте метод сортировки, который не рассматривался на уроках.
from random import randint


def median_seek(lst, idx=0):
    el = lst[idx]
    left_count = 0
    right_count = 0
    lst_side = (len(lst) - 1) / 2
    for i in range(len(lst)):
        if lst[i] <= el and idx != i:
            if left_count < lst_side:
                left_count += 1
        if lst[i] >= el and idx != i:
            if right_count < lst_side:
                right_count += 1
    if left_count == right_count:
        return el
    elif idx == len(lst) - 1:
        return 'Медиана не найдена.'
    idx += 1
    result = median_seek(lst, idx)
    return result


if __name__ == '__main__':
    m = 5
    n = 2 * m + 1
    my_array = [randint(0, 50) for _ in range(n)]
    print(my_array)
    print(sorted(my_array))
    print(median_seek(my_array))

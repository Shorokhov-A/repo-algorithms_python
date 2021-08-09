# Проанализировать скорость и сложность одного любого алгоритма, разработанных в
# рамках практического задания первых трех уроков.
# Данную задачу рассмотрим на примере задачи №5 из урока №3.
# Задача №3_5: в массиве найти максимальный отрицательный элемент. Вывести на экран его значение и
# позицию (индекс) в массиве.
from random import randint
from cProfile import run


def list_gen(n):
    return [randint(-50, 50) for _ in range(n)]


# Моя реализация данного алгоритма представлена функцией max_in_min_my().
# Сложность алгоритма в данном случае - O(n * log(n)).
def max_in_min_my(num_list):
    # print(num_list)
    negative_els = []
    for item in num_list:
        if item < 0:
            negative_els.append(item)

    if negative_els:
        max_negative_el = negative_els[0]
        for item in negative_els:
            if item > max_negative_el:
                max_negative_el = item

        max_el_idx = [idx for idx in range(len(num_list)) if num_list[idx] == max_negative_el]
        idx_str = ", ".join(map(str, max_el_idx))
        print(f'Максимальный отрицательный элемент в массиве: {max_negative_el}')
    else:
        print('В массиве отсутствуют отрицательные элементы.')


# Для сравнения существенно ухудшим алгоритм решения задачи №3_5, повысив его сложность до O(n^2).
# Алгоритм сложностью O(n^2) представлен в функции max_in_min_var_1().
# Данный алгоритм должен быть наихудшим вариантом. Сравнительные тесты сделаем ниже.
def max_in_min_var_1(num_list):
    # print(num_list)
    max_negative_el = num_list[0]
    for item in num_list:
        if item < 0:
            max_negative_el = item
            for el in num_list:
                if max_negative_el < el < 0:
                    max_negative_el = el

    if max_negative_el < 0:
        max_el_idx = [idx for idx in range(len(num_list)) if num_list[idx] == max_negative_el]
        idx_str = ", ".join(map(str, max_el_idx))
        print(f'Максимальный отрицательный элемент в массиве: {max_negative_el}')

    else:
        print('В массиве отсутствуют отрицательные элементы.')


# Вряд ли алгоритм решения данной задачи можно сделать менее сложным, чем O(n * log(n)).
# Попробуем улучшить мой алгоритм рещения задаи №3_5, используя возможности Python.
def max_in_min_var_2(num_list):
    # print(num_list)
    # Вместо цикла нахождения всех отрицательных элементов массива данных воспользуемся списковым включением.
    negative_els = [item for item in num_list if item < 0]

    if negative_els:
        # Максимальный элемент среди отрицательных элементов массива найдем функцией max().
        max_negative_el = max(negative_els)
        max_el_idx = [idx for idx in range(len(num_list)) if num_list[idx] == max_negative_el]
        idx_str = ", ".join(map(str, max_el_idx))
        print(f'Максимальный отрицательный элемент в массиве: {max_negative_el}')
    else:
        print('В массиве отсутствуют отрицательные элементы.')


# Также можно попробовать добиться более быстрой работы алгоритма, если организовать поиск нужного элемента только
# среди уникальных элементов массива.
def max_in_min_var_3(num_list):
    # Уникальные элементы массива данных получим путем преобразования массива в множество.
    # Остальные улучшения возьмем из предыдущей функции max_in_min_var_2().
    numbers = set(num_list)
    # print(numbers)
    negative_els = [item for item in numbers if item < 0]

    if negative_els:
        max_negative_el = max(negative_els)
        max_el_idx = [idx for idx in range(len(num_list)) if num_list[idx] == max_negative_el]
        idx_str = ", ".join(map(str, max_el_idx))
        print(f'Максимальный отрицательный элемент в массиве: {max_negative_el}')
    else:
        print('В массиве отсутствуют отрицательные элементы.')


# Есть предположение, что несмотря на все улучшения, все выше описанные алгоритмы будут иметь существенные ограничения
# на количество входных данных.
# Ради интереса попробуем написать алгоритм, который не будет зависеть от объема входных данных.
# Реализуем алгоритм поиска максимального отрицательного числа методом записи/чтения в файлы
# (запускать только в виртуальном окружении).
def array_to_file(n):
    with open('source.txt', 'w', encoding='utf-8') as f:
        for _ in range(n):
            number = str(randint(-50, 50))
            f.write(f'{number}\n')


def max_in_min_var_4():
    max_negative_el = []
    with open('source.txt', 'r', encoding='utf-8') as f:
        with open('negative_nums.txt', 'w', encoding='utf-8') as f_2:
            for line in f:
                if int(line) < 0:
                    f_2.write(line)
    with open('negative_nums.txt', 'r', encoding='utf-8') as f:
        for line in f:
            max_negative_el.append(int(line))
            if len(max_negative_el) > 1:
                max_negative_el.remove(min(max_negative_el))
    max_in_min_el = max_negative_el[0]
    print(f'Максимальный отрицательный элемент в массиве: {max_in_min_el}')
    with open('source.txt', 'r', encoding='utf-8') as f:
        # Запись позиций максимального отрицательного элемента в массиве данных в файл.
        with open('negative_nums_pos.txt', 'w', encoding='utf-8') as f_2:
            for count, line in enumerate(f):
                if int(line) == max_in_min_el:
                    f_2.write(f'{count}\n')


# Проверка №1.
list_1 = list_gen(20000)
run(f'max_in_min_my({list_1})')
run(f'max_in_min_var_1({list_1})')  # Как и предполагалось, алгоритм max_in_min_var_1() никуда не годится.
run(f'max_in_min_var_2({list_1})')

# Проверка №2.
# Небольшое преимущество имеет алгоритм max_in_min_var_3(). Он получился самым быстрым. Можно его назвать победителем
# по скорости работы. Тем не менее проверять работу всех трех алгоритмов массивом, включающим в себя 2 млн и более
# элементов я бы не рисковал.
# list_1 = list_gen(1000000)
# run(f'max_in_min_my({list_1})')
# run(f'max_in_min_var_2({list_1})')
# run(f'max_in_min_var_3({list_1})')

# Проверка №3. Неожиданный результат.
# И вот она - проверка алгоритма, работающего через чтение/запись в файлы.
# Этот алгоритм получился самым живучим. Спокойно обработает и 10 млн элементов массива даже на слабом железе.
# При этом алгоритм max_in_min_var_4(), работая с таким же количеством данных, как и алгоритмы max_in_min_my(),
# max_in_min_var_2(), max_in_min_var_3(), показал вполне конкурентноспособную скорость.
# array_to_file(2000000)
# run(f'max_in_min_var_4()')

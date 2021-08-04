matrix_5x4 = []
print('Укажите по 3 элемента каждой строки матрицы 5х4 целыми числами.\n'
      'Последний элемент каждой строки будет заполняться автоматически значениями '
      'суммы трех указанных элементов этой строки.')
for i in range(5):
    print(f'Строка №{i + 1}:')
    matrix_str = []
    for j in range(3):
        number = int(input(f'элемент №{j + 1}: '))
        matrix_str.append(number)
    fourth_el = sum(matrix_str)
    matrix_str.append(fourth_el)
    matrix_5x4.append(matrix_str)

# Все дальнейшие действия требуют пояснения и нужны только для красоты вывода матрицы на экран.
# Найдем наибольшую длину элемента среди элементов матрицы.
# Эта длина понадобится для вычислелия длины пробела между элементами матрицы.
max_el_len = 0
# Предусмотрим индикатор наличия отрицательного элемента в начале любой строки матрицы.
# Он нам пригодится, чтобы добавить пробельный символ в начало каждой строки при выводе матрицы на экран в случае,
# если любая из строк матрицы начинается с отрицательного числа.
first_negative_el = False
for matrix_str in matrix_5x4:
    if not first_negative_el and matrix_str[0] < 0:
        first_negative_el = True
    for el in matrix_str:
        if len(str(el)) > max_el_len:
            max_el_len = len(str(el))

print('Матрица 5х4:')
for matrix_str in matrix_5x4:
    el_str = ''
    if first_negative_el:
        el_str = ' '
    for el in matrix_str:
        max_space = max_el_len + 2  # Вычисляем длину пробела между элементами матрицы.
        # Если элемент отрицательный, то убираем из строки последний пробельный символ перед этим элементом
        # и увеличиваем max_space на единицу.
        if el < 0:
            el_str = el_str.rsplit(' ', 1)[0]
            max_space += 1
        el = str(el)
        el_str += ''.join(el)
        for _ in range(abs(len(el) - max_space)):
            el_str += ''.join(' ')
    el_str = el_str.rstrip()
    print(el_str)

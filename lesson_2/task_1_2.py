# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
natural_num = int(input('Введите натуральное число: '))
# Зададим счётчики чётных и нечетных цифр.
even_num_count = 0
odd_num_count = 0
# Создадим списки чётных и нечетных цифр. Они нужны только для красоты вывода.
even_num = []
odd_num = []

if natural_num >= 0:
    while True:
        digit = natural_num % 10
        natural_num = natural_num // 10
        if digit % 2 == 0:
            even_num.append(digit)
            even_num_count += 1
        else:
            odd_num.append(digit)
            odd_num_count += 1
        if natural_num == 0:
            break
# Работаем над красотой вывода.
# Если чётные или нечётные цифры есть, то они будут выведены на экран в скобках после их количества.
    even_num.reverse()
    odd_num.reverse()
    even_num_str = f'({", ".join(map(str, even_num))})'
    odd_num_str = f'({", ".join(map(str, odd_num))})'
    if not even_num:
        even_num_str = ''
    elif not odd_num:
        odd_num_str = ''
    print(f'Количество четных цифр: {even_num_count} {even_num_str}\n'
          f'Количество нечетных цифр: {odd_num_count} {odd_num_str}')
else:
    print(f'Число {natural_num} не является натуральным.')

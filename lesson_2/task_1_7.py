# Напишите программу, доказывающую или проверяющую, что для множества натуральных
# чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число.
number = int(input('Введите натуральное число: '))
if number >= 0:
    expression_1 = 0
    expression_2 = number * (number + 1) / 2
    item = 0

    for _ in range(number):
        item += 1
        expression_1 += item

    print(f'{expression_1} = {expression_2}')
else:
    print(f'Число {number} не является натуральным.')

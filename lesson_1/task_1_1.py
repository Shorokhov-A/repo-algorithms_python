number = input('Введите трехзначное число: ')

if number.isdigit() and len(number) == 3 and int(number[0]) != 0:
    a = int(number[0])
    b = int(number[1])
    c = int(number[2])
    digits_sum = a + b + c
    digits_product = a * b * c
    print(f'Сумма цифр: {digits_sum} \nПроизведение цифр: {digits_product}')
else:
    print('Ошибка ввода данных.')

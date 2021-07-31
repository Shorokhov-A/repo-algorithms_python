# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.
number = int(input('Введите целое число: '))
result = ''
if number < 0:
    result = '-'
    number = abs(number)

while True:
    digit = number % 10
    result += str(digit)
    number = number // 10
    if number == 0:
        break
result = int(result)
print(f'Обратное число: {result}')

# Посчитать, сколько раз встречается определенная цифра в введенной последовательности
# чисел. Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом
# с клавиатуры.
numbers_amount = int(input('Укажите количество чисел в последовательности: '))
while True:
    target_digit = int(input('Укажите цифру, которую необходимо посчитать в последовательности чисел: '))
    target_digit = abs(target_digit)
    if target_digit // 10 == 0:
        break
    print('Ошибка ввода. Необходимо указать только одну цифру.')

count = 0
print('Последовательность чисел: ')
for _ in range(abs(numbers_amount)):
    user_enter = int(input())
    if user_enter < 0:
        user_enter = abs(user_enter)
    while True:
        digit = user_enter % 10
        user_enter = user_enter // 10
        if digit == target_digit:
            count += 1
        if user_enter == 0:
            break

print(f'Цифра {target_digit} встречается {count} раз(а).')

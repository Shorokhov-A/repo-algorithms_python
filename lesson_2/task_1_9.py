# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.
print('Задайте последовательность натуральных чисел.\nДля завершения  ввода нажмите "enter".\n'
      'Последовательность натуральных чисел:')
max_sum = 0
max_sum_nums = []
count = 0
while True:
    user_enter = input('')
    if not user_enter:
        break
    elif user_enter.isdigit() and int(user_enter) >= 0:
        digits_sum = 0
        number = int(user_enter)
        count += 1
        while True:
            digit = number % 10
            number = number // 10
            digits_sum += digit
            if number == 0:
                break
        if digits_sum > max_sum:
            max_sum = digits_sum
            max_sum_nums.clear()
            max_sum_nums.append(user_enter)
        elif digits_sum == max_sum:
            max_sum_nums.append(user_enter)
    else:
        print(f'Число {user_enter} не является натуральным.')

if count > 0:
    print(f'Количество чисел, равных между собой по максимальной сумме цифр: {len(max_sum_nums)}\n'
          f'Наибольшие числа по сумме цифр: {", ".join(map(str, max_sum_nums))}\n'
          f'Сумма цифр: {max_sum}')
print('Конец программы.')

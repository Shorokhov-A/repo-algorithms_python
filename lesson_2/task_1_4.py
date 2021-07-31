# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.
el_number = int(input('Количество элементов (n): '))
el_sum = 0
first_el = 1

for _ in range(el_number):
    el_sum += first_el
    first_el /= -2

print(f'Сумма {el_number} элементов ряда: {el_sum}')

from random import randint

list_1 = [randint(1, 5) for _ in range(20)]

print(list_1)
max_count = 0
max_count_els = []
for idx in range(len(list_1)):
    count = list_1.count(list_1[idx])
    if count > max_count:
        max_count = count
        max_count_els.clear()
        max_count_els.append(list_1[idx])
    elif count == max_count and (list_1[idx] not in max_count_els):
        max_count_els.append(list_1[idx])

numbers_str = ', '.join(map(str, max_count_els))
print(f'Максимальное количество вхождений одного числа: {max_count}\n'
      f'Числа, которые встречаются в массиве максимальное количество раз: {numbers_str}')

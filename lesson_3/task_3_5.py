numbers = (-5, -18, -10, 0, 5, 12, -3, -11, -19, -7, -3)
print(numbers)
max_negative_el = numbers[0]
for item in numbers:
    if max_negative_el < item < 0:
        max_negative_el = item

max_el_idx = [idx for idx in range(len(numbers)) if numbers[idx] == max_negative_el]
print(f'Максимальный отрицательный элемент в массиве: {max_negative_el}\n'
      f'Позиция элементов в массиве: {", ".join(map(str, max_el_idx))}')

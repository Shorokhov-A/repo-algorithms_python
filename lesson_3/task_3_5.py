numbers = (5, -5, -18, -10, 0, 5, 12, -3, -11, -19, -7, -3)
print(numbers)
negative_els = []
for item in numbers:
    if item < 0:
        negative_els.append(item)

if negative_els:
    max_negative_el = negative_els[0]
    for item in negative_els:
        if item > max_negative_el:
            max_negative_el = item

    max_el_idx = [idx for idx in range(len(numbers)) if numbers[idx] == max_negative_el]
    print(f'Максимальный отрицательный элемент в массиве: {max_negative_el}\n'
          f'Позиция элементов в массиве: {", ".join(map(str, max_el_idx))}')
else:
    print('В массиве отсутствуют отрицательные элементы.')

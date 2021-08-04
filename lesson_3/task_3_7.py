from random import randint

list_1 = [randint(-5, 5) for _ in range(20)]
print(list_1)
result = []
for item in list_1:
    result.append(item)
    if len(result) > 2:
        max_el = result[0]
        for idx in range(len(result)):
            if result[idx] > max_el:
                max_el = result[idx]
        result.remove(max_el)

result_str = ', '.join(map(str, result))
print(f'Два наименьших элемента массива: {result_str}')

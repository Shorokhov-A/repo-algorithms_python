from random import randint

list_1 = [randint(-5, 5) for _ in range(20)]

print(list_1)
min_el = list_1[0]
max_el = list_1[0]
for item in list_1:
    if item < min_el:
        min_el = item
    elif item > max_el:
        max_el = item

min_el_idx = []
max_el_idx = []
for idx in range(len(list_1)):
    if list_1[idx] == min_el:
        min_el_idx.append(idx)
    elif list_1[idx] == max_el:
        max_el_idx.append(idx)

for item in min_el_idx:
    list_1[item] = max_el
for item in max_el_idx:
    list_1[item] = min_el

print(list_1)

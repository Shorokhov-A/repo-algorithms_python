numbers = (8, 3, 15, 6, 4, 2)
even_numbers_indices = []
for idx in range(len(numbers)):
    if numbers[idx] % 2 == 0:
        even_numbers_indices.append(idx)

print(numbers)
print(even_numbers_indices)

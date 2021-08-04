result = {}
for number in range(2, 100):
    for divisor in range(2, 10):
        multiples_list = []
        result.setdefault(divisor, multiples_list)
        if number % divisor == 0:
            result[divisor].append(number)

for key, val in result.items():
    multiples_str = ", ".join(map(str, val))
    print(f'Количество чисел от 2 до 99, кратных {key}: {len(val)}. Кратные числа: {multiples_str}')

year = int(input('Введите год: '))

if year % 4 == 0:
    if year % 100 == 0 and year % 400 != 0:
        print(f"Год {year} невисокосный")
    else:
        print(f"Год {year} високосный")
else:
    print(f"Год {year} невисокосный")

ax = int(input('Введите координату x точки А: '))
ay = int(input('Введите координату y точки А: '))
bx = int(input('Введите координату x точки B: '))
by = int(input('Введите координату y точки B: '))

if bx != ax:
    k = (by - ay) / (bx - ax)
    b = ay - ax * k
    if k == 0:
        print(f'y = {b}')
    elif b == 0:
        print(f'y = {k}x')
    elif b < 0:
        b *= -1
        print(f'y = {k}x - {b}')
    else:
        print(f'y = {k}x + {b}')
else:
    print(f'x = {ax}')

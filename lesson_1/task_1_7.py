line_segment_1 = int(input('Введите длину первого отрезка (целое число): '))
line_segment_2 = int(input('Введите длину второго отрезка (целое число): '))
line_segment_3 = int(input('Введите длину третьего отрезка (целое число): '))

if line_segment_1 < (line_segment_2 + line_segment_3) and line_segment_2 < (line_segment_1 + line_segment_3) and \
        line_segment_3 < (line_segment_1 + line_segment_2):
    if line_segment_1 == line_segment_2 == line_segment_3:
        print(f'Треугольник со сторонами {line_segment_1} {line_segment_2} {line_segment_3} - равносторонний')
    elif line_segment_1 == line_segment_2 or line_segment_1 == line_segment_3 or line_segment_2 == line_segment_3:
        print(f'Треугольник со сторонами {line_segment_1} {line_segment_2} {line_segment_3} - равнобедренный')
    else:
        print(f'Треугольник со сторонами {line_segment_1} {line_segment_2} {line_segment_3} - разносторонний')
else:
    print(f'Построение треугольника со сторонами {line_segment_1} {line_segment_2} {line_segment_3} невозможно')

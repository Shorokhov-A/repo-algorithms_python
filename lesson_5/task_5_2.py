# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое
# число представляется как коллекция, элементы которой это цифры числа.
# Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
# ---------------------------------------------------------------------------------------------------
# Много времени ушло на то, чтобы вспомнить, как складывать и умножать шестнадцатиричные счисла.
# В даной программе успел лишь выразить свое понимание данных операций в виде алгоритмов. Сделал решение "в лоб".
# Специализированные типы коллекции из модуля Collections попробовать применить не успеваю.
# Циклы в циклах... Мамочки... Наверное здесь стоило бы подумать над оптимизацией.
# Вместо кортежа HEX_ELS возможно стоило поработать со словарем. Но в этом случае, исходя из логики моих алгоритмов,
# скорее всего понадобился бы еще один словарь, содержащий реверсированные элементы "ключ: значение".
# Тем не менее программа работает корректно. Результаты вычислений от перестановки мест слагаемых и множителей
# не изменяются. Хотя в процессе написания алгоритмов были и такие варианты.)
HEX_ELS = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F')


def hex_sum(*hex_nums):
    int_div = 0
    result = []
    for number in hex_nums:
        hex_num_1 = result[:]  # Здесь можно было попробовать использовать метод copy() вместо среза [:].
        hex_num_2 = number[:]  # Здесь также можно было попробовать использовать метод copy().
        result.clear()
        while len(hex_num_1) or len(hex_num_2):
            item_1 = '0'
            item_2 = '0'
            if not len(hex_num_2):
                item_1 = hex_num_1.pop()
            elif not len(hex_num_1):
                item_2 = hex_num_2.pop()
            else:
                item_1 = hex_num_1.pop()
                item_2 = hex_num_2.pop()
            sum_els = HEX_ELS.index(item_1) + HEX_ELS.index(item_2) + int_div
            if int_div:
                int_div = 0
            rem_div = sum_els % 16
            result.append(HEX_ELS[rem_div + int_div])
            int_div = sum_els // 16
        if int_div:
            result.append(str(int_div))
        result.reverse()
    return result


def hex_mul(*hex_nums):
    int_div = 0
    numbers = []
    result = []
    for number in hex_nums:
        hex_num_1 = result[:]  # Стоило бы попробовать copy().
        if not hex_num_1:
            hex_num_1.append('1')
        hex_num_2 = number[:]  # Замечание, аналогичное трем предыдущим.
        hex_num_1.reverse()
        hex_num_2.reverse()
        numbers.clear()
        result.clear()
        count = 0
        for item_1 in hex_num_1:
            tmp = []
            for _ in range(count):
                tmp.append('0')
            for item_2 in hex_num_2:
                els_mul = HEX_ELS.index(item_1) * HEX_ELS.index(item_2) + int_div
                if int_div:
                    int_div = 0
                rem_div = els_mul % 16
                tmp.append(HEX_ELS[rem_div + int_div])
                int_div = els_mul // 16
            if int_div:
                tmp.append(str(int_div))
                int_div = 0
            tmp.reverse()
            numbers.append(tmp)
            count += 1
        result = hex_sum(*numbers)
    return result


if __name__ == '__main__':
    first_number = ' '.join(input('Первое число: ')).upper().split()
    second_number = ' '.join(input('Второе число: ')).upper().split()
    print(first_number, second_number)
    result_sum = hex_sum(first_number, second_number)
    result_sum_str = ''.join(map(str, result_sum))
    result_mul = hex_mul(first_number, second_number)
    result_mul_str = ''.join(map(str, result_mul))
    print(f'Результат сложения: {result_sum_str}')
    print(f'Результат умножения: {result_mul_str}')

# Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем. После выполнения вычисления программа не
# должна завершаться, а должна запрашивать новые данные для вычислений. Завершение
# программы должно выполняться при вводе символа '0' в качестве знака операции. Если
# пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна сообщать ему об
# ошибке и снова запрашивать знак операции. Также сообщать пользователю о невозможности
# деления на ноль, если он ввел 0 в качестве делителя.
def operations():
    while True:
        operation_sign = input('Знак операции: ')
        if operation_sign in ('0', '+', '-', '*', '/'):
            break
        print(f'Ошибка операции вычисления. Операция  {operation_sign} не предусмотрена.')
    return operation_sign


while True:
    operation = operations()
    if operation == '0':
        print('Завершение программы.')
        break
    first_number = float(input('Первое число: '))
    second_number = float(input('Второе число: '))
    if operation == '+':
        print(f'{first_number} + {second_number} = {first_number + second_number}')
    elif operation == '-':
        print(f'{first_number} - {second_number} = {first_number - second_number}')
    elif operation == '*':
        print(f'{first_number} * {second_number} = {first_number * second_number}')
    elif operation == '/':
        if second_number == 0:
            print('Деление на ноль невозможно.')
        else:
            print(f'{first_number} : {second_number} = {first_number / second_number}')

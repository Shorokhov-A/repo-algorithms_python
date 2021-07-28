from string import ascii_lowercase

letter_number = input('Введите номер буквы латинского алфавита (от 1 до 26): ')

if letter_number.isdigit() and int(letter_number) <= 26:
    letter_number = int(letter_number)
    letter = ascii_lowercase[letter_number - 1]
    print(f'Порядковому номеру {letter_number} в латинском алфавите соответствует буква {letter}')
else:
    print('Введено некорректное значение порядкового номера буквы.')

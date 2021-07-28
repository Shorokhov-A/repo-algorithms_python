from string import ascii_lowercase

first_letter = input('Укажите первую букву (от a до z): ')
second_letter = input('Укажите вторую букву (от a до z): ')

first_letter_pos = ascii_lowercase.find(first_letter.lower()) + 1
second_letter_pos = ascii_lowercase.find(second_letter.lower()) + 1
letters_num = second_letter_pos - first_letter_pos - 1
if first_letter_pos == second_letter_pos:
    letters_num = second_letter_pos - first_letter_pos
elif first_letter_pos > second_letter_pos:
    letters_num = abs(second_letter_pos - first_letter_pos) - 1

print(f'Порядковый номер буквы {first_letter} в алфавите: {first_letter_pos}\n'
      f'Порядковый номер буквы {second_letter} в алфавите: {second_letter_pos}\n'
      f'Количество букв между {first_letter} и {second_letter}: {letters_num}')

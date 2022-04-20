# Задача 5
# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
alfabet='abcdefghijklmnopqrstuvwxyz'

letter_1 = input('Введите первую  букву: ')
letter_2 = input('Введите вторую букву: ')

pos_letter_1 = alfabet.find(letter_1)
pos_letter_2 = alfabet.find(letter_2)

if pos_letter_2> pos_letter_1:
    diff= pos_letter_2 - pos_letter_1 - 1
else:
    diff = pos_letter_2 - pos_letter_1 - 1

print(f'Первая буква {letter_1}, на позиции: {pos_letter_1}')
print(f'Вторая буква {letter_2}, на позиции: {pos_letter_2}')
print(f'Между ними {diff} букв')



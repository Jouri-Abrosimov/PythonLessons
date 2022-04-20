# Задача 6
# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
alfabet=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')

position = int(input('Введите позицию буквы в лат.алфавите : '))
if position < len(alfabet):
    letter = alfabet[position]
    print(f'Буква : {letter}')
else:
    print('Нет такой буквы в алфавите')

# Задача 9.
# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).'''

num1 = int(input('Введите первое число : '))
num2 = int(input('Введите второе число : '))
num3 = int(input('Введите третье число : '))

if num2 < num1 < num3 or num3 < num1 < num2:
    print(f'Среднее: {num1}')
elif num1 < num2 < num3 or num3 < num2 < num1:
    print(f'Среднее: {num2}')
else:
    print(f'Среднее: {num3}')


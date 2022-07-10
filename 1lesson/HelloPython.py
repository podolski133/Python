# print('hello world')

# типы данных и переменная

# int, float, boolean, str, list, None
# value = None
# print(type(value))
# print(type(a))
# print(type(b))
# value = 12334
# print(type(value))
# s = 'hello world'
# a = 123
# b = 1.23
# print(s) # вывод строки
# print(a, '-',b, '-', s) # способы вывода:
# print('{1} - {2} - {0}'.format(a, b, s))
# print(f'{a} - {b} - {s}')

# f = False
# print(f)
# list = ['1', '2', '3']
# col = ['hello', 1,2,4.5,True]
# print(list)
# print(col)

# Ввод и вывод данных
# print, input

# print('Введите a'); # приглашение к вводу
# a = int(input()) # присваиваем число или слово к "a"
# print('Введите b');
# b = int(input())
# print(a, '+' , b, '=', a + b)
# print('{} {}'.format(a, b))
# print(f'{a} {b}')

# Арифметические операции
# +, -, *, /, %, //, **
# **, *, /, //, %, +, -
# (), Сокращенные операции

#a = 1.3
#b = 3
#c = round(a * b, 5) 
#print(c)

# round типо округление (пример, 1,3*3=3,900000081, включаем round и будет 3,9)
# c = a / b = 0.25 (операция деления работает как для вещественных чисел)
# c = a // b = 1 (деление целых чисел)
# % - (остаток от деления)
# с = a ** b (возведение в степень)

# a = 3
# a = a + 5 # либо так a += 5 (так же это работает и для других *= и т.д.)
# print(a)

# Логические операции
# >, >=, <=, == (сравнение), != (не равенство)
# not, and, or - не путать с &, |, ^
# is, is not, in, not in
# gen

# func = 1
# T = 4
# x = 2
# print(func<T>(x))

# f = 1 > 2 or 4 < 6
# print(f)

# f = [1,2,3,4]
# print(f)
## print(2 in f) # содержание 2 в списке f (результат True)
# print(not 2 in f) # либо отрицание 2
# проверяем факт четности числа:
# is_odd = f[0] % 2 == 0 # находим остаток от деления на 2 равен (==) 0
# print(is_odd) # будет False так как 1 не чётная

# либо через отрицания not так:

f = [1,2,3,4]
is_odd = not f[0] % 2 
print(is_odd) # будет False так как 1 не чётная
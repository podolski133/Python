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

# f = [1,2,3,4]
# is_odd = not f[0] % 2 
# print(is_odd) # будет False так как 1 не чётная

# Управляющие конструкции
# if, if-else

# нахождения максимума из двух чисел:
# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)

# применение elif:

# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же МАША!')
# elif username == 'Марина':
#     print('Я так ждала Вас, Марина!')
# elif username == 'Ильнар':
#     print('Ильнар - топ')
# else:
#     print('Привет, ', username)


# Управляющие конструкции: while

# original = 23
# inverted = 0
# делаем инвертируемое число:
# while original != 0: # не равен 0
#     # далее компануем перевернутое число
#     inverted = inverted * 10 + (original % 10)
#     # и целочисленное делим на 10
#     original //= 10
# print(inverted)

# while-else
# выполняется в том случае когда основной тело цикла перестает работать 

# original = 23
# inverted = 0
# while original != 0: # не равен 0
#      # далее компануем перевернутое число
#      inverted = inverted * 10 + (original % 10)
#      # и целочисленное делим на 10
#      original //= 10
# else:
#     print('Пожалуй')
#     print('хватит )')
# print(inverted)


# Управляющие конструкции: for

# for i in 1,2,3,4,5:
#    print(i**2) # демонстрация квадрата этих чисел
# получаем 1 4 9 16 25

# либо так 

# list = [1,2,3,4,5]
# for i in list:
#     print(i**2)

# range
# r = range(10)
# for i in r:
#     print(i)
# выведет от 0 до 9

# либо так:
# for i in range(10): # либо указываем диапазон (1, 5)
#     print(i)
# выведет от 0 до 9

# Немного о строках:

# text = 'съешь ещё этих мягких французских булок'
# print(len(text)) # кол-во символов в строке = 39
# print('ещё' in text) # проверяем какое либо слово в строке = True
# print(text.isdigit()) # проверяем являются ли все строки числами = False
# print(text.islower()) # или являются символами нижнего регистра
# print(text.replace('ещё' , 'ЕЩЁ')) # или например мы что то хотим заменить
# for c in text:
#     print(c)



# help(text.istitle)  -- данная команда подсказывает что это такое


# Срезы

# text = 'съешь ещё этих мягких французских булок'
# print(text[0])                               # c
# print(text[1])                               # ъ
# print(text[len(text)])                       # IndexError        
# print(text[len(text)-1])                     # к
# print(text[-5])                              # б
# print(text[:])                               # съешь ещё этих мягких французких булок
# print(text[len(text)-2:])                    # ок
# print(text[2:9])                             # ешь ещё
# print(text[6:-18])                           # ещё этих мягких
# print(text[0:len(text):6])                   # сеикакл
# print(text[::6])                             # сеикакл
# text = text[2:9] + text[-5] + text[:2]       # ...


# Списки
## list = list

# numbers = [1, 2, 3, 4, 5]
# print(numbers)
# ran = range(1, 6)
# numbers = list(ran)
# print(numbers)
# numbers[0] = 10
# print(numbers)
# for i in numbers:
#     i *= 2
#     print(i)
# print(numbers)


# Функции

def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

arg = 2.3
print(type(f(arg)))

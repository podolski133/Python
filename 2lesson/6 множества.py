# Множества

# colors = {'red', 'green', 'blue'}

# print(colors)  # {'blue', 'red', 'green'}  каждый  раз список перемешивается
# colors.add('red') # {'blue', 'red', 'green'}
# colors.add('gray')
# print(colors) # {'blue', 'gray', 'red', 'green'}
# colors.remove('red')
# print(colors) # {'green', 'blue', 'gray'}

# # colors.remove('red')  # KeyError: 'red'
# colors.discard('red')  # ok

# colors.clear()  # { }  можно очистить множество
# print(colors)  # set()


# Доп

a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy()            # c = {1, 2, 3, 5, 8}
u = a.union(b)          # u = {1, 2, 3, 5, 8, 13, 21} - объединение множест
i = a.intersection(b)   # i = {8, 2, 5} - пересечение
dl = a.difference(b)    # dl = {1, 3}
dr = b.difference(a)    # dr = {13, 21}

q = a \
    .union(b) \
    .difference(a.intersection(b))
#  {1, 21, 3, 13

# неизменяемые множства
s = frozenset(a)
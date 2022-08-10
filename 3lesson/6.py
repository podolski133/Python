# Улучшенная версия от 5 файла
# Пример: 1 2 3 5 8 15 23 38 
# Получить: [(2, 4), (8, 64), (38, 1444)]

def select(f, col):
    return [f(x) for x in col]

def where(f, col):
    return [x for x in col if f(x)]

data = '1 2 3 5 8 15 23 38'.split()

res = select(int, data) # [1, 2, 3, 5, 8, 15, 23, 38]
res = where(lambda x: not x % 2, res) # [2, 8, 38]
res =  select(lambda x: (x, x**2), res) # [(2, 4), (8, 64), (38, 1444)]
print(res)

# Либо так:
# def where(f, col):
#     return [x for x in col if f(x)]

# data = '1 2 3 5 8 15 23 38'.split()

# res = map(int, data) # [1, 2, 3, 5, 8, 15, 23, 38]
# res = where(lambda x: not x % 2, res) # [2, 8, 38]  # заменяем where на filter
# res =  list(map(lambda x: (x, x**2), res)) # [(2, 4), (8, 64), (38, 1444)]
# print(res)
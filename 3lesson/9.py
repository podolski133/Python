# Функция filter

data = [x for x in range(10)]

res = list(filter(lambda x: not x % 2, data))
print(res) # [0, 2, 4, 6, 8]
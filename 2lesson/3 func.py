# def new_string(symbol, count):
#     return symbol * count
# print(new_string('!', 5)) # !!!!!
# print(new_string('!')) # TypeError: new_string() missing 1 required positional argument: 'count'

#def new_string(symbol, count = 3):
#    return symbol * count
# print(new_string('!', 5)) # !!!!!
# print(new_string('!')) # !!!
# print(new_string(4)) # 4*3=12

# возможность передачи неограниченного кол-ва аргументов в функции

def concatenatio(*params):  # перед аргументом ставим *
    res: str = ""  # 
    for item in params:  # 
        res += item  # 
    return res  # 
# склеивание строк
print(concatenatio('a', 's', 'd', 'w'))  # asdw
print(concatenatio('a', '1', 'd', '2'))  # a1d2
# print(concatenatio(1, 2, 3, 4))  # TypeError ... Либо что бы работало то вот:

# def concatenatio(*params):
#     res = 0
#     for item in params:
#         res += item
#     return res
# print(concatenatio(1, 2, 3, 4)) # 10


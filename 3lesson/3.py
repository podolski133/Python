sum = lambda x, y: x+y    # либо так -> def sum(x, y):
                          #                 return x+y

mylt = lambda x, y: x*y   # либо так -> def mylt(x, y):
                          #                 return x*y

def calc(op, a, b):
    print(op(a, b))
    # return op(a, b)

calc(mylt, 4, 5) # 20
calc(sum, 4, 5) # 9  

# Либо просто в одну строку:
# calc(lambda x, y: x+y, 4, 5) -> 9
# calc(lambda x, y: x*y, 4, 5) -> 20
def f(x):
    return x**2

g = f

# print(type(f))
# print(type(g))

# print(f(4))
# print(g(4)) 

def calc1(x):
    return x+10
# print(calc1(10))

def calc2(x):
    return x-10
# print(calc2(10))

def calc4(x):
    return x**2
# print(calc4(10))

def calc5(x):
    return x//2
# print(calc5(10))

def calc6(x):
    return x/2
# print(calc6(10))

def calc3(x):
    return x*10
# print(calc3(10))

def math(op, x):
    print(op(x))
math(calc3, 10) # 100
math(calc6, 10) # 5.0
math(calc4, 10) # 100
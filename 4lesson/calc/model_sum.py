x = 0
y = 0

# метод отвечающий за инициализацию x, y
def init(a, b):
    global x
    global y
    x = a
    y = b
# метод отвечающий за складывания x, y
def do_it(): 
    return x + y
#write a fun that accept another fun & applies it 2 numbers



def apply_operation(func, x, y):
    return func(x, y)

def add(a, b):
    return a + b

print(apply_operation(add,5,3))

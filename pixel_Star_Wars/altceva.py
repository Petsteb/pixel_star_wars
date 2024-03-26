def a(x):
    if(x < 1):
        return x
    return a(x - 1) + a(x - 2)

def b(x):
    if(x <= 1):
        return 1
    return 2 * b(x / 2)

def c(x):
    if(x < 0):
        return 0
    return 1 + c(x - 10)

print(a(123456789))
print(b(123456789))
print(c(123456789))
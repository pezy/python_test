def hello():
    print 'hello'

hello();

def maximum(a, b):
    if a < b:
        return b
    elif a == b:
        pass
    else:
        return a

print maximum(2, 3);
print maximum(3, 3);
print maximum(5, 4);

x = 5

def func():
    global x
    print 'x is', x
    x = 3
    print 'changed local x to', x

func()
print 'value of x is', x

def say(message, times=1):
    print message * times

say('hello')
say('world', 4)

def abc(a, b=3, c=5):
    print 'a is', a, 'and b is', b, 'and c is', c

abc(1, 4)
abc(1, c=7)
abc(c=8, a=9)

def total(initial=5, *numbers, **keywords):
    count = initial
    for number in numbers:
        count += number
    for key in keywords:
        count += keywords[key]
    return count

print total(10, 1, 2, 3, vegetable=50, fruits=100)

def print_max(x, y):
    '''
    Prints the maximum of two numbers.
    The two values must be integers.
    '''
    x = int(x)
    y = int(y)

    if x > y:
        print x, 'is maximum'
    elif y > x:
        print y, 'is maximum'

print print_max.__doc__
print_max(3, 5)
help(print_max)

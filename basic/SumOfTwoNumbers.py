import constants

"""
this is a function. indentation here defines a block of code
sum is identifer; def is a keyword; a & b here are arguments or parameters.
"""


def sum(a, b):
    # sum = input("enter values")
    print('a+b=', a + b)
    return a + b


def multiply(a, b):
    print('a*b=', a * b)


def divison(a, b):
    print('a/b=', a / b)
    # subtraction(a,b)


def subtraction(a, b):
    print('a-b=', a - b)


if __name__ == "__main__":
    a = int(input('enter number a\n'))
    b = constants.PI
    print('value of b=', b)
    d = sum(a, b)
    c = int(input('enter number c\n'))
    sum(a,b,c)
    sum(c, d)
    multiply(a, b)
    divison(a, b)
    subtraction(a, b)
    e = constants.GRAVITY
    print('value of Gravity=', e)
    f = r'Hello\xfrom AskPython'
    print(f)

    g = 'true' + 4
    h = False + 5

    print('g:', g)
    print('h:', h)
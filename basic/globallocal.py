x = "global "


def foo():
    # global x
    # x = 'sai '
    x = x + "padmini"
    print(x)
    y = "local"
    print(y)


def bar():
    print(x)


if __name__ == '__main__':
    foo()
    bar()
    # print(x)


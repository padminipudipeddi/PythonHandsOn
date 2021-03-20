# functions are first class citizens
double = lambda x, y: x * y

if __name__ == '__main__':
    print(double(5, 4))
    ""
# program for filter() function in lamda


if __name__ == '__main__':
    padmini_list = (input('please enter numbers here:'))
    x = list(padmini_list)
    new_list = list(filter(lambda a: a % 3 == 0, x))
    print(new_list)

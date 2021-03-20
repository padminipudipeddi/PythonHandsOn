def find_infinite_loop():
    list_is = []

    while True:
        input_console = input("Enter an integer: ")
        if input_console == 'X':
            break
        else:
            list_is.append(int(input_console))
            list_is.sort()
            print('infinite loop is:', input_console)
    return list_is


if __name__ == '__main__':
    # number = input('Please enter integer:')
    output = find_infinite_loop()
    print('sorted numbers:', output)

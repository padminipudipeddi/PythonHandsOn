def greet(*names):
    """This function greets all
    the person in the names tuple."""
    print('This is of type:', type(names))
    # names is a tuple with arguments
    for name in names:
        print("Hello", name)


if __name__ == '__main__':
    greet("Monica", "Luke", "Steve", "John")

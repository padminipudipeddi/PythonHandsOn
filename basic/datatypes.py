def find_datatype(input):
    print('Name is:', input, type(input))


## main method; this is the starting point for
## python program
if __name__ == "__main__":
    '''sabv'''
    a = [1, 2, 2, 3, 3, 3]
    print(a[5])
    # reading input from console #
    input_from_console = 0.12345678901234567
    # calling function find_datatype
    find_datatype(input_from_console)

# slicing operation #

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print('operation slicing:', a[0:5])
print('slicing from index 3:',a[3:])
print('slice', a[2:7])
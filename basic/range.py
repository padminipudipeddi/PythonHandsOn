def reverse_number(number):
    list_of_numbers = list(number)
    #print('inside reverse_numer', list_of_numbers)
    start = len(list_of_numbers) - 1
    print('start->', start)
    result = ''
    for i in range(start,-1, -1):
        print('i=', i)
        print('list_of_numbers=',list_of_numbers[i])
        result = result + list_of_numbers[i]
        print('result=', result)
    return result


if __name__ == "__main__":
    input_number = input('please enter a numbers')
    # print('main method', input_number)
    output = reverse_number(input_number)
    print(output)

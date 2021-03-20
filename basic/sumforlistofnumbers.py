def sum_list_numbers(list_of_numbers):
    result = 0
    ## write the logic here
    for value in list_of_numbers:
        # print('value is:', value)#
        # result = 0
        result = result + value
    return result


if __name__ == "__main__":
    # list_numbers = input("please enter list on numbers:")#
    list_numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    print("list of numbers:", list_numbers)

    # print("size of list is:", len(list_numbers))#
    # print("index from 3 is :", list_numbers[3:])#
    x = sum_list_numbers(list_numbers)
    print("result is:", x)

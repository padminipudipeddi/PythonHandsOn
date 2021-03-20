def reverse_numbers(input_number):
    list_of_numbers = list(input_number)
    index = len(list_of_numbers) - 1
    output = ''
    while index >= 0:
        #print('value of index is:', index)
        #print('value at the index is:', list_of_numbers[index])
        output = output + list_of_numbers[index]
        #print('output is :', output)
        index = index - 1
    return output


if __name__ == "__main__":
    number = input("Enter numbers:")
    # print(numbers)
    output = reverse_numbers(number)
    print(output)

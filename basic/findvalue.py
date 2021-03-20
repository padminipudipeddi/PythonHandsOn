def find_value(list_numbers, i):
    #print(list_numbers, i)
    return list_numbers[i]


if __name__ == "__main__":
    index = int(input("enter index"))
    number = [2, 3, 4, 5]
    value = find_value(number, index)
    print("value is:", value)
import random

def generate_random(random_upper_limit, requested_random_number):
    i = 1
    list_random_numbers = []
    while i <= requested_random_number:
        number = random.randint(0, random_upper_limit)
        if number not in list_random_numbers:
            list_random_numbers.append(number)
            i = i + 1
    return list_random_numbers


def print_even_odd_number(list_random_numbers):
    for number in list_random_numbers:
        if (number % 2) == 0:
            print(number, 'is even')
        else:
            print(number, 'is odd')


if __name__ == "__main__":
    upper_limit = int(input('enter random number upper limit:'))
    requested_random_number = int(input('enter requested random number'))
    list_random_numbers = generate_random(upper_limit, requested_random_number)
    print('list of random numbers are:', list_random_numbers)
    print_even_odd_number(list_random_numbers)

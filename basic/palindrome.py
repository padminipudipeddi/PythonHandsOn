def is_a_palindrome(word):
    print('This is the entered input:', word)
    is_palindrome = True
    last_index = len(word) - 1
    start_index = 0
    while start_index <= last_index:
        if word[start_index] == word[last_index]:
            start_index = start_index + 1
            last_index = last_index - 1
        else:
            is_palindrome = False
            print('The given word', word, 'is not a palindrome')

            return is_palindrome

    return is_palindrome


if __name__ == '__main__':
    given_string = input('Please enter a word:')
    # print('Entered input string is:', given_string)
    palindrome_word = is_a_palindrome(given_string)
    print('The given string', given_string, 'is a palindrome:', palindrome_word)

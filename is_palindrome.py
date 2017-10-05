# Define a procedure is_palindrome, that takes as input a string, and returns a
# Boolean indicating if the input string is a palindrome.

# Base Case: '' => True
# Recursive Case: if first and last characters don't match => False
# if they do match, is the middle a palindrome?

def is_palindrome(string):
    if string == '':
        return True
    else:
        if string[0] != string [-1]:
            return False
        else:
            return is_palindrome(string[1:-1])



print is_palindrome('')
# >>> True
print is_palindrome('abab')
# >>> False
print is_palindrome('abba')
# >>> True
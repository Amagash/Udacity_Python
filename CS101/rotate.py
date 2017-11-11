# Write a procedure, rotate which takes as its input a string of lower case
# letters, a-z, and spaces, and an integer n, and returns the string constructed
# by shifting each of the letters n steps, and leaving the spaces unchanged.
# Note that 'a' follows 'z'. You can use an additional procedure if you
# choose to as long as rotate returns the correct string.
# Note that n can be positive, negative or zero.

def shift_n_letters(letter, n):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    i = 0
    for char in alphabet:
        i = 1 + i
        if char == letter:
            # if i + n > 26:
            return alphabet[( i + n - 1 ) % 26]

def rotate(string, n):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    new_string = ''
    for char in string:
        if char == ' ':
            new_string = new_string + ' '
        else:
            new_string = new_string + shift_n_letters(char, n)
    return new_string

print rotate ('sarah', 13)
#>>> 'fnenu'
print rotate('fnenu',13)
#>>> 'sarah'
print rotate('dave',5)
#>>>'ifaj'
print rotate('ifaj',-5)
#>>>'dave'
print rotate(("zw pfli tfuv nfibj tfiivtkcp pfl jyflcu "
                "sv rscv kf ivru kyzj"),-17)
#>>> ???
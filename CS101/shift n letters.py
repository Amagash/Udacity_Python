# Write a procedure, shift_n_letters which takes as its input a lowercase
# letter, a-z, and an integer n, and returns the letter n steps in the
# alphabet after it. Note that 'a' follows 'z', and that n can be positive,
#negative or zero.

def shift_n_letters(letter, n):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    i = 0
    for char in alphabet:
        i = 1 + i
        if char == letter:
            # if i + n > 26:
            return alphabet[( i + n - 1 ) % 26]

    # table = []
    # for char in alphabet:
    #     table.append(char)
    # for i in range (0, len(table)):
    #     if table[i] == letter:
    #
    #         return table[i + n]



print shift_n_letters('s', 1)
#>>> t
print shift_n_letters('s', 2)
#>>> u
print shift_n_letters('s', 10)
#>>> c
print shift_n_letters('s', -10)
#>>> i
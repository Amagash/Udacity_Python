# Write a procedure, shift, which takes as its input a lowercase letter,
# a-z and returns the next letter in the alphabet after it, with 'a'
# following 'z'.

def shift(letter):
    if letter == 'z':
        return 'a'
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    table = []
    for char in alphabet:
        table.append(char)
    for i in range (0, len(table)):
        if table[i] == letter:
            return table[i + 1]


print shift('a')
# >>> b
print shift('n')
# >>> o
print shift('z')
# >>> a
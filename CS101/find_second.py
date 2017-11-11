# Define a procedure, find_second, that takes
# two strings as its inputs: a search string
# and a target string. It should return a
# number that is the position of the second
# occurrence of the target string in the
# search string.

def find_second(sentence, word):
    first = sentence.find(word)
    second = sentence.find(word, first + 1)
    return second


danton = "De l'audace, encore de l'audace, toujours de l'audace"
print find_second(danton, 'audace')
# >>> 25

# first = danton.find('audace')
# print first

# second = danton.find('audace', first+1)
# print second

twister = "she sells seashells by the seashore"
print find_second(twister, 'she')
# >>> 13
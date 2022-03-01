# Practice with map
# Fill out the rest of the map functions.
# You can define additional functions if you need to.
# (a) ["apple", "orange", "pear"] => (5, 6, 4)  (length)
# (b) ["apple", "orange", "pear"] => ("APPLE", "ORANGE", "PEAR")  (uppercase)
# (c) ["apple", "orange", "pear"] => ("elppa", "egnaro", "raep")  (reversed)
# (d) ["apple", "orange", "pear"] => ("ap", "or", "pe")  (first two letters)

# Practice with filter
# Fill out the rest of the filter functions.
# You can define additional functions if you need to.
# (e) range(100) => (0, 3, 6, 9, ...)  (div by 3)
# (f) range(100) => (0, 5, 10, 15, ...)  (div by 5)
# (g) range(100) => (0, 15, 30, 45, ...)  (div by 15)
# (h) range(100) => (1, 2, 4, 7, 8, 11, 13, 14, 16, 17, ...)  (not div by 3 and not div by 5)
from audioop import reverse


def condition(element):
    return element % 5 == 0

if __name__ == '__main__':
    fruits = ["apple", "orange", "pear"]
    a = map(len, fruits)
    b = map(str.upper, fruits)
    c = map(lambda x: x[::-1] , fruits)
    d = map(lambda x: x[:2], fruits)

    e = filter(lambda x: x % 3 == 0, range(100))
    f = filter(lambda x: x % 5 == 0, range(100))
    g = filter(lambda x: x % 15 == 0, range(100))
    h = filter(lambda x: x % 3 != 0 and x % 5 != 0, range(100))

    print(list(a))
    print(list(b))
    print(list(c))
    print(list(d))
    print(list(e))
    print(list(f))
    print(list(g))
    print(list(h))

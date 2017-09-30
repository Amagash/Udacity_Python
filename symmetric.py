# A list is symmetric if the first row is the same as the first column,
# the second row is the same as the second column and so on. Write a
# procedure, symmetric, which takes a list as input, and returns the
# boolean True if the list is symmetric and False if it is not.

def is_square (table):
    for row in table:
        if len(row) != len(table):
            return False
    return True

def symmetric(list):
    if is_square(list) == False:
        return False
    col = []
    for i in range(0, len(list)):
        for row in list:
            col.append(row[i])
        if col == list[i]:
            col = []
            i = i + 1
        else:
            return False
    return True




print symmetric([[1, 2, 3],
               [2, 3, 4],
               [3, 4, 1]])
#>>> True

print symmetric([["cat", "dog", "fish"],
               ["dog", "dog", "fish"],
               ["fish", "fish", "cat"]])
#>>> True

print symmetric([["cat", "dog", "fish"],
               ["dog", "dog", "dog"],
               ["fish","fish","cat"]])
#>>> False

print symmetric([[1, 2],
               [2, 1]])
#>>> True

print symmetric([[1, 2, 3, 4],
               [2, 3, 4, 5],
               [3, 4, 5, 6]])
#>>> False

print symmetric([[1,2,3],
                [2,3,1]])
#>>> False
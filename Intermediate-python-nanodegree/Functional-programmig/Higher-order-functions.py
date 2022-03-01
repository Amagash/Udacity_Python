"""
Why are maps et filters better ? Because they are lazy meaning they only compute when asked so it's better for the memory.
As far as speed goes they are comparable to list comprehensions.
Map:
Here are three different ways of doing the same thing with the no_map, the yes_map and the map functions.
"""
def do_something(element):
    return element + 1

def no_map(iterable):
    output = []
    for element in iterable:
        val = do_something(element)
        output.append(val)
    return output

def yes_map(iterable):
    output = [
        do_something(element)
        for element in iterable
    ]
    return output

map(do_something, [1, 2, 3])
"""
Filter:
Here are three different ways of filtering elements with the no_filter, the yes_filter and the filter functions.

"""
def condition(element):
    """
    Check if element is even
    """
    return element % 2 == 0

def no_filter(iterable):
    output = []
    for element in iterable:
        if condition(element):
            output.append(element)
    return output

def yes_filter(iterable):
    output = [
        element
        for element in iterable
        if condition(element)
    ]
    return output

filter(condition, [1, 2, 3, 4, 5, 6])


if __name__ == '__main__':
    print(no_map([1, 2, 3]))
    print(yes_map([1, 2, 3]))
    print(list(map(do_something, [1, 2, 3])))

    print(no_filter([1, 2, 3, 4, 5, 6]))
    print(yes_filter([1, 2, 3, 4, 5, 6]))
    print(list(filter(condition, [1, 2, 3, 4, 5, 6])))
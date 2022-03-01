"""
Lambda functions are anonymous, on-the-fly functions that are used for simple callables that don't need to clutter the local namespace.
"""

def small_function(number):
    if number > 3:
        return True
    else:
        return False

if __name__ == '__main__':
    print(small_function(4))
    print(small_function(2))
    print(small_function(5))

    print((lambda number: number > 3)(4)) # => True

    # Squares from 0**2 to 9**2
    print(list(map(lambda val: val ** 2, range(10))))

    # Tuples with positive second elements
    print(list(filter(lambda pair: pair[1] > 0, [(4,1), (3, -2), (8,0)])))

    # Sort a collection based on a custom function.
    print(list(sorted([(4,1), (3, -2), (8,0)], key=lambda pair: pair[1])))
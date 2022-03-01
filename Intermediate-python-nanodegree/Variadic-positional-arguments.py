"""
A variadic parameter collection collects excess arguments (that would otherwise go unmatched to a parameter) into a data structure, 
for the function implementation's use. 
There are two kinds of variadic parameters: variadic positional parameters (*) and variadic keyword parameters (**).
"""

def print_my_arguments(a, *b, c=1):
    print(f"a={a}, b={b}, c={c}")

def product(*nums, start=1):
    running_product = start
    for number in nums:
        running_product *= number
    return running_product

if __name__ == '__main__':
    print_my_arguments(2)                   # a=2, b=(), c=1
    print_my_arguments(2, 7)                # a=2, b=(7,), c=1
    print_my_arguments(2, 7, 1)             # a=2, b=(7, 1), c=1
    print_my_arguments(2, 7, 1, 8)          # a=2, b=(7, 1, 8), c=1
    print_my_arguments(2, 7, 1, 8, 2)       # a=2, b=(7, 1, 8, 2), c=1
    print_my_arguments(2, 7, 1, 8, 2, c=8)  # a=2, b=(7, 1, 8, 2), c=8

    print(product(3, 5))  # => 15
    print(product(3, 4, 2))  # => 24
    print(product(3, 4, 2, 5))  # => 120
    print(product())  # => 1
    print(product(7, start=15))  # => 105
    print(product(5, 6, start=10))  # => 300
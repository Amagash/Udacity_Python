# Define a procedure, fibonacci, that takes a natural number as its input, and
# returns the value of that fibonacci number.

# Two Base Cases:
#    fibonacci(0) => 0
#    fibonacci(1) => 1

# Recursive Case:
#    n > 1 : fibonacci(n) => fibonacci(n-1) + fibonacci(n-2)

def fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


#Define a faster fibonacci procedure that will enable us to computer
#fibonacci(36).

def fibonacci(n):
    current = 0
    after = 1
    for i in range(0,n):
        current, after = after, current + after
    return current


print fibonacci(36)
#>>> 14930352


print fibonacci(0)
#>>> 0
print fibonacci(1)
#>>> 1
print fibonacci(15)
#>>> 610
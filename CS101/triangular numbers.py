# Question 2. Triangular Numbers

# The triangular numbers are the numbers 1, 3, 6, 10, 15, 21, ...
# They are calculated as follows.

# 1
# 1 + 2 = 3
# 1 + 2 + 3 = 6
# 1 + 2 + 3 + 4 = 10
# 1 + 2 + 3 + 4 + 5 = 15

# Write a procedure, triangular, that takes as its input a positive
# integer n and returns the nth triangular number.

def triangular(n):
    sum = 1
    i = 2
    while i <= n:
        sum = sum + i
        i = i + 1
    return sum



print triangular(1)
#>>>1

print triangular(3)
#>>> 6

print triangular(10)
#>>> 55

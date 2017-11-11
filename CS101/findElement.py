# Define a procedure, find_element,
# that takes as its inputs a list
# and a value of any type, and
# returns the index of the first
# element in the input list that
# matches the value.

# If there is no matching element,
# return -1.

# with a while loop
def find_element_while (p, t):
    i = 0
    while i<len(p):
      if p[i] == t:
          return i
      i = i + 1

    return -1

# with a for loop
def find_element_for(p, t):
    i = 0
    for e in p:
        if e == t:
            return i
        i = i + 1
    return -1

# built in functions
def find_element_builtIn (p, t):
    if t in p:
        return p.index (t)
    return -1

print find_element_while([1, 2, 3], 3)
print find_element_for([1, 2, 3], 3)
print find_element_builtIn([1, 2, 3], 3)

# >>> 2

print find_element_while(['alpha', 'beta'], 'gamma')
print find_element_for(['alpha', 'beta'], 'gamma')
print find_element_builtIn(['alpha', 'beta'], 'gamma')
# >>> -1